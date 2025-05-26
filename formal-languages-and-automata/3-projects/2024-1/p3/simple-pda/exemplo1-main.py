from graphviz import Digraph
def grafo():
    # Grafo estático do automato com pilha. Apenas será gerado se as condições forem atendidas.
    afe = Digraph('L={anbn∣n≥0', filename='aut_pilha_ex1', format='png')
    afe.attr(rankdir='LR', size='10,7')

    # Estados
    afe.attr('node', shape='doublecircle')
    afe.node('qf')
    afe.attr('node', shape='circle')
    afe.node('q0')
    afe.node('q1')

    # Transições
    afe.edge('q0', 'q0', label='a, ϵ, A')
    afe.edge('q0', 'q1', label='b, A, ϵ')
    afe.edge('q0', 'qf', label='?, ?, ϵ')
    afe.edge('q1', 'q1', label='b, A, ϵ')
    afe.edge('q1', 'qf', label='?, ?, ϵ')
    
    afe.view()
    
    
class PDA:
    def __init__(self):
        self.pilha = ['?']  # Inicializa a pilha com o símbolo inicial '?'
        self.estado = 'q0'  # Estado inicial
        self.transicoes = {
            ('q0', 'a', '?'): ('q0', 'A?'),
            ('q0', 'a', 'A'): ('q0', 'AA'),
            ('q0', 'b', 'A'): ('q1', ''),
            ('q0', '', '?'): ('qf', '?'),
            ('q1', 'b', 'A'): ('q1', ''),
            ('q1', '', '?'): ('qf', '?')
        }
    # Faz a conferência de aceitação.
    def verificação_final(self, palavra):
        for char in palavra:
            if not self.teste_caractere(char):
                return False
        return self.estado == 'qf' and self.pilha == ['?']

    
    def teste_caractere(self, char):
        if (self.estado, char, self.pilha[-1]) in self.transicoes: # Faz o alinhamento do estado atual, caractere lido e último item da pilha para verificar junto as transições se aquele passo é válido.
            novo_estado, pilha_item = self.transicoes[(self.estado, char, self.pilha[-1])] # Retorna novo estado e novo item a ser adiconado na pilha
            self.estado = novo_estado # Atualizado o estado atual
            self.pilha.pop() # Retira último item da pilha
            if pilha_item:
                self.pilha.extend(pilha_item[::-1]) # Empilha os símbolos (reverso)
            return True
        return False
    
    #Retorno da utilização da classe
    def __str__(self):
        return f"Estado: {self.estado}, Pilha: {self.pilha}"

# Função para testar o PDA com animação simples de leitura
import time
import os

# Função para testar o PDA com animação simples.
def test_pda(pda, palavra):
    count_a = 0 # conta número de a's da palavra
    count_b = 0 # conta número de b's da palavra
    teste = 1 # Recebe a verificação do teste de caractere
    for char in palavra:
        os.system('cls') # limpa o terminal para cada nova leitura
        if char == 'a':
            count_a += 1
        if char == 'b':
            count_b += 1
        print(f"Processando entrada: {palavra}")
        print(pda)
        print(f"Lendo: {char}")
        teste = pda.teste_caractere(char)
        time.sleep(1) # Pausa para visualização

    # Checagem final com a transição vazia
    os.system('cls') # limpa o terminal para cada nova leitura
    print(pda)
    pda.teste_caractere('')
    print("Lendo: epsilon")
    time.sleep(1) # Pausa para visualização
    
    # Resultado da verificação
    result = pda.verificação_final('') # Verificação de classe
    if teste == False: # Verificação de passo
        result = False
    if count_a != count_b: # Verificação de palavra
        result = False
    print(f"Final estado: {pda.estado}, Pilha: {pda.pilha}")
    print("Aceito" if result else "Rejeitado")
    if result == True:
        grafo()

# Exemplo de uso
palavra = "ab"
pda = PDA()
test_pda(pda, palavra)


