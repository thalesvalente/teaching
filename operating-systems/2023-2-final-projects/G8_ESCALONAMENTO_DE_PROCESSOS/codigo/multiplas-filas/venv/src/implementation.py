#Nesse algoritmo a prioridade das subfilas é definida pela posição dela na fila principal sendo a posição 0 a de maior prioridade
def CriarMultiplasFilas():
    fila = []
    subfila = []
    fila.append(subfila)
    return fila
#Adiciona uma nova subfila a fila
def AdicionaSubfila(filaMultipla):
    subfila = []
    filaMultipla.append(subfila)
#Cria os processos que serão executados na fila(os níveis de prioridade dependem que quantas subfilas existem)
def CriaProcesso(id, nome, prioridade):
    processo = {"nome": nome, "id": id, "prioridade": prioridade}
    return processo
#Adiciona processo na fila verificando se é possível adicioná-la
def AdicionaProcessoNaFila(fila,processo):
    prioridade = processo["prioridade"]
    tamanhoFila = len(fila)
    if(tamanhoFila > processo["prioridade"]):
        fila[prioridade].append(processo)
        return 1
    else:
        print("Prioridade não condiz com as filas existentes")
        return 0
#executa o processo com maior prioridade
def ExecutaProcesso(fila):
    tamanhoFila = len(fila)
    tamanhoSubfila = 0
    for i in range(tamanhoFila):
        tamanhoSubfila = len(fila[i])
        for j in range(tamanhoSubfila):
            processo = fila[i][j]
            print(f"[{processo["nome"]}, {processo["id"]}] executado com sucesso...")
            del fila[i][j]
            return fila



#Mostra todas as filas e a disposição dos processos
def MostraFilas(fila):
    tamanhoFila = len(fila)
    for i in range(tamanhoFila):
        print(fila[i])
