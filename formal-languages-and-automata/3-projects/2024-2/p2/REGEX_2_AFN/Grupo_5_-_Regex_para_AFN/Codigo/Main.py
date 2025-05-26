from itertools import count

class AFN:
    # Classe que representa um Autômato Finito Não Determinístico (AFN).
    def __init__(self, estado_inicial: str, estado_final: str, transicao: dict):
        self.estado_inicial = estado_inicial  # Estado inicial do AFN.
        self.estado_final = estado_final      # Estado final do AFN.
        self.transicao = transicao           # Dicionário de transições (formato: {estado: {símbolo: {destinos}}}).

def regex_para_afn(regex: str) -> AFN:
    # Gera IDs únicos para estados
    id_generator = count(1)

    def prox_estado_id() -> str: 
        return f'S{next(id_generator)}'  # Retorna um novo ID de estado.

    def adicionar_transicao(transicoes, origem, simbolo, destinos):
        # Adiciona uma transição ao dicionário de transições.
        if origem not in transicoes:
            transicoes[origem] = {}
        if simbolo not in transicoes[origem]:
            transicoes[origem][simbolo] = set()
        transicoes[origem][simbolo].update(destinos)  # Usa conjunto para evitar duplicatas.

    def criar_afn_para_simbolo(simbolo: str) -> AFN:
        # Cria um AFN básico para um único símbolo.
        estado_inicial = prox_estado_id()
        estado_final = prox_estado_id()
        transicao = {}
        adicionar_transicao(transicao, estado_inicial, simbolo, {estado_final})
        return AFN(estado_inicial, estado_final, transicao)

    def concatenar_afn(afn1: AFN, afn2: AFN) -> AFN:
        # Concatena dois AFNs adicionando uma transição ε do estado final de afn1 para o inicial de afn2.
        adicionar_transicao(afn1.transicao, afn1.estado_final, 'ε', {afn2.estado_inicial})
        return AFN(afn1.estado_inicial, afn2.estado_final, {**afn1.transicao, **afn2.transicao})

    def uniao_afn(afn1: AFN, afn2: AFN) -> AFN:
        # Cria um novo AFN que representa a união (|) de dois AFNs.
        estado_inicial = prox_estado_id()
        estado_final = prox_estado_id()
        transicao = {estado_inicial: {'ε': {afn1.estado_inicial, afn2.estado_inicial}},
                     afn1.estado_final: {'ε': {estado_final}},
                     afn2.estado_final: {'ε': {estado_final}},
                     **afn1.transicao, **afn2.transicao}
        return AFN(estado_inicial, estado_final, transicao)

    def asterisco_afn(afn: AFN) -> AFN:
        # Cria um novo AFN que representa a operação de fecho de Kleene (*) sobre um AFN.
        estado_inicial = prox_estado_id()
        estado_final = prox_estado_id()
        transicao = {estado_inicial: {'ε': {afn.estado_inicial, estado_final}},
                     afn.estado_final: {'ε': {afn.estado_inicial, estado_final}},
                     **afn.transicao}
        return AFN(estado_inicial, estado_final, transicao)

    def aplicar_operador(operadores, operandos):
        # Aplica o operador do topo da pilha de operadores aos operandos apropriados.
        operador = operadores.pop()
        if operador == '.':
            operandos.append(concatenar_afn(operandos.pop(-2), operandos.pop()))
        elif operador == '|':
            operandos.append(uniao_afn(operandos.pop(-2), operandos.pop()))
        elif operador == '*':
            operandos.append(asterisco_afn(operandos.pop()))

    operadores, operandos = [], []
    prioridade = {'*': 3, '.': 2, '|': 1}  # Define a precedência dos operadores.

    # Itera sobre a expressão regular para construir o AFN.
    for char in regex: 
        if char.isalnum():  # Se for um símbolo, cria um AFN básico.
            operandos.append(criar_afn_para_simbolo(char))
        elif char in {'*', '|', '.'}:  # Operadores da regex.
            # Aplica operadores de maior ou igual precedência no topo da pilha.
            while operadores and operadores[-1] != '(' and prioridade[operadores[-1]] >= prioridade[char]:
                aplicar_operador(operadores, operandos)
            operadores.append(char)
        elif char == '(':
            operadores.append(char)  # Abre um grupo.
        elif char == ')':
            # Fecha um grupo e aplica operadores dentro do parêntese.
            while operadores[-1] != '(':
                aplicar_operador(operadores, operandos)
            operadores.pop()  # Remove o '(' da pilha.

    # Aplica operadores restantes.
    while operadores: 
        aplicar_operador(operadores, operandos) 
    
    return operandos[0]  # Retorna o AFN final.

def formatar_transicoes(transicoes: dict) -> str:
    # Formata as transições do AFN para exibição.
    return "\n".join(f"{origem} --{simbolo}--> {', '.join(destinos)}" 
                     for origem, destinos_simbolo in transicoes.items() 
                     for simbolo, destinos in destinos_simbolo.items())

# Entrada do usuário para a expressão regular.
regex = input("Digite a expressão regular: ")
afn = regex_para_afn(regex)

# Exibe os detalhes do AFN gerado.
print("AFN:")
print(f"Estado Inicial: {afn.estado_inicial}")
print(f"Estado Final: {afn.estado_final}")
print("Transições:")
print(formatar_transicoes(afn.transicao))
