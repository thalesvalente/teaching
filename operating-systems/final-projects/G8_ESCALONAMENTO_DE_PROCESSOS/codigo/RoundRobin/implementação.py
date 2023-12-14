class RoundRobinScheduler:
    def __init__(self, quantum_time): #funcão inicializadora da classe, recebe o quantum e cria 2 listas.
        self.quantum_time = quantum_time
        self.process_queue = [] #copia da lista 
        self.original_queue = [] 

     
    def add_process(self, process, process_time): #Adiciona os processos na lista, para serem executados 
        self.process_queue.append((process, process_time))
        self.original_queue.append((process, process_time))

    
    def run_scheduler(self): #função de Escalonamento dos processos .
        tempo_atual = 0 
        lista_de_tempos = []

        while self.process_queue:
            
            # Retira o primeiro elemento da lista, para a interação 

            current_process, tempo_processamento = self.process_queue.pop(0)

            tempo_execucao = min(tempo_processamento, self.quantum_time)

            print(f"Processo {current_process} foi executado por {tempo_execucao} unit time.")

            tempo_atual += tempo_execucao

            tempo_processamento -= tempo_execucao
            
            # verifica se a tarefa ainda possui tempo de processamento, caso tenha, ela sera adicionada novamente na lista com o tempo de processamento atualizado.
            if tempo_processamento > 0:
                self.process_queue.append((current_process, tempo_processamento))
            else:
                print(f"\nProcesso {current_process} concluído. terminou no tempo : {tempo_atual}\n")
                lista_de_tempos.append(tempo_atual)

            if (len(self.process_queue)) == 0:
                print("\nprocessos finalizados")
                resultado = sum(lista_de_tempos)/(len(self.original_queue))
                print(f"\ntempo de turnround medio  = {resultado}")
                                                                  


