import matplotlib.pyplot as plot
import pandas as pd

def main():
    while True:
        try:
            prc = int(input('Insira a quantidade de processos: '))
            if prc > 0:
                break
            else:
                print('Por favor, insira um número inteiro positivo.')
        except ValueError:
            print('Por favor, insira um número inteiro válido.')
        #loop que pede ao usuário a quantidade de processos que ele quer computar
        #os valores digitados pelo usuário não podem ser negativos ou letras/símbolos

    processos = []

    print('Insira o tempo de chegada e de computação de cada processo')
    for i in range(prc):
        while True:
            try:
                tempo_chegada = int(input(f'P{i+1} - Tempo de Chegada: '))
                tempo_comp = int(input(f'P{i+1} - Tempo de Computação: '))
                if tempo_chegada > 0 and tempo_comp > 0:
                    break
                else:
                    print('Por favor, insira apenas números inteiros positivos.')
            except ValueError:
                print('Por favor, insira um número inteiro válido.')
        #loop que pede ao usuário o tempo de chegada e computação de cada processo dentro da variável 'prc'
        #os valores digitados pelo usuário não podem ser negativos ou letras/símbolos
                
        processos.append([i + 1, tempo_chegada, tempo_comp, tempo_comp, 0, 0, 0]) 
        #a segunda variável 'tempo_comp'[3] irá armazenar valores de tempo restante de computação
        #a posição [4] da lista armazenará o tempo de conclusão dos processos
        #a posição [5] da lista armazenará o tempo de espera dos processos
        #a posição [6] da lista armazenará o tempo de turnaround dos processos

    #inicio do escalonamento com preempção
    tempo_atual = 0
    sequencia_processos = []

    while True:
        fila_pronto = []
        fila_normal = []

        for i in range(len(processos)):
            if processos[i][1] <= tempo_atual and processos[i][3] > 0:
                fila_pronto.append(processos[i].copy())
            elif processos[i][3] > 0:
                fila_normal.append(processos[i].copy())
            #loop que itera sobre a lista de processos para identificar quais estão prontos para execução (fila_pronto) 
            #ou em estado normal (fila_normal) um processo é considerado pronto se o seu tempo de chegada for 
            #menor ou igual ao tempo_atual e se ainda tiver tempo de execução restante.

        if not fila_pronto and not fila_normal:
            break
            #se não houver processos nem na fila de prontos nem na fila normal, o escalonamento é interrompido
            #encerrando o loop principal.
            
        if fila_pronto:
            fila_pronto.sort(key=lambda x: x[3])
            tempo_atual += 1
            for k in range(len(processos)):
                if processos[k][0] == fila_pronto[0][0]:
                    break
            processos[k][3] -= 1
            if processos[k][3] == 0:
                processos[k][4] = tempo_atual  #adiciona o tempo de conclusão
            sequencia_processos.append(processos[k][0])
            #loop onde se houver processos na fila de prontos, eles são ordenados pelo tempo restante de 
            #execução (x[3]) e o processo com menor tempo restante é selecionado para execução
            #também incrementa o tempo_atual e decrementa o tempo restante de computação
            #quando o tempo restante de computação chega a zero o tempo de conclusão é registrado e o 
            #ID do processo é adicionado à sequência de processos

        if not fila_pronto:
            if tempo_atual < fila_normal[0][1]:
                tempo_atual = fila_normal[0][1]
            tempo_atual += 1
            for k in range(len(processos)):
                if processos[k][0] == fila_normal[0][0]:
                    break
            processos[k][3] -= 1
            if processos[k][3] == 0:
                processos[k][4] = tempo_atual  #adiciona o tempo atual ao tempo restante de computação
            sequencia_processos.append(processos[k][0])
            #loop onde se não houver processos na fila_pronto, o próximo processo da fila_normal é selecionado e
            #se o tempo_atual for menor que o tempo de chegada do processo, o tempo_atual é ajustado para o tempo de chegada do processo
            #o tempo_atual é incrementado e o tempo restante de computação do processo é decrementado
            #e se o tempo restante de computação chegar a zero, o tempo de conclusão é registrado 
            #e o ID do processo é adicionado à sequência de processos.

    # Calcular espera
    total_esp = 0
    for i in range(len(processos)):
        tempo_esp = processos[i][4] - processos[i][1] - processos[i][2] #calula o tempo de espera do i-ésimo processo, subtraindo o 
        #tempo de chegada e o tempo de computação do tempo de conclusão
        total_esp += tempo_esp #acumula a soma total do tempo de espera de todos os processos
        processos[i][5] = tempo_esp  #atualiza o tempo de espera dos processos

    media_espera = total_esp / len(processos) #caclula a média do tempo de espera

    # Calcular turnaround
    total_turnaround = 0
    for i in range(len(processos)):
        tempo_turn = processos[i][4] - processos[i][1] #calula o tempo de turnaound do i-ésimo processo, subtraindo o 
        #tempo de chegada do tempo de conclusão
        total_turnaround += tempo_turn #acumula a soma total do tempo de turnaround de todos os processos
        processos[i][6] = tempo_turn  #atualiza o tempo de turnaround dos processos

    media_turn = total_turnaround / len(processos) #caclula a média do tempo de turnaound

    dfprocessos = pd.DataFrame(processos, columns=['ID Processo', 'Tempo de Chegada', 'Tempo de Computação', 'Tempo Restante', 
                                                   'Tempo de Conclusão', 'Tempo de Espera', 'Tempo de Turnaround'])
    #usamos a biblioteca pandas para imprimir o output de forma organizada e alinhada
    dfprocessos = dfprocessos.drop(columns=['Tempo Restante']) #remove a coluna 'Tempo Restante' já que não queremos ela no nosso output
    print('\n')
    print(dfprocessos.to_string(index=False)) #imprime o dataframe sem exibir os índices das linhas

    print(f'\nO tempo médio de espera é de: {media_espera:.2f}')
    print(f'O tempo médio de Turnaround é de: {media_turn:.2f}')
    print(f'Sequência de execução: {sequencia_processos}')
    #imprime as médias de espera e turnaround e a sequência de execucção dos processos
    
    #gráfico para exexmplificar
    tasks = []
    inicio_tempo = 0 
    for i in range(1, len(sequencia_processos)): #loop que itera sobre os índices da 'sequencia_processos'
      if sequencia_processos[i] != sequencia_processos[i - 1]: 
        tasks.append((inicio_tempo, i - 1, sequencia_processos[i - 1])) #
        inicio_tempo = i
    tasks.append((inicio_tempo, len(sequencia_processos) - 1, sequencia_processos[-1]))
    #loop que itera sobre os índices da 'sequencia_processos' e identifica blocos de tempo consecutivos em que o
    #mesmo processo está sendo executado na lista sequencia_processos e armazena essas informações na lista tasks

    fig, ax = plot.subplots(figsize=(10, 4)) #cria uma figura e um conjunto de eixos, a figura é do tipo 10x4
    
    for i, task in enumerate(tasks):
      start, end, label = task
      duracao = end - start + 1 #calcula a duração da barra de processos e garante que cada um tenha pelo menos 1 unidade de tempo
      ax.broken_barh([(start, duracao)], (1.2, 0.6),
                facecolors=f'C{label-1}', label=str(label))
      ax.annotate(f"P{label}", xy=(start , 1.5), xycoords='data',
                xytext=(1.5, 1.5), textcoords='offset points')
      ax.annotate(start, xy=(start, .8), xycoords='data', xytext=(1.5, 1.5), textcoords='offset points')
        #personalização do gráfico, define uma cor para cada processo e um rótulo para cada processo
        
    ax.annotate(end+1, xy=(end+1, .8), xycoords='data',
                xytext=(1.5, 1.5), textcoords='offset points')

    ax.set_title('Gantt Chart - Shortest Remaning Time Next')
    plot.ylim((0,5))
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    handles, labels = plot.gca().get_legend_handles_labels() #pega os rótulos já criados
    by_label = dict(zip(labels, handles)) #cria uma legenda com as informações dos rótulos
    ax.legend(by_label.values(), by_label.keys(), bbox_to_anchor=(1.05, 1), loc='upper left', title='Processos') #posiciona a legenda
    ax.grid(False)
    ax.axis('on')
    
    #adiciona rótulos aos eixos x e y
    plot.xlabel('Eixo X')
    plot.ylabel('Eixo Y')
    
    #plota o gráfico
    plot.tight_layout()
    plot.show()
    

if __name__ == "__main__":
    main()
    #verifica se o script esta funcionando e chama a função principal