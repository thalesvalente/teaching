import heapq
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class TuringMachine:
    def __init__(self, states, tape, transitions, start_state, accept_states):
        self.states = states
        self.tape = list(tape) + ['_']  # Garante um espaço extra na fita
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
        self.head = 0  # Posição inicial do cabeçote
        self.history = []  # Armazena os passos para animação
    
    def run(self):
        """ Executa a Máquina de Turing usando Dijkstra e armazena os passos para animação. """
        priority_queue = [(0, self.start_state, self.head, list(self.tape), [])]
        visited = {}
        
        while priority_queue:
            cost, state, head, tape, path = heapq.heappop(priority_queue)
            
            if (state, head) in visited and visited[(state, head)] <= cost:
                continue
            visited[(state, head)] = cost
            
            self.history.append((state, head, tape[:], path, cost))  # Salva o estado atual para animação
            
            if state in self.accept_states:
                return ''.join(tape), path, cost
            
            current_symbol = tape[head] if 0 <= head < len(tape) else '_'
            
            if (state, current_symbol) in self.transitions:
                best_transition = min(self.transitions[(state, current_symbol)], key=lambda x: x[3])
                next_state, write_symbol, move, weight = best_transition
                
                new_tape = tape[:]
                new_tape[head] = write_symbol
                new_head = head + (1 if move == 'R' else -1)
                
                if new_head < 0:
                    new_tape.insert(0, '_')
                    new_head = 0
                elif new_head >= len(new_tape):
                    new_tape.append('_')
                
                heapq.heappush(priority_queue, (cost + weight, next_state, new_head, new_tape, path + [(state, next_state, weight)]))
        
        return None

def draw_graph(transitions, history, save_gif=False):
    """ Gera uma animação interativa do grafo da Máquina de Turing. """
    G = nx.DiGraph()
    
    for (state, symbol), transitions_list in transitions.items():
        for next_state, write_symbol, move, weight in transitions_list:
            G.add_edge(state, next_state, label=f'{symbol}/{write_symbol}, {move}, {weight}')
    
    pos = nx.spring_layout(G)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    def update(frame):
        ax.clear()
        state, head, tape, path, cost = history[frame]
        
        # Desenha os nós e arestas
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, font_size=10, ax=ax)
        
        # Destaca a transição atual
        if path:
            last_edge = path[-1]
            nx.draw_networkx_edges(G, pos, edgelist=[(last_edge[0], last_edge[1])], width=2.5, edge_color='red', ax=ax)
        
        labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=6, ax=ax)
        
        # Exibir a fita e estado atual
        ax.set_title(f"Passo {frame+1}: Estado = {state}, Cabeça = {head}, Custo = {cost}\nFita: {''.join(tape)}")
        print(state)

    ani = animation.FuncAnimation(fig, update, frames=len(history), interval=1000, repeat=False)
    if save_gif:
        ani.save("turing_machine.gif", writer="pillow", fps=1)  # Salva como GIF
    plt.show()

# Definição dos estados e transições
states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q_accept'}
tape = ['0', '0', '1', '1', '0']

transitions = {
    ('q0', '0'): [('q1', '0', 'R', 1), ('q2', '1', 'R', 2)],  # Escolha entre q1 e q2
    ('q1', '0'): [('q2', '1', 'R', 3), ('q3', '0', 'L', 9)],  # Escolha entre q2 e q3
    ('q2', '1'): [('q3', '0', 'R', 6), ('q2', '0', 'R', 7)],
    ('q3', '1'): [('q4', '1', 'R', 1), ('q2', '1', 'L', 5)],  # Retorno ao q2 ou avanço para q4
    ('q4', '0'): [('q_accept', '_', 'R', 6)]
}

start_state = 'q0'
accept_states = {'q_accept'}

# Criando e executando a Máquina de Turing
machine = TuringMachine(states, tape, transitions, start_state, accept_states)
result = machine.run()

# Exibindo os resultados finais
if result:
    print("Fita final:", result[0])
    print("Caminho percorrido:", result[1])
    print("Soma ponderada:", result[2])
    #print()
else:
    print("Rejeitado")

# Gerando a animação do grafo
draw_graph(transitions, machine.history, save_gif=True)
