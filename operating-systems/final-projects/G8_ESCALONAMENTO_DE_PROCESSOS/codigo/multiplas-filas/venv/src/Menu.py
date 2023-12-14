import implementation
def Menu():

    print("=====Implementação Múltiplas Filas=====")
    print("Digite um número correspondente a ação:")
    print("1 - Criar Fila Multipla | 2 - Criar SubFila | 3 - Criar Processo | 4 - Executa Processo |5 - Mostrar processos | 0 - Encerra Programa")
    resposta = int(input("---> "))
    while True:
        if(resposta == 1):
            global filaMultipla
            filaMultipla = implementation.CriarMultiplasFilas()
            print("Fila múltipla criada...")
            Menu()

        if(resposta == 2):
            implementation.AdicionaSubfila(filaMultipla)
            print("Subfila adicionada...")
            Menu()

        if (resposta == 3):
            print("=====CRIANDO PROCESSO=====")
            nome = str(input("Digite o nome: "))
            id = str(input("Digite o ID: "))
            prioridade = int(input("Digite a prioridade do processo(Numero inteiro de 0 a n): "))
            processo = implementation.CriaProcesso(nome, id, prioridade)
            if(implementation.AdicionaProcessoNaFila(filaMultipla, processo) == 1):
                print("Processo Adicionado com sucesso...")
                Menu()
            else:
                Menu()
        if(resposta == 4):
            implementation.ExecutaProcesso(filaMultipla)
            Menu()
        if(resposta == 5):
            implementation.MostraFilas(filaMultipla)
            Menu()
        if(resposta == 0):
            break


