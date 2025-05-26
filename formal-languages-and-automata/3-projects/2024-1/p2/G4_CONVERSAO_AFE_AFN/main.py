from collections import defaultdict
from graphviz import Digraph

# Função para calcular o fecho-epsilon de um estado
def fecho_epsilon(estado, transicoes):
    fecho = {estado}
    pilha = [estado]
    while pilha:
        estado_atual = pilha.pop()
        if 'ϵ' in transicoes[estado_atual]:
            for prox_estado in transicoes[estado_atual]['ϵ']:
                if prox_estado not in fecho:
                    fecho.add(prox_estado)
                    pilha.append(prox_estado)
    return fecho


def afe_afn(afn_epsilon):
    # Calcula o fecho-epsilon para todos os estados
    fecho_epsilon_todos = {estado: fecho_epsilon(estado, afn_epsilon['transicoes']) for estado in afn_epsilon['estados']}
    # Novos estados {'q2': {'q2'}, 'q0': {'q2', 'q0', 'q1'}, 'q1': {'q2', 'q1'}}

    # Cria o novo conjunto de transições sem epsilon
    novas_transicoes = defaultdict(lambda: defaultdict(set))


    for estado in afn_epsilon['estados']: # Percorrendo estados q0, q1, q2
        print(f'Estado: {estado}')
        for simbolo in afn_epsilon['alfabeto']: # Percorrendo alfabeto a, b
            destinos = set()
            print(f'Simbolo: {simbolo}')
            for estado_fecho in fecho_epsilon_todos[estado]: # Usando q0, q1, q2 para percorrer Novos estados {'q2': {'q2'}, 'q0': {'q2', 'q0', 'q1'}, 'q1': {'q2', 'q1'}}
                print(f'Fecho: {estado_fecho}')
                if simbolo in afn_epsilon['transicoes'][estado_fecho]:
                    print(f'Simbolo encontrado!!!')
                    for destino in afn_epsilon['transicoes'][estado_fecho][simbolo]:
                        destinos.update(fecho_epsilon_todos[destino])
                        print(f'Destino: {destino}')
                else:
                    print(f'Simbolo NÃO encontrado!!!')
            if destinos:
                novas_transicoes[estado][simbolo] = destinos
            print(f'Destinos: {novas_transicoes}\n\n')

    # Determinar os novos estados finais
    novos_estados_finais = set()
    for estado in afn_epsilon['estados']:
        if any(estado_fecho in afn_epsilon['finais'] for estado_fecho in fecho_epsilon_todos[estado]):
            novos_estados_finais.add(estado)

    # Definição do novo AFN
    afn = {
        'estados': afn_epsilon['estados'],
        'alfabeto': afn_epsilon['alfabeto'],
        'transicoes': novas_transicoes,
        'inicial': afn_epsilon['inicial'],
        'finais': novos_estados_finais
    }
    return afn

# Função para imprimir o AFN resultante de forma legível
def imprimir_automato(afn):
    print("Estados:", afn['estados'])
    print("Alfabeto:", afn['alfabeto'])
    print("Estado Inicial:", afn['inicial'])
    print("Estados Finais:", afn['finais'])
    print("Transições:")
    for estado, trans in afn['transicoes'].items():
        for simbolo, destinos in trans.items():
            for destino in destinos:
                print(f"δ({estado}, {simbolo}) -> {destino}")
    print('\n\n')

def graficos(automato, nome_grafico):
    # Grafo do AFϵ e AFN
    afe = Digraph(nome_grafico, filename=nome_grafico, format='png')
    afe.attr(rankdir='LR', size='10,7')

    # Estados
    afe.attr('node', shape='doublecircle')
    for i in automato['finais']:
        afe.node(i)
    afe.attr('node', shape='circle')
    for i in automato['estados']:
        afe.node(i)

    # Transições
    for estado_entrada in automato['transicoes']:
        for alfabeto in automato['transicoes'][estado_entrada]:
            for estado_saida in automato['transicoes'][estado_entrada][alfabeto]:
                afe.edge(estado_entrada, estado_saida, label=alfabeto)
    
    afe.view()





# Utilização do programa
"""
# EXEMPLO 1
ex1_afn_epsilon = {
    'estados': {'q0', 'q1'},
    'alfabeto': {'a', 'b'},
    'transicoes': {
        'q0': {'a': {'q0'}, 'ϵ': {'q1'}},
        'q1': {'b': {'q1'}}
    },
    'inicial': 'q0',
    'finais': {'q1'}
}


ex1_afn = afe_afn(ex1_afn_epsilon)
# Imprime o AFN resultante
imprimir_automato(ex1_afn_epsilon)
imprimir_automato(ex1_afn)
graficos(ex1_afn_epsilon, 'ex1_afn_epsilon')
graficos(ex1_afn, 'ex1_afn')
"""


"""
 # EXEMPLO 2
ex2_afn_epsilon = {
    'estados': {'q0', 'q1', 'q2'},
    'alfabeto': {'a', 'b'},
    'transicoes': {
        'q0': {'a': {'q0'}, 'ϵ': {'q1'}},
        'q1': {'b': {'q1'}, 'ϵ': {'q2'}},
        'q2': {'a': {'q2'}}
    },
    'inicial': 'q0',
    'finais': {'q2'}
}


ex2_afn = afe_afn(ex2_afn_epsilon)
# Imprime o AFN resultante
imprimir_automato(ex2_afn_epsilon)
imprimir_automato(ex2_afn)
graficos(ex2_afn_epsilon, 'ex2_afn_epsilon')
graficos(ex2_afn, 'ex2_afn')
"""



 # EXEMPLO 3
ex3_afn_epsilon = {
    'estados': {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'qf'},
    'alfabeto': {'a', 'b', 'c'},
    'transicoes': {
        'q0': {'a': {'q0'}, 'b': {'q0'}, 'c': {'q0'}, 'ϵ': {'q1', 'q2', 'q4'}},
        'q1': {'a': {'qf'}},
        'q2': {'b': {'q3'}},
        'q3': {'b': {'qf'}},
        'q4': {'c': {'q5'}},
        'q5': {'c': {'q6'}},
        'q6': {'c': {'qf'}},
        'qf': {'ϵ': ''},
    },
    'inicial': 'q0',
    'finais': {'qf'}
}


ex3_afn = afe_afn(ex3_afn_epsilon)
# Imprime o AFN resultante
imprimir_automato(ex3_afn_epsilon)
imprimir_automato(ex3_afn)
graficos(ex3_afn_epsilon, 'ex3_afn_epsilon')
graficos(ex3_afn, 'ex3_afn')
