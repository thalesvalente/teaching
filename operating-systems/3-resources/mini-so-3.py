# Universidade Federal do Maranhão
# Author: Prof. Thales Levi Azevedo Valente
# Description: Mini Sistema Operacional
# Date: 16-08-2023



# 4) Gerenciamento de Memória
# Para simular o gerenciamento de memória, podemos usar uma lista para representar a memória. 
# Por simplicidade, vamos considerar cada posição da lista como uma "unidade de memória".

# Vamos começar implementando o gerenciamento de memória.
class SimpleOSSimulated_v3:
    def __init__(self):
        # Sistema de arquivos simulado
        self.filesystem = {}
        self.current_directory = self.filesystem
        
        # Memória simulada
        self.memory = [None] * 10  # 10 unidades de memória

    # Funções de gerenciamento de memória
    def allocate_memory(self, data):
        # Pega endereco de memória e valor contido
        for index, unit in enumerate(self.memory):
            # Se a unidade estiver vazia, aloca
            if unit is None:
                self.memory[index] = data
                return index
        return -1  # Memória cheia

    # Função para liberar memória
    def free_memory(self, index):
        # Se o índice estiver dentro do tamanho máximo da memória, libera
        if 0 <= index < len(self.memory):
            self.memory[index] = None
            return True
        return False


    # ... Restante do código anterior de SimpleOS-v2 ...


    # Funções de programas simulados (como anteriormente)
    # Executa o programa passado por argumento
    def execute_program(self, program_name, *args):
        # Verifica qual programa deve ser executado
        if program_name == "calc":
            # Executa o programa 'calc'
            return self.program_calc(*args)
        elif program_name == "echo":
            # Executa o programa 'echo'
            return self.program_echo(*args)
        else:
            # Caso contrário, exibe uma mensagem de erro
            return f"Programa '{program_name}' não reconhecido."
    
    # Programa calculadora simples
    def program_calc(self, operation, *args):
        # Verifica qual operação deve ser executada
        if operation == "add":
            # Se a operação for de soma, soma todos os argumentos
            return sum(args)
        elif operation == "sub":
            # Se a operação for de subtração, subtrai o primeiro argumento da soma dos demais
            return args[0] - sum(args[1:])
        else:
            # Caso contrário, exibe uma mensagem de erro
            return f"Operação '{operation}' não reconhecida."

    # Programa echo
    def program_echo(self, message):
        return message


    # ... Restante do código anterior de SimpleOS-v1 ...

    # Prompt de comando
    def command_prompt(self):
        while True:
            # Exibe o prompt de comando e lê a entrada do usuário
            command = input("SimpleOS> ").strip().split()
            if not command:
                continue

            # ....Comandos básicos....
            # Comando 'exit'
            if command[0] == "exit":
                print("Encerrando o SimpleOS...")
                break
            # Comando 'ls' para listar o diretório atual
            elif command[0] == "ls":
                self.list_directory()
            # Comando 'touch' para criar um arquivo
            elif command[0] == "touch":
                # Verifica se o nome do arquivo foi especificado
                if len(command) > 1:
                    self.create_file(command[1])
                else:
                # Caso contrário, exibe uma mensagem de erro
                    print("Nome do arquivo não especificado.")
            # Comando 'rm' para remover um arquivo
            elif command[0] == "rm":
                # Verifica se o nome do arquivo foi especificado
                if len(command) > 1:
                    self.remove_file(command[1])
                else:
                # Caso contrário, exibe uma mensagem de erro
                    print("Nome do arquivo não especificado.")
            else:
                print(f"Comando '{command[0]}' não reconhecido.")

    # Lista o conteúdo do diretório atual        
    def list_directory(self):
        # Exibe o nome de cada arquivo ou diretório
        for name, content in self.current_directory.items():
            if isinstance(content, dict):
                print(f"[DIR] {name}")
            else:
                print(f"[FILE] {name}")
    
    # Cria um arquivo no diretório atual
    def create_file(self, filename):
        # Verifica se o arquivo já existe
        if filename in self.current_directory:
            print(f"Arquivo '{filename}' já existe.")
        else:
            # Cria o arquivo vazio
            self.current_directory[filename] = ""
            print(f"Arquivo '{filename}' criado com sucesso.")
            
    # Remove um arquivo do diretório atual
    def remove_file(self, filename):
        # Verifica se o arquivo existe
        if filename in self.current_directory:
            # Remove o arquivo
            del self.current_directory[filename]
            print(f"Arquivo '{filename}' removido com sucesso.")
        else:
            # Caso contrário, exibe uma mensagem de erro
            print(f"Arquivo '{filename}' não encontrado.")


# Testando o gerenciamento de memória
simple_os_v3 = SimpleOSSimulated_v3()

allocated_1 = simple_os_v3.allocate_memory("Programa 1")
allocated_2 = simple_os_v3.allocate_memory("Programa 2")
memory_after_allocation = simple_os_v3.memory.copy()

freed = simple_os_v3.free_memory(allocated_1)
memory_after_release = simple_os_v3.memory.copy()



# allocated_1, allocated_2, memory_after_allocation, freed, memory_after_release
# imprima todas as variáveis acima para ver o resultado
# imprima o indice do programa 1
print("Índice do programa 1: " + str(allocated_1))
# imprima o indice do programa 2
print("Índice do programa 2: " + str(allocated_2))
# imprima a memória após alocação
print("Memória após alocação: " + str(memory_after_allocation))
# imprima o resultado da liberação
print("Resultado da liberação: " + str(freed))
# imprima a memória após liberação
print("Memória após liberação: " + str(memory_after_release))
