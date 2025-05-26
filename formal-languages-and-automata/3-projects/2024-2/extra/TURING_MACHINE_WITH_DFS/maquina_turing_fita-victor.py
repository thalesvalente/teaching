from collections import deque

class TuringMachine:
    def __init__(self, tape, initial_state):
        self.tape = list(tape)  # Converte a string da fita em uma lista mutável
        self.head_position = 0  # Posição inicial da cabeça de leitura/escrita
        self.current_state = initial_state  # Estado inicial da máquina

        # Dicionário de transições: (estado_atual, símbolo_lido) -> {(novo_estado, símbolo_escrito, direção)}
        self.states = {
            ('q0', '0'): {('q1', '0', 'D')},
            ('q1', 'a'): {('q2', 'X', 'D')},
            ('q1', 'b'): {('q3', 'X', 'D')},
            ('q1', 't'): {('qf', 't', 'E')},
            ('q2', 'a'): {('q2', 'a', 'D'), ('q4', 'Y', 'E')},
            ('q2', 'b'): {('q2', 'b', 'D')},
            ('q3', 'a'): {('q3', 'a', 'D')},
            ('q3', 'b'): {('q3', 'b', 'D'), ('q4', 'Y', 'E')},
            ('q4', 'a'): {('q4', 'a', 'E')},
            ('q4', 'b'): {('q4', 'b', 'E')},
            ('q4', 'X'): {('q5', 'X', 'D')},
            ('q5', 'a'): {('q6', 'X', 'D')},
            ('q5', 'b'): {('q8', 'X', 'D')},
            ('q5', 'Y'): {('q11', 'Y', 'D')},
            ('q6', 'a'): {('q6', 'a', 'D')},
            ('q6', 'b'): {('q6', 'b', 'D')},
            ('q6', 'Y'): {('q7', 'Y', 'D')},
            ('q7', 'Y'): {('q7', 'Y', 'D')},
            ('q7', 'a'): {('q10', 'Y', 'E')},
            ('q8', 'a'): {('q8', 'a', 'D')},
            ('q8', 'b'): {('q8', 'b', 'D')},
            ('q8', 'Y'): {('q9', 'Y', 'D')},
            ('q9', 'Y'): {('q9', 'Y', 'D')},
            ('q9', 'b'): {('q10', 'Y', 'E')},
            ('q10', 'a'): {('q10', 'a', 'E')},
            ('q10', 'b'): {('q10', 'b', 'E')},
            ('q10', 'Y'): {('q10', 'Y', 'E')},
            ('q10', 'X'): {('q5', 'X', 'D')},
            ('q11', 'Y'): {('q11', 'Y', 'D')},
            ('q11', 't'): {('qf', 't', 'E')}
        }
        self.final_states = ['qf']  # Estados de aceitação

    def possible_actions(self, tape, head, state):
        """Retorna todas as transições possíveis para (state, simbolo_lido)."""
        if head < 0 or head >= len(tape):
            return set()  # Cabeça fora dos limites da fita
        symbol = tape[head]
        return self.states.get((state, symbol), set())

    def run_dfs(self):
        """Executa a máquina de Turing usando uma pilha (DFS) para explorar caminhos."""
        stack = []  # Pilha para explorar estados em profundidade
        visited = set()  # Conjunto de configurações visitadas
        initial_config = (tuple(self.tape), self.head_position, self.current_state, [self.current_state])
        stack.append(initial_config)
        visited.add(initial_config[:3])

        while stack:
            current_tape, current_head, current_state, path = stack.pop()
            print("Current state:", current_state)
            print("Tape:", ''.join(current_tape))
            print("Head position:", current_head)
            print("Path so far:", " -> ".join(path))
            print("-------------------------")

            if current_state in self.final_states:
                print("Machine halts at final state:", current_state)
                print("Final tape configuration:", ''.join(current_tape))
                return

            actions = self.possible_actions(current_tape, current_head, current_state)
            if not actions:
                continue

            for new_state, new_char, direction in actions:
                new_tape_list = list(current_tape)
                new_tape_list[current_head] = new_char
                new_head = current_head + 1 if direction == 'D' else current_head - 1
                if 0 <= new_head < len(new_tape_list):
                    new_config = (tuple(new_tape_list), new_head, new_state, path + [new_state])
                    if new_config[:3] not in visited:
                        visited.add(new_config[:3])
                        stack.append(new_config)

        print("Nenhum estado final foi alcançado.")

# Exemplo de uso:
tm = TuringMachine("0ababt", 'q0')
tm.run_dfs()
