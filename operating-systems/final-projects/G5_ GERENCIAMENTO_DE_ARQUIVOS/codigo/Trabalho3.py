import random
import os

class Usuario:# classe para salvar o usuario
    def __init__(self, nome, senha,grupo):
        self.nome = nome
        self.senha = senha
        self.grupo = grupo # dois tipos de grupo p cliente e adm( adm pode fazer todas as funcoes,cliente apenas mexer nos seus proprios arquivos)
        self.atributo_formado = self.misturar(nome, senha)# atributo que servira como uma chave unica

    def misturar(self, nome, senha):# funcao para criar a chave unica
        mistura = list(nome + senha)
        random.shuffle(mistura)
        return ''.join(mistura)


def criar_usuario(usuarios): # funcao para cadastrar o usuario na hora da execucao
    nome = input("Digite o nome do usuário: ")
    for usuario in usuarios:
        if nome == usuario.nome: # verificacao se ja nao existe um usuario igual
            print("Já existe um usuário com este nome. Escolha outro nome.")
            return None
    
    senha = input("Digite a senha: ")
    grupo = "cliente" # grupo padronizado como cliente 
    usuario = Usuario(nome, senha, grupo)
    limpar_tela()
    print(f"Usuário {usuario.nome} criado com sucesso!")
    return usuario

def logar(usuarios): # funcao para testar se o usuario existe e se a senha fornecida ta certa
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")
    for usuario in usuarios:
        if nome == usuario.nome and senha == usuario.senha:
            limpar_tela()
            print("Login bem sucedido!")
            print("Atributo formado:", usuario.atributo_formado)
            return usuario
    limpar_tela()    
    print("Nome de usuário ou senha incorretos!")
    return None


class Arquivo: # classe para salvar o coteudo do arquivo e seu dono 
    def __init__(self, nome, conteudo, usuario):
        self.nome = nome
        self.conteudo = conteudo
        self.usuario = usuario  # Adicionando o atributo "usuario" para identificar o dono do arquivo

class Diretorio: # classe que vai salvar os arquivos 
    def __init__(self, nome, usuario):
        self.nome = nome
        self.usuario = usuario
        self.arquivos = {}
        self.proprietario_arquivos = {}  # Dicionário para armazenar proprietários dos arquivos

    def adicionar_arquivo(self, arquivo, usuario): 
        self.arquivos[arquivo.nome] = arquivo
        self.proprietario_arquivos[arquivo.nome] = usuario.nome

    def listar_arquivos(self, usuario):
        if usuario.atributo_formado == self.usuario.atributo_formado:
            return self.arquivos.keys()
        else:
            return "Acesso negado."
        
    def acessar_arquivo(self, nome_arquivo, usuario):
        if nome_arquivo in self.arquivos:
            arquivo = self.arquivos[nome_arquivo]
            if usuario.atributo_formado == arquivo.usuario.atributo_formado:
                return arquivo.conteudo
            else:
                return "Acesso negado."
        else:
            return "Arquivo não encontrado."
        
def editar_arquivo( usuario_logado,usuarios ,diretorioB ): # funcao para editar arquivos
    nome_arquivo = input("Digite o nome do arquivo que você deseja editar: ") 
    diretorio = diretorioB
    caminho_arquivo = os.path.join(diretorio, nome_arquivo) # busca o arquivo no diretorio
    
    with open(caminho_arquivo, 'r') as arquivo: # abre o arquivo
        linhas = arquivo.readlines()
        atributo_formado_arquivo = linhas[0].split(":")[1].strip() if len(linhas) > 0 else None # pega a primeira frase dos arquivos q sempre sera a chave unica
        usuario_atributo = usuario_logado.atributo_formado 
        if (atributo_formado_arquivo == usuario_atributo) or (usuario_logado.grupo =='adm'): # testa se o usuario que ta tentando editar tem a mesma chave unica do usuario criador ou se e um adm
            conteudo = ''.join(linhas[2:])
            caminho_arquivo = os.path.join(diretorio, nome_arquivo)
            if os.path.isfile(caminho_arquivo):
                with open(caminho_arquivo, 'a') as arquivo:
                    conteudo = input("Digite o conteúdo que você deseja adicionar ao arquivo: ")
                    arquivo.write("\n" + conteudo)
                    print(f"Arquivo {nome_arquivo} editado com sucesso!")
            else:
                print("Acesso negado. O arquivo não pode ser visualizado por este usuário.")
        else:
            print("Usuário não autorizado..")

def criar_arquivo(usuario_logado, usuarios,diretorioB): # funcao para criar o arquivo no diretorio alem de salvar quem foi o usuario que criou
    nome = input("Digite o nome do arquivo: ")
    conteudo = input("Digiteo conteúdo do arquivo: ") # informacoes do arquivo 
    diretorio =diretorioB  
    nome_arquivo_completo = os.path.join(diretorio, nome + ".txt")  #arquivos nesse codigo sempre sao textos
  
    atributo_formado_usuario_logado = usuario_logado.atributo_formado # salva a chave unica do usuario
  
    usuario_correspondente = next((u for u in usuarios if u.nome == usuario_logado.nome), None)
  
    if usuario_correspondente and usuario_correspondente.atributo_formado == atributo_formado_usuario_logado:
        with open(nome_arquivo_completo, "w") as arquivo:
            arquivo.write(f"Atributo_formado: {atributo_formado_usuario_logado}\n\n{conteudo}")
        print(f"Arquivo {nome}.txt criado com sucesso no diretório {diretorio}!")
    else:
        print("Usuário não autorizado.")

def visualizar_arquivo(usuario_logado, diretorio): # funcao para testar se o usuario pode acessar arquivo
    nome_arquivo = input("Digite o nome do arquivo que você deseja visualizar: ")
    diretorio_base = diretorio
    caminho_arquivo = os.path.join(diretorio_base, nome_arquivo) # procura o arquivo no diretorio especifico

    if os.path.exists(caminho_arquivo):  # Verifica se o arquivo ou diretório existe
        if os.path.isdir(caminho_arquivo):  # Verifica se é um diretório (pasta)
            diretorio_base = caminho_arquivo
            print(f"Você está agora no diretório: {diretorio_base}")
            return diretorio_base
        else:
            with open(caminho_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
            atributo_formado_arquivo = linhas[0].split(":")[1].strip() if len(linhas) > 0 else None # pega a primeira frase dos arquivos q sempre sera a chave unica
            usuario_atributo = usuario_logado.atributo_formado 
            if (atributo_formado_arquivo == usuario_atributo) or (usuario_logado.grupo =='adm'): # testa se o usuario que ta tentando editar tem a mesma chave unica do usuario criador ou se e um adm
                conteudo = ''.join(linhas[2:])
                print("Conteúdo do arquivo:")
                print(conteudo)
            else: 
                print("Acesso negado. O arquivo não pode ser visualizado por este usuário.")
    else:
        print("O arquivo ou diretório especificado não existe.")

def excluir_arquivo(usuario_logado, diretorioB):# funcao para testar se o usuario pode excluir e remocao do arquivo
    diretorio = diretorioB # salvar o diretorio
    nome_item = input("Digite o nome do arquivo ou pasta que você deseja excluir: ")
    caminho_item = os.path.join(diretorio, nome_item)

    if os.path.exists(caminho_item):
        if os.path.isfile(caminho_item):  # Verifica se é um arquivo
            with open(caminho_item, "r") as arquivo:
                linhas = arquivo.readlines()
                atributo_formado_arquivo = linhas[0].split(': ')[1].strip() # pega a primeira frase dos arquivos q sempre sera a chave unica

                if (atributo_formado_arquivo == usuario_logado.atributo_formado) or (usuario_logado.grupo =='adm'): # testa se o usuario que ta tentando editar tem a mesma chave unica do usuario criador ou se e um adm
                    arquivo.close()
                    try:
                        os.remove(caminho_item) # remove o caminho do diretorio 
                        print(f"Arquivo {nome_item} foi excluído com sucesso!")
                    except OSError as e:
                        print(f"Erro ao excluir o arquivo: {e}")
                else:
                    print("Você não tem permissão para excluir este arquivo.")
        elif os.path.isdir(caminho_item):  # Verifica se é um diretório (pasta)
            try:
                os.rmdir(caminho_item) # remove o nome da pasta do diretorio 
                print(f"Pasta {nome_item} foi excluída com sucesso!")
            except OSError as e: # testa se foi remocvido com sucesso 
                print(f"Erro ao excluir a pasta: {e}")
        else:
            print("O caminho especificado não é um arquivo ou pasta.")
    else:
        print("O arquivo ou pasta especificada não existe.")

def renomear_arquivo(usuario_logado, diretorio):
    nome_arquivo = input("Digite o nome do arquivo que você deseja renomear: ")
    caminho_arquivo = os.path.join(diretorio, nome_arquivo) # procura  o arquivo que foi passado no diretorio 

    if os.path.exists(caminho_arquivo): # testa se existe o arquivo
        with open(caminho_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
        atributo_formado_arquivo = linhas[0].split(":")[1].strip() if len(linhas) > 0 else None # pega a primeira frase dos arquivos q sempre sera a chave unica

        if (atributo_formado_arquivo == usuario_logado.atributo_formado)or (usuario_logado.grupo =='adm'): # testa se o usuario que ta tentando editar tem a mesma chave unica do usuario criador ou se e um adm
            novo_nome = input("Digite o novo nome para o arquivo: ")
            novo_caminho = os.path.join(diretorio, novo_nome) 

            try:
                os.rename(caminho_arquivo, novo_caminho) # dar o novo nome do arquivo
                print(f"Arquivo renomeado para {novo_nome} com sucesso!")
            except OSError as e:
                print(f"Erro ao renomear o arquivo: {e}")
        else:
            print("Você não tem permissão para renomear este arquivo.")
    else:
        print("O arquivo especificado não existe.")


def listar_arquivos(diretorioB): # funcao para listar o nome dos arquivos cadastrados no diretorio especifico
    print("Arquivos:")
    diretorio = diretorioB
    arquivos = os.listdir(diretorio)
    for arquivo in arquivos:
        print(arquivo)

def criar_pasta(diretorioB): # funcao para criar um subdiretorio em um diretorio especifico
    diretorio = diretorioB
    nome_pasta = input("Digite o nome da nova pasta: ")
    caminho_pasta = os.path.join(diretorio, nome_pasta)
    os.makedirs(caminho_pasta, exist_ok=True)
    print(f"Pasta {nome_pasta} criada com sucesso no diretório {diretorio}!")


def menu_logado(): # menu que aparece quando o usuario esta "logado"
    print("\n1. Listar arquivos")
    print("2. Criar arquivo")
    print("3. Editar arquivo")
    print("4. Criar pasta")
    print("5. Visualizar arquivo")
    print("6. Deslogar")
    print("7. Acessar pasta")
    print("8. Excluir arquivo/pasta")
    print("9. Voltar pasta")
    print("10. Renomear arquivo")
    opcao = input("Escolha uma opção: ")
    return opcao

def menu(): # menu antes de esta "logado"
    print("1. Login")
    print("2. Criar novo usuário")
    print("3. Usuarios criados")
    
    opcao = input("Escolha uma opção: ")
    return opcao

def limpar_tela(): # funcao para limpar a tela(nao ficar muita informacao no terminal)
    if os.name == 'nt': 
        os.system('cls')
        
def main():
    usuarios = [Usuario("gui", "123", "adm")]# usuario teste cadastrado

    diretorio_objeto = Diretorio("diretorio1", usuarios[0]) # diretorio raiz do primeiro usuario
    diretorio_objeto.adicionar_arquivo(Arquivo("arquivo1", "conteudo1", usuarios[0]), usuarios[0])

    while True:
        usuario_logado = None
        
        diretorioR = r'C:\Users\guilh\OneDrive\Área de Trabalho\Raiz'# DIRETORIO PRE-CADASTRADO COM RAIZ. TEM QUE ALTERAR PARA UM EXISTENTE DO SEU COMPUTADOR
        diretorio =  diretorioR# serve para salvar o diretorio anterior
        opcao = menu()
        limpar_tela()
        if opcao == '1':# switch do menu para fazer o login
            if usuarios:
                usuario_logado = logar(usuarios)
            else:
                print("Nenhum usuário criado ainda. Por favor, crie um usuário primeiro.")
        elif opcao == '2':
            novo_usuario = criar_usuario(usuarios)
            if novo_usuario:
                usuarios.append(novo_usuario)
        elif opcao == '3':
            print("Usuários cadastrados:")
            for usuario in usuarios:
                print(usuario.nome)
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

        while usuario_logado:# switch para rodar o menu do usuario logado
            opcao = menu_logado()
            limpar_tela()
            if opcao == '1':
                listar_arquivos(diretorio)
            elif opcao == '2':
                criar_arquivo(usuario_logado,usuarios,diretorio)
            elif opcao == '3':
                editar_arquivo( usuario_logado,usuarios ,diretorio)
            elif opcao == '4':
                criar_pasta(diretorio)
            elif opcao == '5':
                limpar_tela()
                visualizar_arquivo(usuario_logado,diretorio)
            elif opcao == '6':
                usuario_logado = None
                limpar_tela()
            elif opcao == '7':
                diretorio = visualizar_arquivo(usuario_logado,diretorio)
            elif opcao == '8':
               excluir_arquivo(usuario_logado, diretorio)
            elif opcao == '9':
               diretorio = diretorioR
               print('voltou de diretorio.')
            elif opcao == '10':
                renomear_arquivo(usuario_logado,diretorio)
            else:
                print("Opção inválida. Por favor, escolha uma opcao valida. ")

if __name__ == "__main__":
    main()