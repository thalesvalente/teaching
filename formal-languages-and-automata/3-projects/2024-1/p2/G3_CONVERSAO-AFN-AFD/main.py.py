import graphviz

class Automaton:
    def __init__(self, num_states, accepting_states):
        # Inicializa o autômato com um determinado número de estados e um conjunto de estados de aceitação
        self.num_states = num_states
        self.transitions = [{} for _ in range(num_states)]
        self.accepting_states = accepting_states

    def add_transition(self, start_state, characters, end_state):
        # Adiciona uma transição do start_state para o end_state usando um ou mais caracteres
        if isinstance(characters, tuple):
            for character in characters:
                if character not in self.transitions[start_state]:
                    self.transitions[start_state][character] = set()
                self.transitions[start_state][character].add(end_state)
        else:
            if characters not in self.transitions[start_state]:
                self.transitions[start_state][characters] = set()
            self.transitions[start_state][characters].add(end_state)

    def epsilon_closure(self, states):
        # Calcula o fechamento epsilon para um conjunto de estados
        stack = list(states)
        closure = set(states)
        
        while stack:
            state = stack.pop()
            if '' in self.transitions[state]:  # Assuming '' is used for epsilon transitions
                for next_state in self.transitions[state]['']:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
        
        return closure

    def convert_to_dfa(self):
        # Converte o AFN atual em um AFD
        initial_state = frozenset(self.epsilon_closure({0})) # Estado inicial do AFD é o fechamento epsilon do estado inicial do AFN
        dfa_states = {initial_state: 0}  # Mapeia estados do AFD para seus identificadores
        dfa_accepting_states = set()  # Conjunto de estados de aceitação do AFD
        dfa_transitions = [{}]  # Lista de transições do AFD
        new_states = [initial_state]  # Lista de novos estados a serem processados
        state_counter = 1  # Contador para atribuir identificadores únicos aos estados do AFD

        while new_states:
            current = new_states.pop()  # Pega um novo estado para processar
            current_state_id = dfa_states[current]  # Obtém o identificador do estado atual

            if any(state in self.accepting_states for state in current):
                dfa_accepting_states.add(current_state_id)  # Adiciona ao conjunto de estados de aceitação se qualquer estado do AFN for de aceitação

            all_symbols = set()
            for state in current:
                all_symbols.update(self.transitions[state].keys())  # Coleta todos os símbolos possíveis de transição

            all_symbols.discard('')  # Remove o símbolo epsilon

            # Ordena os símbolos para garantir uma ordem  determinística
            for symbol in sorted(all_symbols):
                next_state = set()
                for sub_state in current:
                    if symbol in self.transitions[sub_state]:
                        next_state.update(self.transitions[sub_state][symbol])  # Coleta todos os estados alcançáveis com o símbolo atual

                next_state_closure = frozenset(self.epsilon_closure(next_state))  # Calcula o fechamento epsilon do próximo estado

                if next_state_closure not in dfa_states:
                    dfa_states[next_state_closure] = state_counter  # Atribui um novo identificador se o estado ainda não foi mapeado
                    new_states.append(next_state_closure)  # Adiciona o novo estado para processamento futuro
                    dfa_transitions.append({})  # Expande a lista de transições para incluir o novo estado
                    state_counter += 1

                dfa_transitions[current_state_id][symbol] = dfa_states[next_state_closure]  # Adiciona a transição ao AFD

        dfa = Automaton(len(dfa_states), dfa_accepting_states)  # Cria o AFD resultante
        dfa.transitions = dfa_transitions  # Define as transições do AFD
        return dfa

    def plot_automaton(self, filename='automaton'):
        dot = graphviz.Digraph()

        for i in range(self.num_states):
            if i in self.accepting_states:
                dot.node(str(i), shape='doublecircle')
            else:
                dot.node(str(i), shape='circle')

        for start_state, transitions in enumerate(self.transitions):
            for symbol, end_states in transitions.items():
                if not isinstance(end_states, set):
                    end_states = {end_states}  # Transforma em um conjunto se não for
                for end_state in end_states:
                    dot.edge(str(start_state), str(end_state), label=symbol if symbol else 'ε')

        dot.render(filename, format='png', cleanup=True)
        print(f"Automaton graph saved as {filename}.png")


# Exemplo de uso:
def create_automaton1():
    afn = Automaton(4, {3})
    afn.add_transition(0, 'a', 1)
    afn.add_transition(0, ('a', 'b'), 0)
    afn.add_transition(1, 'a', 2)
    afn.add_transition(2, 'a', 3)
    return afn

def create_automaton2():
    afn = Automaton(5, {4})
    afn.add_transition(0, '1', 1)
    afn.add_transition(0, ('1', '0'), 0)
    afn.add_transition(1, '0', 2)
    afn.add_transition(2, '1', 3)
    afn.add_transition(3, '0', 4)
    return afn

def create_automaton3():
    afn = Automaton(4, {3})
    afn.add_transition(0, '1', 1)
    afn.add_transition(0, ('1', '0'), 0)
    afn.add_transition(1, '0', 2)
    afn.add_transition(1, '', 2)
    afn.add_transition(2, '1', 3)
    afn.add_transition(3, ('1', '0'), 3)
    return afn

# Imprimir os AFDs resultantes
afn1 = create_automaton1()
afn1.plot_automaton('AFN_1')
afd1 = afn1.convert_to_dfa()
afd1.plot_automaton('AFD_1')

afn2 = create_automaton2()
afn2.plot_automaton('AFN_2')
afd2 = afn2.convert_to_dfa()
afd2.plot_automaton('AFD_2')

afn3 = create_automaton3()
afn3.plot_automaton('AFN_3')
afd3 = afn3.convert_to_dfa()
afd3.plot_automaton('AFD_3')






