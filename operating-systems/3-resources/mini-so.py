# Universidade Federal do Maranhão
# Author: Prof. Thales Levi Azevedo Valente
# Description: Mini Sistema Operacional
# Date: 16-08-2023

# Criar um sistema operacional completo, mesmo que básico, é uma tarefa extremamente complexa. 
# No entanto, posso guiá-lo através da criação de um "sistema operacional simulado" para fins educacionais. 
# Isso pode incluir funcionalidades básicas como:

# Um prompt de comando.
# A capacidade de executar "programas" simples.
# Um sistema de arquivos simulado.
# Gerenciamento de memória simplificado.
# Porém, observe que isso seria apenas uma simulação e não teria a complexidade de um sistema operacional real.

# Aqui está uma estrutura simples para começar:

# Estrutura:
# 1) Prompt de Comando - Pergunta ao usuário por comandos e executa as ações correspondentes.
# 2) Programas Simulados - Estes são simples funções que podem ser chamadas através do prompt de comando.
# 3) Sistema de Arquivos Simulado - Um dicionário para simular arquivos e diretórios.
# 4) Gerenciamento de Memória - Uma lista para simular a memória e suas operações.
# Vamos começar com o prompt de comando e o sistema de arquivos simulado.

# Vamos começar com o prompt de comando e o sistema de arquivos simulado.
class SimpleOSSimulated:
    def __init__(self):
        # .............. 3) Sistema de Arquivos Simulado ..............
        # Sistema de arquivos simulado usando dicionários
        self.filesystem = {}
        self.current_directory = self.filesystem

    # .............. 1) Prompt de Comando ..............
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

    # .............. 2) Programas Simulados ..............
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

# Inicializa o SimpleOS Simulado
simple_os = SimpleOSSimulated()

# ... Vamos definir uma sequência de comandos para simular a interação ....
# 1. touch para criar um arquivo chamado "documento.txt".
# 2. ls para listar os arquivos e diretórios no diretório atual.
# 3. touch para criar outro arquivo chamado "notas.txt".
# 4. ls para listar os arquivos e diretórios novamente.
# 5. rm para remover o arquivo "documento.txt".
# 6. ls para listar os arquivos e diretórios após a remoção.
# 7. Vou executar essa sequência agora.

# Definindo uma sequência de comandos para simulação
commands_sequence = [
    ("touch", "documento.txt"),
    ("ls",),
    ("touch", "notas.txt"),
    ("ls",),
    ("rm", "documento.txt"),
    ("ls",)
]

# Executando a sequência de comandos
for command in commands_sequence:
    if command[0] == "ls":
        simple_os.list_directory()
    elif command[0] == "touch":
        simple_os.create_file(command[1])
    elif command[0] == "rm":
        simple_os.remove_file(command[1])

# Agora, vamos adicionar a capacidade de executar programas simulados a partir de comandos do usuário.
simple_os.command_prompt()
