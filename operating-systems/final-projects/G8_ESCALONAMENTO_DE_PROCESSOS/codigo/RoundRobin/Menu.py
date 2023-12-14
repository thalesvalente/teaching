import implementação

def menu():
    executando = True
    print("\nDigite um número correspondente a ação:")
    print("\n1 - Adicionar processos \n | 2 - ver lista de processos \n | 3 - executar processos \n | 4 - Encerra Programa")
    resposta = int(input("---> "))

    while executando:
        if(resposta == 1):
            x = int(input("digite quantos procesos deseja adicionar: "))
            while x > 0:
                nome = str(input("Digite o nome do processo : "))
                time = str(input("Digite o tempo de processamento: "))
                processo = scheduler.add_process( nome, int(time))
                x = x - 1
            menu()
        if(resposta == 2):
          print("lista de processos:")
          for process, process_time in scheduler.original_queue:
              print(f"processo: {process}, tempo de processamento:{process_time}")
          menu()
        if(resposta == 3):
            if(len(scheduler.process_queue)) == 0:
                print('Não á processos na fila')
                menu()
            else:
                scheduler.run_scheduler()
                menu()

        if(resposta == 4):
            executando = False

            print("Programa finalizado")
        
        else:
            print("opção invalida")
            menu()


quantum_time = int(input("defina um valor inteiro para o quantum: "))

scheduler = implementação.RoundRobinScheduler(quantum_time) # instancia classe do escalonador 
