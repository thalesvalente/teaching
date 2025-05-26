import re

class Reconhecor_valores:
    def __init__(self):
        # Definindo os estados do autômato
        self.estados = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6']
        # Definindo as transições entre os estados
        self.transicoes = {
            'q0': {'digit': 'q1', '.': 'q6'},
            'q1': {'digit': 'q1', '.': 'q2', ',': 'q4'},
            'q2': {'digit': 'q3'},
            'q3': {'digit': 'q3', ',': 'q4'},
            'q4': {'digit': 'q5'},
            'q5': {'digit': 'q5'},
            'q6': {'digit': 'q3'}
        }
        # Estado inicial do autômato
        self.estado_inicial = 'q0'
        # Estados de aceitação, onde reconhecemos que encontramos um valor válido
        self.estado_aceito = ['q5']
        # Estado atual do autômato
        self.estado_atual = self.estado_inicial
        # Valor encontrado durante o reconhecimento
        self.valor = ''

    def reset(self):
        # Reinicia o autômato para o estado inicial
        self.estado_atual = self.estado_inicial
        self.valor = ''

    def reconhecedor(self, text):
        # Função para reconhecer um valor monetário em um texto
        self.reset()
        for char in text:
            if char.isdigit():
                char_type = 'digit'
            elif char in ['.', ',']:
                char_type = char
            else:
                char_type = None

            if char_type:
                # Se o caractere for um dígito, ponto ou vírgula
                if char_type in self.transicoes[self.estado_atual]:
                    # Se houver uma transição definida para o caractere no estado atual
                    self.estado_atual = self.transicoes[self.estado_atual][char_type]
                    if char_type in ['.']:
                        self.valor += ''
                    elif char_type in [',']:
                        self.valor += '.'
                    else:
                        self.valor += char
                else:
                    # Se não houver transição definida para o caractere no estado atual
                    if self.estado_atual in self.estado_aceito:
                        return True, float(self.valor)
                    else:
                        return False, None
            else:
                # Se o caractere não for um dígito, ponto ou vírgula
                if self.estado_atual in self.estado_aceito:
                    return True, float(self.valor)
                else:
                    return False, None

        if self.estado_atual in self.estado_aceito:
            # Se o estado atual for um estado de aceitação
            return True, float(self.valor)
        else:
            # Se não for possível reconhecer um valor monetário
            return False, None

# Teste
texto = """
Extrato de Conta Corrente
Lançamentos
Dia Histórico Valor
0,00 (+)27/01/2023Saldo Anterior
30,00 (+)08/02/2023Transferido da poupança
7,00 (-)08/02/2023Pix - Enviado
3,99 (-)08/02/2023Pix - Enviado
14,60 (-)08/02/2023Tarifa Pacote de Serviços
1.520,00 (+)13/02/2023Pix - Recebido
14,00 (-)13/02/2023Pix - Enviado
1.500,00 (-)13/02/2023Pix - Enviado
1.602,00 (+)16/02/2023Ordem Banc 12 Sec Tes Nac
250,00 (-)22/02/2023Pix - Enviado
327,00 (-)23/02/2023Pix - Enviado
32,20 (-)27/02/2023Pix - Enviado
10,00 (-)27/02/2023Pix - Enviado
101,14 (-)27/02/2023Net Serviços de Comunicaç
892,07 (+)28/02/2023S A L D O
Total Aplicações Financeiras152,00asd
* Saldos por dia Base
"""

reconhecor_valores = Reconhecor_valores()
# Usando expressão regular para encontrar possíveis valores monetários no texto
ocorrencias = re.findall("[0-9]{0,3}[.]{0,1}[0-9]{0,3}[,][0-9]{2}", texto)
print(ocorrencias)
for item in ocorrencias:
    # Para cada correspondência encontrada, tentamos reconhecer como um valor monetário usando o autômato
    reconhecidos, valor = reconhecor_valores.reconhecedor(item)
    if reconhecidos:
        print("Valor reconhecido:", valor)
    else:
        print("Valor não reconhecido:", item)

