class TuringMachine:
    def __init__(self, logic):
        self.transitions = {}  # Dicionário para armazenar as transições da máquina de Turing
        self.parse_logic(logic)  # Chama o método para analisar a lógica fornecida

    def parse_logic(self, logic):
        """
        Analisa a lógica fornecida e preenche o dicionário de transições.
        Cada linha da lógica deve conter: estado_atual, símbolo_atual, novo_símbolo, direção, novo_estado.
        """
        for line in logic.strip().split('\n'):
            line = line.strip()
            if not line or line.startswith(';'):
                continue  # Ignora linhas vazias ou comentários

            parts = line.split()
            if len(parts) < 5:
                continue  # Ignora linhas que não têm os 5 componentes necessários

            current_state = parts[0]
            current_symbol = parts[1]
            new_symbol = parts[2]
            direction = parts[3]
            new_state = parts[4]

            # Adiciona a transição ao dicionário
            self.transitions[(current_state, current_symbol)] = (new_symbol, direction, new_state)

    def run(self, input_tape, show_steps=False):
        """
        Executa a máquina de Turing na fita de entrada fornecida.
        Se show_steps for True, exibe cada passo da execução.
        """
        tape = list(input_tape)  # Converte a fita de entrada em uma lista de caracteres
        head_position = 0  # Posição inicial da cabeça de leitura/escrita
        state = '0'  # Estado inicial
        step_count = 0  # Contador de passos

        # Verifica se há um '*' na fita para determinar a posição inicial da cabeça
        if '*' in tape:
            head_position = tape.index('*')
            tape.pop(head_position)  # Remove o '*' da fita

        if show_steps:
            print("Iniciando a execução da Máquina de Turing...")
            print("Fita inicial: " + "".join(tape))
            print("Estado inicial: 0")
            print("Posição da cabeça: " + str(head_position))
            print("-" * 30)

        while not state.startswith('halt'):
            step_count += 1
            if step_count > 1000:  # Limite de segurança para evitar loops infinitos
                state = 'halt-error-potential-infinite-loop'
                if show_steps:
                    print("Limite de passos atingido (1000). Interrompendo devido a potencial loop infinito.")
                break

            # Obtém o símbolo atual sob a cabeça
            current_symbol = tape[head_position] if 0 <= head_position < len(tape) else '_'

            transition = None
            transition_rule = None  # Armazena a regra de transição para exibição

            # Tenta encontrar uma correspondência exata para a transição
            if (state, current_symbol) in self.transitions:
                transition = self.transitions[(state, current_symbol)]
                transition_rule = f"({state}, {current_symbol}) -> ({transition[0]}, {transition[1]}, {transition[2]})"
            # Tenta correspondência com curinga para o símbolo
            elif (state, '*') in self.transitions:
                transition = self.transitions[(state, '*')]
                transition_rule = f"({state}, *) -> ({transition[0]}, {transition[1]}, {transition[2]})"

            if transition:
                new_symbol, direction, new_state = transition

                if new_symbol != '*':
                    if 0 <= head_position < len(tape):
                        tape[head_position] = new_symbol  # Escreve o novo símbolo na fita
                    elif head_position < 0:  # Expansão para a esquerda, insere no início
                        tape.insert(0, new_symbol)
                        head_position = 0  # A cabeça permanece no início após a inserção
                    else:  # Expansão para a direita, adiciona ao final
                        tape.append(new_symbol)

                # Move a cabeça de acordo com a direção especificada
                if direction == 'l':
                    head_position -= 1
                elif direction == 'r':
                    head_position += 1
                elif direction == '*':
                    pass  # Sem movimento

                # Atualiza o estado
                state = new_state if new_state != '*' else state

                if show_steps:
                    # Exibe o estado atual da fita com a posição da cabeça marcada
                    tape_display = list(tape)
                    tape_display_str_parts = []
                    for i, symbol in enumerate(tape_display):
                        if i == head_position:
                            tape_display_str_parts.append(f"[{symbol}]")  # Marca a posição da cabeça com colchetes
                        else:
                            tape_display_str_parts.append(symbol)
                    tape_display_str = "".join(tape_display_str_parts)

                    print(f"Passo: {step_count}")
                    print(f"Estado: {state}")
                    print(f"Fita: {tape_display_str}")
                    print(f"Posição da cabeça: {head_position}")
                    print(f"Símbolo atual: {current_symbol if current_symbol != '_' else '_'}")
                    print(f"Transição: {transition_rule}")
                    print("-" * 30)

            else:
                state = 'halt-error-no-transition'
                if show_steps:
                    print(f"Passo: {step_count}")
                    print(f"Estado: {state}")
                    print(f"Fita: {''.join(tape)}")
                    print(f"Posição da cabeça: {head_position}")
                    print(f"Símbolo atual: {current_symbol if current_symbol != '_' else '_'}")
                    print("Nenhuma transição encontrada para o estado e símbolo atuais. Interrompendo.")
                    print("-" * 30)
                break

            # Lida com os limites da fita, adicionando espaços em branco conforme necessário
            if head_position < 0:
                tape.insert(0, '_')
                head_position = 0
            elif head_position >= len(tape):
                tape.append('_')

        # Remove espaços em branco iniciais e finais da fita de saída
        while tape and tape[0] == '_':
            tape.pop(0)
        while tape and tape[-1] == '_':
            tape.pop()

        if show_steps:
            if state.startswith('halt') and not state.startswith('halt-error'):
                print("Máquina de Turing interrompida com sucesso!")
            elif state.startswith('halt-error'):
                print(f"Máquina de Turing interrompida com estado de erro: {state}")
            print("Fita final: " + "".join(tape))
            print("-" * 30)

        return "".join(tape)

tm_logic = """
; Multiplication of two binary numbers, in tuple syntax.
; Example input: 11S10
; Symbol '_' is used for blank, 'S' is used instead of '*' as a literal separator.

; -- start state: start
0 0 0 l init       ; [0,1]: {L: init}
0 1 1 l init

; -- init
init _ + r right       ; ' ' => '_'; {write: '+', R: right}

; -- right
right 0 0 r right      ; [0,1,'*']: R  => substituí '*' por 'S'
right 1 1 r right
right S S r right
right _ _ l readB      ; ' ' => '_'; {L: readB}

; -- readB
readB 0 _ l doubleL    ; 0: {write: ' ', L: doubleL} => '_' no lugar de espaço
readB 1 _ l addA       ; 1: {write: ' ', L: addA}

; -- addA
addA 0 0 l addA        ; [0,1]: L => permanece em addA
addA 1 1 l addA
addA S S l read        ; '*': {L: read} => substituído '*' por 'S'

; -- doubleL
doubleL 0 0 l doubleL  ; [0,1]: L => continua em doubleL
doubleL 1 1 l doubleL
doubleL S 0 r shift    ; '*': {write: 0, R: shift} => substituí '*' por 'S'

; -- double
double 0 0 r double    ; [0,1,+]: R => permanece em double
double 1 1 r double
double + + r double
double S 0 r shift     ; '*': {write: 0, R: shift} => substituí '*' por 'S'

; -- shift
shift 0 S r shift0     ; 0: {write: '*', R: shift0} => substituí '*' por 'S'
shift 1 S r shift1     ; 1: {write: '*', R: shift1}
shift _ _ l tidy       ; ' ': {L: tidy} => '_' para branco

; -- shift0
shift0 0 0 r shift0    ; 0: {R: shift0}
shift0 1 0 r shift1    ; 1: {write: 0, R: shift1}
shift0 _ 0 r right     ; ' ' => '_'; {write: 0, R: right}

; -- shift1
shift1 0 1 r shift0    ; 0: {write: 1, R: shift0}
shift1 1 1 r shift1    ; 1: {R: shift1}
shift1 _ 1 r right     ; ' ' => '_'; {write: 1, R: right}

; -- tidy
tidy 0 _ l tidy        ; [0,1]: {write: ' ', L} => '_' para branco, permanece em tidy
tidy 1 _ l tidy
tidy + _ l halt-done   ; +: {write: ' ', L: done} => renomeei done para halt-done

; -- (done) => trocado para 'halt-done' para encerrar a máquina

; -- read
read 0 c l have0       ; 0: {write: c, L: have0}
read 1 c l have1       ; 1: {write: c, L: have1}
read + + l rewrite     ; +: {L: rewrite} (mantém '+')

; -- have0
have0 0 0 l have0      ; [0,1]: L => fica em have0
have0 1 1 l have0
have0 + + l add0       ; +: {L: add0}

; -- have1
have1 0 0 l have1
have1 1 1 l have1
have1 + + l add1

; -- add0
add0 0 O r back0       ; [0,' ']: {write: O, R: back0} => substitui ' ' por '_'
add0 _ O r back0
add0 1 I r back0       ; 1 => {write: I, R: back0}
add0 O O l add0        ; [O,I]: L => permanece
add0 I I l add0

; -- add1
add1 0 I r back1       ; [0,' ']: {write: I, R: back1}
add1 _ I r back1
add1 1 O l carry       ; 1 => {write: O, L: carry}
add1 O O l add1        ; [O,I] => L => continua
add1 I I l add1

; -- carry
carry 0 1 r back1      ; [0,' ']: {write: 1, R: back1}
carry _ 1 r back1
carry 1 0 l carry      ; 1 => {write: 0, L} => permanece em carry

; -- back0
back0 0 0 r back0      ; [0,1,O,I,+]: R => continua
back0 1 1 r back0
back0 O O r back0
back0 I I r back0
back0 + + r back0
back0 c 0 l read       ; c => {write: 0, L: read}

; -- back1
back1 0 0 r back1
back1 1 1 r back1
back1 O O r back1
back1 I I r back1
back1 + + r back1
back1 c 1 l read       ; c => {write: 1, L: read}

; -- rewrite
rewrite O 0 l rewrite  ; O => {write: 0, L}
rewrite I 1 l rewrite  ; I => {write: 1, L}
rewrite 0 0 l rewrite  ; 0 => {write: 0, L}
rewrite 1 1 l rewrite  ; 1 => {write: 1, L}
rewrite _ _ r double   ; ' ' => '_' => {R: double}

"""

tm = TuringMachine(tm_logic)
#Mostrar os passos da maquina
show_steps = True 

# Exemplo:
input1 = "10"
input2 = "11"
input_tape = list(input1 + "S" + input2 + "_")
result_tape = tm.run(input_tape, show_steps)

print(f"Entrada 1: {input1}")
print(f"Entrada 2: {input2}")
print(f"Fita de Resultado: {result_tape}")

# Verificar resultado:
num1 = int(input1, 2)
num2 = int(input2, 2)
expected_product_bin = bin(num1 * num2)[2:]
print(f"Produto Binário Esperado: {expected_product_bin}")
print(f"Resultado Correto: {result_tape == expected_product_bin}")