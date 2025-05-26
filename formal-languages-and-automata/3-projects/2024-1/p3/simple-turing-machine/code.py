def grafo():
        from graphviz import Digraph
        # Grafo estático da Maquina de Turing. Apenas será gerado se as condições forem atendidas.
        afe = Digraph('L={anbn∣n≥0', filename='turing', format='png')
        afe.attr(rankdir='LR', size='10,7')

        # Estados
        afe.attr('node', shape='doublecircle')
        afe.node('qf')
        afe.attr('node', shape='circle')
        afe.node('q0')
        afe.node('q1')
        afe.node('q2')
        afe.node('q3')

        # Transições
        afe.edge('q0', 'q0', label='*, *, D')
        afe.edge('q0', 'q1', label='a, A, D')
        afe.edge('q0', 'q3', label='B, B, D')
        afe.edge('q0', 'qf', label='_, _, D')
        afe.edge('q1', 'q1', label='a, a, D')
        afe.edge('q1', 'q1', label='B, B, D')
        afe.edge('q1', 'q2', label='b, B, E')
        afe.edge('q2', 'q2', label='a, a, E')
        afe.edge('q2', 'q2', label='B, B, E')
        afe.edge('q2', 'q0', label='A, A, D')
        afe.edge('q3', 'q3', label='B, B, D')
        afe.edge('q3', 'qf', label='_, _, D')
        
        afe.view()


class MaquinaTuring:
    def __init__(self, fita, espaco_vazio, estado_incial, estados_finais, transicoes):
        self.fita = list(fita)  # Inicializa a fita como uma lista de caracteres
        self.espaco_vazio = espaco_vazio  # Símbolo usado para representar espaços em branco na fita
        self.posicao_cabeca = 0  # Posição inicial da cabeça de leitura/escrita
        self.estado = estado_incial  # Estado inicial da máquina
        self.estados_finais = estados_finais  # Conjunto de estados de aceitação
        self.transicoes = transicoes  # Função de transição (dicionário)
        self.movimentos = [(self.estado, ''.join(self.fita), self.posicao_cabeca)]  # Lista para armazenar os passos para animação

    def movimento(self):
        simbolo_atual = self.fita[self.posicao_cabeca]  # Obtém o símbolo atual sob a cabeça de leitura/escrita
        # Verifica se há uma transição definida para o par (estado atual, símbolo atual)
        if (self.estado, simbolo_atual) in self.transicoes:
            # Obtém o próximo estado, símbolo a ser escrito e direção do movimento da cabeça
            proximo_estado, proximo_simbolo, direcao = self.transicoes[(self.estado, simbolo_atual)]
            self.fita[self.posicao_cabeca] = proximo_simbolo  # Escreve o novo símbolo na fita
            # Move a cabeça de leitura/escrita para a direita ou esquerda
            self.posicao_cabeca += 1 if direcao == 'D' else -1
            self.estado = proximo_estado  # Atualiza o estado atual
            # Adiciona o passo atual à lista de passos para animação
            self.movimentos.append((self.estado, ''.join(self.fita), self.posicao_cabeca))
        else:
            # Lança uma exceção se não houver uma transição definida para o par (estado atual, símbolo atual)
            raise Exception("Nenhuma transição encontrada para o estado {} com o símbolo {}".format(self.estado, simbolo_atual))

    def run(self):
        # Executa a máquina até que ela alcance um estado de aceitação
        while self.estado not in self.estados_finais:
            self.movimento()  # Executa um passo da máquina
        return ''.join(self.fita), self.estado  # Retorna o estado final da fita e o estado final da máquina

    def animacao(self):
        import time
        import os
        os.system('cls') # limpa o terminal para cada nova leitura
        # Anima a execução da máquina imprimindo os passos com um atraso de 1 segundo
        
        for movimento in self.movimentos:
            estado, fita, posicao_cabeca = movimento
            print(f"Fita: {fita}, Posição: {posicao_cabeca}, Estado: {estado}, Simbolo: {fita[posicao_cabeca]}")
            time.sleep(1) # atraso de 1 segundo
            os.system('cls') # limpa o terminal para cada nova leitura




# Função de transição: define as regras de transição da máquina
transicoes = {
    ('q0', '*'): ('q0', '*', 'D'),  # No estado q0 e ler '*', escreva '*', vá para q1 e mova a cabeça para a direita
    ('q0', 'a'): ('q1', 'A', 'D'),  # No estado q0 e ler 'a', escreva 'A', vá para q1 e mova a cabeça para a direita
    ('q0', 'B'): ('q3', 'B', 'D'),  # No estado q0 e ler 'B', escreva 'B', vá para q3 e mova a cabeça para a direita
    ('q0', '_'): ('qf', '_', 'D'),  # No estado q0 e ler '_', escreva '_', vá para qf (estado de aceitação)
    ('q1', 'a'): ('q1', 'a', 'D'),  # No estado q1 e ler 'a', escreva 'a', continue em q1 e mova a cabeça para a direita
    ('q1', 'B'): ('q1', 'B', 'D'),  # No estado q1 e ler 'B', escreva 'B', continue em q1 e mova a cabeça para a direita
    ('q1', 'b'): ('q2', 'B', 'E'),  # No estado q1 e ler 'b', escreva 'B', vá para q2 e mova a cabeça para a esquerda
    ('q2', 'a'): ('q2', 'a', 'E'),  # No estado q2 e ler 'a', escreva 'a', continue em q2 e mova a cabeça para a esquerda
    ('q2', 'A'): ('q0', 'A', 'D'),  # No estado q2 e ler 'A', escreva 'A', vá para q0 e mova a cabeça para a direita
    ('q2', 'B'): ('q2', 'B', 'E'),  # No estado q2 e ler 'B', escreva 'B', continue em q2 e mova a cabeça para a esquerda
    ('q3', 'B'): ('q3', 'B', 'D'),  # No estado q3 e ler 'B', escreva 'B', continue em q3 e mova a cabeça para a direita
    ('q3', '_'): ('qf', '_', 'D')  # No estado q3 e ler '_', escreva '_', vá para qf (estado de aceitação) e mova a cabeça para a direita
}

# Inicializando a máquina de Turing
fita = "*aabb__" # A fita inicial com a palavra a ser processada. São dois espaços finais para visualização da animação!!!
espaco_vazio = '_'  # Símbolo em branco
estado_incial = 'q0'  # Estado inicial
estados_finais = {'qf'}  # Conjunto de estados de aceitação

# Cria uma instância da máquina de Turing
teste = MaquinaTuring(fita, espaco_vazio, estado_incial, estados_finais, transicoes)
resultado_fita, estado_final = teste.run()  # Executa a máquina

if teste:
    teste.animacao()  # Anima a execução da máquina
    grafo()
    print("Resultado final da fita:", resultado_fita)  # Imprime o estado final da fita
    print("Estado final:", estado_final)  # Imprime o estado final da máquina
