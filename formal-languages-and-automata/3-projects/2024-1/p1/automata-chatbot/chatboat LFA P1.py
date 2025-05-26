class Chatbot:
    def __init__(self):
        # Define o estado inicial do chatbot como 'inicio'
        self.estado = 'inicio'
        # Define um dicionário com os estados e as mensagens correspondentes
        self.estados_mensagens = {
            'inicio': "Olá! Em que posso te ajudar hoje?",
            'descrever_problema': "Por favor, descreva qual é o problema que você está enfrentando.",
            'pedido_informacao': "Em que mais posso te ajudar?",
            'informacao_adicional': "Por favor, forneça mais detalhes sobre o que você precisa.",
            'solucao': "Vou tentar te ajudar a resolver isso. Já tentou reiniciar o dispositivo?",
            'encerramento': "Obrigado por utilizar o nosso serviço. Até logo!"
        }
        # Mostra a mensagem do estado inicial
        print("Estado atual:", self.estado)
        print(self.estados_mensagens[self.estado])

    def responder(self, entrada):
        if self.estado == 'inicio':
            if entrada.lower() == 'problema':
                self.estado = 'descrever_problema'
            elif entrada.lower() == 'informacao':
                self.estado = 'pedido_informacao'
            elif entrada.lower() == 'sair':
                self.estado = 'encerramento'
            else:
                return "Desculpe, não entendi. Poderia repetir?"

        elif self.estado == 'descrever_problema':
            self.estado = 'solucao'

        elif self.estado == 'pedido_informacao':
            self.estado = 'informacao_adicional'

        elif self.estado == 'informacao_adicional':
            self.estado = 'encerramento'

        elif self.estado == 'solucao':
            if entrada.lower() == 'sim':
                self.estado = 'encerramento'
            elif entrada.lower() == 'nao':
                self.estado = 'encerramento'
            else:
                return "Desculpe, não entendi. Por favor, responda com 'sim' ou 'não'."

        # Retorna a resposta padrão do estado
        return self.estados_mensagens[self.estado]

def main():
    # Cria uma instância do Chatbot
    chatbot = Chatbot()
    while chatbot.estado != 'encerramento':
        entrada_usuario = input("Usuário: ")
        resposta = chatbot.responder(entrada_usuario)
        # Imprime o estado atual e a resposta do chatbot
        print("Estado atual:", chatbot.estado)
        print("Chatbot:", resposta)

if __name__ == "__main__":
    main()
