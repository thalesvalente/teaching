# Universidade Federal do Maranhão
# Author: Prof. Thales Levi Azevedo Valente
# Description: Mini Sistema Operacional
# Date: 16-08-2023


# Perfeito! Vamos continuar com os próximos componentes:

# PROGRAMAS SIMULADOS
# Para fins de simulação, um "programa" pode ser uma função simples que realiza alguma tarefa. Vou adicionar dois programas simulados:

# Calc: um programa que realiza uma operação aritmética simples.
# Echo: um programa que simplesmente retorna uma mensagem dada.

class SimpleOSSimulated_v2:

    # .............. 2) Mais Programas Simulados ..............
    # Executa o programa passado por argumento
    def execute_program(self, program_name, *args):
        # Verifica qual programa deve ser executado
        if program_name == "calc":
            # Executa o programa 'calc'
            return self.program_calc(*args)
        elif program_name == "echo":
            # Executa o programa 'echo'
            return self.program_echo(*args)
        else:
            # Caso contrário, exibe uma mensagem de erro
            return f"Programa '{program_name}' não reconhecido."
    
    # Programa calculadora simples
    def program_calc(self, operation, *args):
        # Verifica qual operação deve ser executada
        if operation == "add":
            # Se a operação for de soma, soma todos os argumentos
            return sum(args)
        elif operation == "sub":
            # Se a operação for de subtração, subtrai o primeiro argumento da soma dos demais
            return args[0] - sum(args[1:])
        else:
            # Caso contrário, exibe uma mensagem de erro
            return f"Operação '{operation}' não reconhecida."

    def program_echo(self, message):
        return message
    
    # ... Restante do código anterior ...

# Executando programas simulados
simple_os_v2 = SimpleOSSimulated_v2()

# Testando os programas simulaexitdos
calc_result = simple_os_v2.execute_program("calc", "add", 5, 3, 2)
echo_result = simple_os_v2.execute_program("echo", "Hello, SimpleOS!")

print("Resultado do Programa 1: " + str(calc_result))
print("Resultado do Programa 2: " + echo_result)