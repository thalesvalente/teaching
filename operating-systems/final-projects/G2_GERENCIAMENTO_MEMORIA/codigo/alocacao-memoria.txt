# Alocação de memória em um S.O Simulado.
# O código abaixo possui como base o código mini-so-3.py do prof. Thales Valente.
class SimpleOSSimulated_v3:
    def __init__(self, partition_sizes=None):
        # Inicializa o sistema operacional simulado com um sistema de arquivos vazio e diretório atual.
        self.filesystem = {}
        self.current_directory = self.filesystem

        # Valida e define os tamanhos das partições para a memória.
        if partition_sizes is None or len(partition_sizes) != 3:
            raise ValueError("Especifique os tamanhos das partições corretamente (3 partições necessárias).")

        total_memory_size = 10

        if sum(partition_sizes) != total_memory_size:
            raise ValueError("A soma dos tamanhos das partições deve ser igual ao tamanho total da memória.")

        self.partition_sizes = partition_sizes
        self.partition_table = [None] * 3
        self.memory = [[None] * size for size in partition_sizes]
        self.segment_table = [{"start": 0, "end": size, "program": None, "permissions": ""} for size in partition_sizes]

    # FUNÇÕES GERENCIAMENTO MEMORIA
    # 1 = FUNÇÃO DE ALOCAÇÂO MEMÓRIA
    def allocate_memory(self, program, size=1, partition_index=0, permissions=""):
        # Verifica se o índice da partição é válido.
        if 0 <= partition_index < 3:
            required_permissions = "rwx" if partition_index == 0 else "rw"  # Partição 0 exige rwx, outras exigem rw
            partition_size = self.partition_sizes[partition_index]

            # Verifica se o tamanho e as permissões são válidos para a alocação.
            if size > partition_size or not all(p in permissions for p in required_permissions):
                return -1, 0

            # Encontra um bloco contíguo na partição para o programa.
            start_index = -1
            for i in range(partition_size - size + 1):
                if all(self.memory[partition_index][i + j] is None for j in range(size)):
                    start_index = i
                    break

            if start_index == -1:
                return -1, 0  # Não foi possível encontrar um bloco contíguo na partição

            # Aloca memória para o programa na partição.
            for j in range(size):
                self.memory[partition_index][start_index + j] = (program, size)
                self.segment_table[partition_index] = {
                    "start": start_index,
                    "end": start_index + size,
                    "program": program,
                    "permissions": permissions,
                }

            self.partition_table[partition_index] = (program, size)

            return start_index, size

        return -1, 0  # Índice de partição inválido

    # 2 = FUNÇÃO DE LIBERAÇÃÕ MEMÓRIA
    def free_memory(self, partition_index, size=1):
        if 0 <= partition_index < 3:
            partition_size = self.partition_sizes[partition_index]
            for i in range(size):
                self.memory[partition_index][i] = None
            self.segment_table[partition_index] = {"start": 0, "end": partition_size, "program": None, "permissions": ""}
            self.partition_table[partition_index] = None  # Remover a entrada da tabela de partições
            return True
        return False

    # 3 = FUNÇÃO DE IMPRESSAO TABELA PARTIÇÕES
    def print_partition_table(self):
        print("==============================================================")
        print("Tabela de Partições:")
        for index, entry in enumerate(self.partition_table):
            if entry is None:
                print(f"Partição {index}: Empty")
            else:
                program, size = entry
                if callable(program):  # Verifica se é uma função (programa)
                    program_name = program.__name__
                else:
                    program_name = str(program)  # Se não for uma função, trata como uma string

                print(f"Partição {index}: Programa {program_name}, Size: {size}")

        print("\nLocais Livres:")
        for partition_index, partition_memory in enumerate(self.memory):
            print(f"Partição {partition_index}: ", end="")
            free_locations = [index for index, unit in enumerate(partition_memory) if unit is None]
            if not free_locations:
                print("Nenhum local livre")
            else:
                print(f"Locais livres nos índices {free_locations}")

        print("==============================================================")
    # 4 = FUNÇÃO DE CHECAGEM DE PERMISSOES EM PARTIÇÕES
    def check_memory_access(self, partition_index, address, required_permissions=""):
        segment_info = self.segment_table[partition_index]

        return (
                segment_info["start"] <= address < segment_info["end"]
                and all(p in segment_info.get("permissions", "") for p in required_permissions)
        )


    # FUNÇÕES DE PROGRAMAS SIMULADOS
    # 1 = FUNÇÃO DE EXECUCAO DE PROGRAMAS
    def execute_program(self, program_name, *args, partition_index=0):
        # Verifica se o programa está alocado na partição.
        if self.partition_table[partition_index] is not None and self.partition_table[partition_index][
            0] == program_name:

            # Verifica se o programa tem permissões para acessar a partição.
            required_permissions = "rwx" if partition_index == 0 else "rw"
            if not self.check_memory_access(partition_index, 0, required_permissions):
                print(
                    f"ERRO DE PERMISSÃO: Acesso negado de {program_name} à partição {partition_index} com permissões {required_permissions}.")
                print("==============================================================")
                return None

            # Caso positivo, executa o programa determinado
            if program_name == "calc":
                return self.program_calc(*args)
            elif program_name == "echo":
                return self.program_echo(*args)
        else:
            print(f"ERRO: Programa '{program_name}' não está alocado na partição {partition_index}.")
            print("==============================================================")
            return None

    # 2 = PROGRAMA CALCULADORA
    def program_calc(self, *args):
        if len(args) == 0:
            operation = input("Digite a operação a ser realizada (add, sub): ")
            args = [operation] + list(map(int, input("Digite os operandos separados por espaço: ").split()))

        if args[0] == "add":
            return sum(args[1:])
        elif args[0] == "sub":
            return args[1] - sum(args[2:])
        else:
            return f"Operação '{args[0]}' não reconhecida."

    # 3 = PROGRAMA MENSAGEM
    def program_echo(self, *args):
        if len(args) == 0:
            message = input("Digite a mensagem a ser ecoada: ")
            args = [message]

        return args[0]

    # PROMPT DE COMANDO
    def run_command_prompt(self):
        while True:
            print("                    PROMPT DE COMANDO")
            print("==============================================================")

            command = input("Digite um comando (allocate, free, execute, memory, exit): ").lower()

            if command == "allocate":
                self.run_allocate_command()
            elif command == "free":
                self.run_free_command()
            elif command == "execute":
                self.run_execute_command()
            elif command == "memory":
                self.print_partition_table()
            elif command == "exit":
                print("Sistema encerrado.")
                break
            else:
                print("Comando inválido. Tente novamente.")

    # FUNÇÃO PARA ALOCAR UM PROGRMA
    def run_allocate_command(self):
        print("==============================================================")
        partition_index = int(input("Digite o índice da partição (0, 1, 2): "))
        program_name = input("Digite o nome do programa: ")
        size = int(input("Digite o tamanho do programa: "))
        permissions = input("Digite as permissões (r, w, x): ")
        start_index, allocated_size = self.allocate_memory(program_name, size, partition_index, permissions)
        if start_index == -1:
            print("Falha ao alocar memória.")
        else:
            print(f"Memória alocada com sucesso: Partição {partition_index}, Início {start_index}, Tamanho {allocated_size}, Permissões: {permissions}")

    # FUNÇÃO PARA LIBERAR MEMORIA DE UMA PARTIÇÃO
    def run_free_command(self):
        print("==============================================================")
        partition_index = int(input("Digite o índice da partição (0, 1, 2): "))
        size = int(input("Digite o tamanho do bloco a ser liberado: "))
        success = self.free_memory(partition_index, size)
        if success:
            print(f"Memória liberada com sucesso: Partição {partition_index}, Tamanho {size}.")
        else:
            print("Falha ao liberar memória.")

    # FUNÇÃO PARA EXECUTAR UM PROGRMA
    def run_execute_command(self):
        print("==============================================================")
        partition_index = int(input("Digite o índice da partição (0, 1, 2): "))
        program_name = input("Digite o nome do programa a ser executado (calc, echo): ")
        if program_name in ["calc", "echo"]:
            result = self.execute_program(program_name, partition_index=partition_index)
            print(f"Resultado da execução: {result}")
            print("==============================================================")
        else:
            print("Programa não reconhecido.")



# TESTE DE MEMÓRIA
partition_sizes = [4, 3, 3]
simple_os_v3 = SimpleOSSimulated_v3(partition_sizes=partition_sizes)

# Alocação de memória em diferentes partições com permissões específicas
start_index_echo, size_echo = simple_os_v3.allocate_memory("echo", size=2, partition_index=1, permissions="rw")
start_index_calc, size_calc = simple_os_v3.allocate_memory("calc", size=3, partition_index=0, permissions="rwx")

# Impressão do estado atual da tabela de partição após a alocação
simple_os_v3.print_partition_table()

# Recuperando os programas echo e calc da memória usando os índices
echo_memory_info = simple_os_v3.segment_table[1]
calc_memory_info = simple_os_v3.segment_table[0]

# Imprimindo os índices dos programas alocados
print("Índice do programa 'echo':", echo_memory_info["start"])
print("Índice do programa 'calc':", calc_memory_info["start"])
print("==============================================================")

# Executa os programas echo e calc na memória, com argumentos específicos
result_echo = simple_os_v3.execute_program("echo", "hello world", partition_index=1)
result_calc = simple_os_v3.execute_program("calc", "add", 1, 2, 3, partition_index=0)

# Imprimindo os resultados dos programas recuperados da memória
print("Resultado do programa 'echo':", result_echo)
print("Resultado do programa 'calc':", result_calc)
print("==============================================================")

# Liberando a memória dos programas echo e calc
success_free_echo = simple_os_v3.free_memory(1, size_echo)
success_free_calc = simple_os_v3.free_memory(0, size_calc)

# Imprimindo se as memórias foram liberadas com sucesso
print("Memória 'echo' liberada com sucesso:", success_free_echo)
print("Memória 'calc' liberada com sucesso:", success_free_calc)

# Imprimindo o estado atual da memória após a liberação
simple_os_v3.print_partition_table()


# INICIANDO O PROMP DE COMANDO
simple_os_v3.run_command_prompt()