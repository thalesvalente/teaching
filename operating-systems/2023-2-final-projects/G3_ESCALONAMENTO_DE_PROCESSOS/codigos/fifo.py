import matplotlib.pyplot as plot
import pandas as pd
#importa bibliotecas que serão usadas para plotar um gráfico e para imprimir o output de forma organizada

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
    #lista vazia onde serão adicionados os processos
    
    print('Insira o tempo de computação de cada processo')
    for i in range(prc):
        while True:
            try:
                tempo_comp = int(input(f'P{i+1}: '))
                if tempo_comp > 0:
                    break
                else: 
                    print('Por favor, insira um número inteiro positivo.')
            except ValueError:
                print('Por favor, insira um número inteiro válido.')
        processos.append([i + 1, tempo_comp])
        #loop que pede ao usuário o tempo de computação de cada processo dentro da variável 'prc'
        #os valores digitados pelo usuário não podem ser negativos ou letras/símbolos
        #adiciona uma lista contendo o ID do processo (i + 1) e o tempo de computação a lista processos
        
    #loop que calcula o tempo de espera entre processos
    tempo_esp = 0
    for i in range(prc):
        processos[i].append(tempo_esp) #adiciona o valor atual de 'temp_esp' a uma sublista de 'processos' 
        tempo_esp += processos[i][1] #a cada iteração do loop, esta linha soma o valor atual de 'tempo_esp' com o tempo de computação do i-ésimo processo
    
    #loop que calcula o tempo de turnaround entre processos
    total_turnaround = 0
    for i in range(prc):
        tempo_turn = processos[i][1] + processos[i][2] #calula o tempo de turnaound do i-ésimo processo, somando o tempo de computação com o de espera
        total_turnaround += tempo_turn #acumula a soma total do tempo de turnaround de todos os processos
        processos[i].append(tempo_turn) #adiciona ao final da lista associada ao i-ésimo processo
    
    dfprocessos = pd.DataFrame(processos, columns=['ID Processo', 'Tempo de Computação', 'Tempo de Espera', 'Tempo de Turnaround'])
    #usamos a biblioteca pandas para imprimir o output de forma organizada e alinhada
    print('\n')
    print(dfprocessos.to_string(index=False)) #imprime o dataframe sem exibir os índices das linhas
    
    med_esp = sum(p[2] for p in processos)/prc #calcula a média de espera 
    med_turn = total_turnaround/prc #caclula a média do tempo de turnaound
    
    print(f'\nO tempo médio de espera é de: {med_esp:.2f}') 
    print(f'O tempo médio de Turnaround é de: {med_turn:.2f}')
    #print das informações média de espera e média de turnaound
    
    #cria um gráfico para exemplificar o algoritmo FIFO de forma mais dinâmica
    gantt_pos = [(p[2], p[3]) for p in processos] #é uma lista de tuplas que representa a posição inicial e final de cada processo no chart
    #p[2] representa o tempo de espera e p[3] representa o tempo de turnaround
    fim_pos = processos[-1][3]
    fig, ax = plot.subplots(figsize=(10, 4)) #cria uma figura e um conjunto de eixos, a figura é do tipo 10x4

    for i, task in enumerate(gantt_pos): #inicia um loop que itera sobre a lista 'gantt_pos'
        start, end = task
        duracao = end - start + 1  #calcula a duração da barra de processos e garante que cada um tenha pelo menos 1 unidade de tempo
        ax.broken_barh([(start, duracao)], (1.2, 0.6),
                facecolors=f'C{processos[i][0]-1}', label=f"P{processos[i][0]}")
        ax.annotate(f"P{processos[i][0]}", xy=(start , 1.5), xycoords='data',
                xytext=(1.5, 1.5), textcoords='offset points')
        ax.annotate(start, xy=(start, .8), xycoords='data', xytext=(1.5, 1.5), textcoords='offset points')
        #personalização do gráfico, define uma cor para cada processo e um rótulo para cada processo

    ax.annotate(fim_pos, xy=(fim_pos, .8), xycoords='data',
            xytext=(1.5, 1.5), textcoords='offset points')

    ax.set_title('Gantt Chart - First In First Out')
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