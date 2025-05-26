class Automaton:
    def __init__(self, num_states):
        # Inicializa os estados de transição e os estados de aceitação
        self.transitions = [{} for _ in range(num_states)]
        self.accept_states = [False] * num_states

    def addTransition(self, from_state, char, to_state):
        # Adiciona uma transição de um estado para outro dado um caractere
        self.transitions[from_state][char] = to_state

    def setAcceptState(self, state):
        # Marca um estado como estado de aceitação
        self.accept_states[state] = True

    def isAccepted(self, input_string):
        # Verifica se uma string de entrada é aceita pelo autômato
        current_state = 0
        try:
            for symbol in input_string:
                current_state = self.transitions[current_state][symbol]
            return self.accept_states[current_state]
        except KeyError:
            # Retorna falso se uma transição não é encontrada
            return False


def automato():
    # Cria um autômato para identificar datas
    automato = Automaton(13)

    # Configura as transições para formar datas válidas
    for i in range(0, 10):
        i_string = str(i)
        automato.addTransition(1, i_string, 3)  # Dias 01-09
        automato.addTransition(5, i_string, 7)  # Meses 01-09
        automato.addTransition(8, i_string, 9)  # Ano milhar 1
        automato.addTransition(9, i_string, 10) # Ano milhar 2
        automato.addTransition(10, i_string, 11) # Ano dezena 1
        automato.addTransition(11, i_string, 12) # Ano dezena 2
        if (i <= 2):
            automato.addTransition(0, i_string, 1) # Dias 10-29
            automato.addTransition(6, i_string, 7) # Meses 10-12
        if (i<=1):
            automato.addTransition(2, i_string, 3) # Dias 30-31
    automato.addTransition(0, '3', 2) # Dias 30-31
    automato.addTransition(4, '0', 5) # Meses 10-12
    automato.addTransition(4,'1', 6)  # Meses 10-12
    automato.addTransition(3, '/', 4) # Divisão entre dia e mês
    automato.addTransition(7, '/', 8) # Divisão entre mês e ano
    automato.setAcceptState(12) # Define o último estado como estado de aceitação
    return automato

automaton1 = automato() 

# Abre o arquivo e lê seu conteúdo
with open(r'C:\Users\thale\Documents\teste.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()  # Separa o conteúdo do arquivo em palavras
    for palavra in palavras:
        if (automaton1.isAccepted(palavra)):  # Verifica se a palavra é uma data válida
            print(palavra)
