from alocacao_encadeada import AlocacaoEncadeada  # Importa a classe de alocação contígua
import os  # Importa o módulo do sistema operacional
from anytree import Node, RenderTree  # Importa as classes Node e RenderTree do anytree

class SimpleOSSimulated:
    def __init__(self):
        # Inicialização do sistema operacional simulado
        self.filesystem = Node("Diretorio-raiz")  # Cria o nó raiz do sistema de arquivos
        self.current_directory = self.filesystem  # Define o diretório atual como o diretório raiz
        self.current_file = None  # Guarda o arquivo atualmente aberto

        self.file_allocation = AlocacaoEncadeada(disk_space=13)  # Inicializa a alocação contígua com espaço em disco de 13 blocos

    def command_prompt(self):
        self.clear_screen()
        while True:
            command = input("SimpleOS> ").strip().split()  # Recebe o comando do usuário e o separa em partes
            if not command:
                continue
            if command[0] == "exit":
                print("Encerrando o SimpleOS...")
                break
            elif command[0] == "ls":
                self.list_directory()
            elif command[0] == "clean":
                self.clear_screen()
            elif command[0] == "help":
                self.help()
            elif command[0] == "create":
                if len(command) > 2:
                    self.create_file(command[1], command[2])
                else:
                    print("Nome do arquivo ou tamanho do arquivo não especificados.")
            elif command[0] == "mkdir":
                if len(command) > 1:
                    self.create_directory(command[1])
                else:
                    print("Nome do diretório não especificado.")
            elif command[0] == "cd":
                if len(command) > 1:
                    self.change_directory(command[1])
                else:
                    print("Nome do diretório não especificado.")
            elif command[0] == "remove":
                if len(command) > 1:
                    self.remove_file(command[1])
                else:
                    print("Nome do arquivo não especificado")

            elif command[0] == "renamedir":
                if len(command) > 2:
                    self.rename_directory(command[1],command[2])
                else:
                    print("Nome do diretorio não especificado")                 
            elif command[0] == "disk":
                self.file_allocation.display_disk_allocation()

            elif command[0] == "open":
                if len(command) > 1:
                    self.open_file(command[1])
                else:
                    print("Nome do arquivo não especificado.")
            elif command[0] == "write":
                if len(command) > 1:  
                    content_to_write = ' '.join(command[1:])  
                    self.write_to_file(content_to_write)  
                else:
                    print("Conteúdo não especificado para escrita.")
            elif command[0] == "read":
                if len(command) > 1:
                    self.read_from_file(command[1])
                else:
                    print("Nome do arquivo não especificado.")
            elif command[0] == "close":
                if len(command) > 1:
                    self.close_file(command[1])
                else:
                    print("Nome do arquivo não especificado.")
            else:
                print(f"Comando '{command[0]}' não reconhecido.")
    
    def help(self):
        print("""
        Comandos disponíveis:
        - ls: Listar conteúdo do diretório atual.
        - create <nome_arquivo> <tamanho> <algoritmo>: Criar um arquivo com um algoritmo de alocação (first-fit, best-fit, worst-fit).
        - mkdir <nome_diretório>: Criar um diretório.
        - cd <nome_diretório>: Mudar para um diretório.
        - remove <nome_arquivo>: Remover um arquivo.
        - renamedir <nome_antigo> <novo_nome>: Renomear um diretorio.
        - disk: Mostrar alocação de disco.
        - open <nome_arquivo> <modo>: Abrir um arquivo.
        - write <conteúdo>: Escrever conteúdo em um arquivo aberto.
        - read <nome_arquivo>: Ler conteúdo de um arquivo.
        - close <nome_arquivo>: Fechar um arquivo aberto.
        - clean: Limpar a tela. 
        - exit: Encerrar o SimpleOS.
        """)

    def clear_screen(self):
        # Limpa a tela do console, verificando o sistema operacional para usar o comando correto
        os.system('cls' if os.name == 'nt' else 'clear')

    def list_directory(self):
        # Lista o conteúdo do diretório atual e sua árvore hierárquica
        print(f"Diretório atual: C:{self.get_current_directory_path()}")
        for pre, _, node in RenderTree(self.current_directory):
            print("%s%s" % (pre, node.name))

    def create_directory(self, directory_name):
        # Cria um novo diretório com o nome especificado
        existing_children = [child for child in self.current_directory.children if child.name == directory_name]

        if not existing_children:
            Node(directory_name, parent=self.current_directory)  # Cria um nó representando o novo diretório
            print(f"Diretório '{directory_name}' criado com sucesso.")
        else:
            print(f"O diretório '{directory_name}' já existe.")

    def change_directory(self, directory_name):
        # Altera o diretório atual para o especificado
        if directory_name == "..":
            # Se o diretório especificado for "..", muda para o diretório pai se não estiver no diretório raiz
            if self.current_directory != self.filesystem:
                self.current_directory = self.current_directory.parent
                print("Retornou ao diretório pai.")
            else:
                print("Você já está no diretório raiz.")
        else:
            # Verifica se o diretório especificado existe entre os filhos do diretório atual
            child = next((child for child in self.current_directory.children if child.name == directory_name), None)

            if child:
                # Verifica se o nó possui um atributo 'type' antes de tentar acessá-lo
                if hasattr(child, 'type') and child.type == 'file':
                    print(f"'{directory_name}' é um arquivo, não um diretório. Não é possível entrar.")
                else:
                    self.current_directory = child  # Define o diretório atual como o especificado
                    print(f"Entrou no diretório '{directory_name}'.")
            else:
                print(f"Diretório '{directory_name}' não encontrado.")

    def get_current_directory_path(self):
        # Retorna o caminho do diretório atual
        path = self.current_directory
        path_str = ''
        while path.parent:
            path_str = '/' + path.name + path_str  # Adiciona cada nível do diretório ao caminho
            path = path.parent
        return path_str if path_str else '/'  # Retorna o caminho ou '/' se estiver no diretório raiz
 
    def create_file(self, filename, file_size):
        try:
            file_size = int(file_size)
        except ValueError:
            # Verifica se o tamanho do arquivo é um número inteiro positivo
            print("Tamanho do arquivo deve ser um número inteiro positivo.")
            return

        if file_size <= 0:
            # Verifica se o tamanho do arquivo é positivo
            print("Tamanho do arquivo deve ser um número inteiro positivo.")
            return

        if any(node.name == filename for node in self.current_directory.children):
            # Verifica se o arquivo já existe no diretório atual
            print(f"Arquivo '{filename}' já existe.")
        else:
            allocated_blocks = self.file_allocation.allocate_file(filename,file_size)

            if allocated_blocks:
                # Cria um novo nó na árvore para representar o arquivo
                new_node = Node(filename, parent=self.current_directory, type='file', size=file_size, allocation=allocated_blocks, content='')
                print(f"Arquivo '{filename}' criado com sucesso.")
            else:
                # Indica que não há espaço suficiente para alocar o arquivo
                print(f"Espaço insuficiente para alocar o arquivo '{filename}' de tamanho {file_size}.")

    def remove_file(self, filename):
        # Busca pelo nó do arquivo na pasta atual
        file_node = next((node for node in self.current_directory.children if node.name == filename and node.type == 'file'), None)
        
        if file_node:
            allocated_block = file_node.allocation

            if allocated_block is not None:
                # Desaloca os blocos alocados para o arquivo
                success = self.file_allocation.deallocate_blocks(filename)
                if success:
                    file_node.parent = None  # Remove o nó do arquivo da árvore
                    print(f"Arquivo '{filename}' removido com sucesso e blocos desalocados.")
                else:
                    print(f"Falha ao desalocar blocos do arquivo '{filename}'.")
            else:
                file_node.parent = None  # Remove o nó do arquivo da árvore
                print(f"Arquivo '{filename}' removido com sucesso.")
        else:
            print(f"Arquivo '{filename}' não encontrado.")
    
    def rename_directory(self, current_name, new_name):
        # Teste para saber se é um arquivo, se for retorna que não é um diretorio
        # Verifica se há um nó com o nome atual (current_name) e se ele é um arquivo no diretório atual
        if any(node.name == current_name and hasattr(node, 'type') and node.type == 'file' for node in self.current_directory.children):
            print(f"{current_name} não é um diretório")
            return  # Retorna sem fazer nada se for um arquivo
        
        # Encontra o diretório com o nome atual (current_name) dentro dos filhos (children) do diretório atual
        target_directory = next((child for child in self.current_directory.children if child.name == current_name), None)
        
        # Verifica se o diretório com o nome atual foi encontrado
        if not target_directory:
            print(f"Diretório '{current_name}' não encontrado.")
            return  # Retorna se o diretório não foi encontrado
        
        # Obtém os nomes dos filhos atuais do diretório para verificar se o novo nome já existe
        existing_names = [child.name for child in self.current_directory.children]
        
        # Verifica se o novo nome já existe nos filhos do diretório atual
        if new_name in existing_names:
            print(f"Já existe um diretório com o nome '{new_name}'. Escolha outro nome.")
            return  # Retorna se o novo nome já existe
        
        target_directory.name = new_name
        print(f"Diretório '{current_name}' renomeado para '{new_name}' com sucesso.")

    def open_file(self, file_name):
        # Verifica se o arquivo está no diretório atual e é um arquivo
        if any(node.name == file_name and node.type == 'file' for node in self.current_directory.children):
            if self.current_file == file_name:
                print(f"Arquivo '{file_name}' já está aberto.")
            else:
                self.current_file = file_name  # Define o arquivo atual
                print(f"Arquivo '{file_name}' aberto.")
        else:
            print(f"Arquivo '{file_name}' não encontrado ou não é um arquivo.")



    def write_to_file(self, content):
        try:
            # Verifica se há um arquivo aberto para escrita e se é um arquivo
            if self.current_file and any(node.name == self.current_file and node.type == 'file' for node in self.current_directory.children):
                # Atualiza o conteúdo do arquivo
                for node in self.current_directory.children:
                    if node.name == self.current_file:
                        # Encontra o nó correspondente ao arquivo atual e atualiza seu conteúdo
                        node.content = content
                        print("Conteúdo escrito com sucesso.")
                        return  # Retorna após escrever com sucesso

                print("Erro ao encontrar o arquivo para escrita.")  # Se não encontrar o arquivo
            else:
                print("Nenhum arquivo aberto para escrita ou o arquivo é inválido.")  # Se não houver arquivo aberto ou se for inválido
        except KeyError:
            print("Erro ao escrever no arquivo.")  # Se ocorrer um erro ao escrever no arquivo

    def read_from_file(self, file_name):
        # Verifica se o arquivo existe no diretório atual
        if any(node.name == file_name and hasattr(node, 'type') and node.type == 'file' for node in self.current_directory.children):
            try:
                target_node = None
                # Procura pelo nó correspondente ao arquivo desejado no diretório atual
                for node in self.current_directory.children:
                    if node.name == file_name and node.type == 'file':
                        target_node = node
                        break

                if target_node:
                    # Se o arquivo for encontrado, exibe seu conteúdo
                    content = target_node.content
                    print("Conteúdo do arquivo:")
                    print(content)
                else:
                    # Se o arquivo não for encontrado ou não for um arquivo válido
                    print(f"Arquivo '{file_name}' não encontrado ou não é um arquivo.")
            except KeyError:
                # Se ocorrer um erro ao ler o arquivo
                print("Erro ao ler o arquivo.")
        else:
            # Se o arquivo não for encontrado ou não for um arquivo válido
            print(f"Arquivo '{file_name}' não encontrado ou não é um arquivo.")

    def close_file(self, file_name):
        # Verifica se o arquivo está aberto no diretório atual
        if self.current_file == file_name:
            self.current_file = None  # Define o arquivo atual como None
            print(f"Arquivo '{file_name}' fechado com sucesso.")
        else:
            print(f"Arquivo '{file_name}' não está aberto ou é inválido para fechar.")
    
# Inicialização do SimpleOS Simulado
simple_os = SimpleOSSimulated()

# Execução do prompt de comando
simple_os.command_prompt()