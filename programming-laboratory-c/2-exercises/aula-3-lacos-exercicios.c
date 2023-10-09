// Universidade Federal do Maranhão
// Departamento de Engenharia da Computação
// Author: Professor Doutor Thales Levi Azevedo Valente
// Description: Atividades - Laboratório de Programação - Linguagem C
// Date: 08-10-2023

/*
Neste material, você será desafiado a resolver problemas que envolvem a aplicação de laços de repetição na linguagem de programação C. A compreensão e aplicação eficaz dos laços é fundamental para resolver problemas que exigem repetições de operações, seja para processamento de dados, simulações ou controle de sistemas.

Estrutura:
1) Atividade 1: Monitoramento Contínuo de Tensão
2) Atividade 2: Análise de Frequências em um Espectro
3) Atividade 3: Simulação simplificadade um Osciloscópio
4) Atividade 4: Medição Iterativa de Resistência em um Circuito
5) Atividade 5: Monitoramento de Faixas de Frequência
6) Atividade 6: Treinamento Iterativo de um Neurônio Artificial
7) Atividade 7: Análise de Sequências Lógicas
8) Atividade 8: Processamento Iterativo de Sinais
9) Atividade 9: Catalogação Automatizada de Componentes
10) Atividade 10: Classificação Iterativa de Dados

Vamos começar!
*/

#include <stdio.h>

int main() {

    // ##################################################################
    // 1) Atividade 1: Monitoramento Contínuo de Tensão 
    // ==================================================================
    printf("\n1) Atividade 1: Monitoramento Contínuo de Tensão\n");
    printf("---------------------------------------------------\n");

    // Contexto: Em sistemas eletrônicos, o monitoramento contínuo da tensão é fundamental para garantir a segurança e a eficiência do equipamento. Por exemplo, baterias de dispositivos móveis, quando sobrecarregadas, podem sofrer danos ou até mesmo explodir.

    // Desafio:
    // Implemente um sistema que lê continuamente a tensão (em volts) de um dispositivo. O sistema deve executar em um laço 'while' e monitorar a tensão até que o usuário decida parar a leitura (por exemplo, pressionando a tecla 'q'). Em cada leitura, o sistema deve classificar a tensão como:
    // - Baixa (menor que 3.5V)
    // - Média (entre 3.5V e 4.2V)
    // - Alta (maior que 4.2V)
    // Em caso de tensão alta, um alerta deve ser exibido para o usuário.

    // TO-DO: Use um laço 'while' e instruções condicionais para implementar o sistema descrito acima.


    // ##################################################################
    // 2) Atividade 2: Análise de Frequências em um Espectro 
    // ==================================================================
    printf("\n2) Atividade 2: Análise de Frequências em um Espectro\n");
    printf("---------------------------------------------------\n");

    // Contexto: Em telecomunicações, o espectro de frequência é dividido em várias faixas, cada uma com propriedades e aplicações específicas. O conhecimento dessas faixas é essencial para engenheiros e técnicos para evitar interferências e garantir uma comunicação eficiente.

    // Desafio:
    // Suponha que você tenha um espectro de frequência que varia de 0Hz a 100GHz. Você precisa analisar esse espectro em incrementos de 10GHz e determinar a aplicação típica associada a cada faixa.

    // As faixas de frequência e suas aplicações típicas são:
    // - 0-10GHz: Comunicação móvel
    // - 10-20GHz: Satélite
    // - 20-30GHz: Radar
    // - 30-40GHz: Comunicação por fibra ótica
    // - 40-50GHz: Wi-Fi
    // - 50-60GHz: Radiodifusão
    // - 60-70GHz: Pesquisa astronômica
    // - 70-80GHz: Medicina e imagiologia
    // - 80-90GHz: Comunicações militares
    // - 90-100GHz: Pesquisa científica

    // TO-DO: 
    // Utilize um laço 'for' para iterar sobre o espectro de frequência em incrementos de 10GHz. Para cada faixa:
    // - Identifique a aplicação ou sinal mais provável com base nas faixas fornecidas acima.
    // - Imprima a faixa de frequência e sua aplicação/sinal associado.


    // ##################################################################
    // 3) Atividade 3: Simulação Simplificada de um Osciloscópio 
    // ==================================================================
    printf("\n3) Atividade 3: Simulação Simplificada de um Osciloscópio\n");
    printf("---------------------------------------------------\n");

    // Contexto: Um osciloscópio é uma ferramenta essencial em laboratórios de eletrônica. Ele é utilizado para visualizar sinais elétricos. Em sua forma mais básica, quando um sinal de alta frequência é detectado, ele exibe uma onda senoidal no visor, enquanto um sinal de baixa frequência pode parecer mais uma linha reta.

    // Desafio:
    // Você não precisa simular um osciloscópio completo, mas sim criar uma representação simplificada.
    
    // TO-DO: 
    // - Solicite ao usuário que insira uma "frequência" (pode ser simplesmente um número entre 1 e 10).
    // - Se a frequência for 5 ou menos, imprima uma linha reta, representada por "-------".
    // - Se a frequência for maior que 5, imprima uma onda senoidal simplificada, representada por "/\\/\\/".


    // ##################################################################
    // 4) Atividade 4: Medição Iterativa de Resistência em um Circuito 
    // ==================================================================
    printf("\n4) Atividade 4: Medição Iterativa de Resistência em um Circuito\n");
    printf("---------------------------------------------------\n");

    // Contexto: Em laboratórios de eletrônica e em processos de manutenção, é comum medir a resistência de componentes ou de partes de um circuito várias vezes para garantir precisão e verificar a estabilidade do componente ou circuito.

    // Desafio:
    // Suponha que você esteja trabalhando com um multímetro digital e deseja medir a resistência de um resistor em diferentes momentos para verificar sua estabilidade.

    // TO-DO:
    // - Utilize um laço 'for' para simular 5 medições de resistência.
    // - Em cada iteração, solicite ao usuário que insira o valor medido (em Ohms).
    // - Calcule e imprima a média dos valores medidos após todas as iterações.
    // - Caso a variação entre as medições exceda um limite pré-definido (por exemplo, 5% do valor médio), alerte o usuário sobre a possível instabilidade do resistor.

    // ##################################################################
    // 5) Atividade 5: Monitoramento de Faixas de Frequência 
    // ==================================================================
    printf("\n5) Atividade 5: Monitoramento de Faixas de Frequência\n");
    printf("---------------------------------------------------\n");

    // Contexto: Em sistemas de comunicação, é crucial monitorar as faixas de frequência para evitar interferências e garantir a qualidade da transmissão. Cada serviço, como rádio FM, Wi-Fi, etc., opera em uma faixa de frequência específica.

    // Desafio:
    // Implemente um programa que monitore continuamente as faixas de frequência, identificando a qual serviço cada uma pertence ou indicando se a frequência inserida não corresponde a nenhum serviço conhecido.
    
    // TO-DO: 
    // - Solicite ao usuário que insira uma frequência (em MHz).
    // - Classifique a frequência inserida em uma das seguintes categorias: Rádio FM (88-108 MHz), Wi-Fi (2400-2500 MHz), GPS (1575.42 MHz).
    // - Se a frequência não se encaixar em nenhuma das categorias, informe ao usuário que a frequência não corresponde a nenhum serviço conhecido.
    // - Use um laço para permitir múltiplas entradas sem reiniciar o programa.
    
    // Dica: Utilize um laço "while" para manter o programa em execução e estruturas "if-else" para classificar as faixas de frequência e lidar com entradas que não correspondem a nenhum serviço.


    // ##################################################################
    // 6) Atividade 6: Treinamento Iterativo de um Neurônio Artificial 
    // ==================================================================
    printf("\n6) Atividade 6: Treinamento Iterativo de um Neurônio Artificial\n");
    printf("---------------------------------------------------\n");

    // Contexto: Em aprendizado de máquina, os neurônios artificiais são ajustados iterativamente para melhorar seu desempenho em tarefas específicas. O processo de ajustar o peso de um neurônio com base em um erro é chamado de treinamento.

    // Desafio:
    // Simule um treinamento básico de um neurônio. Para cada iteração, ajuste o peso do neurônio com base em um valor de erro fornecido.
    
    // TO-DO: 
    // - Inicie o neurônio com um peso aleatório entre 0 e 1.
    // - Em cada iteração, solicite ao usuário um valor de erro (por exemplo, um número entre -1 e 1).
    // - Ajuste o peso do neurônio subtraindo o valor do erro.
    // - Continue o treinamento até que o usuário decida parar, inserindo um valor específico, como -999.

    // Dica: Use um laço "do-while" para continuar o treinamento até que a condição de parada seja atendida. Ajuste o peso usando operações aritméticas simples.


        // ##################################################################
    // 7) Atividade 7: Análise de Valores Lógicos Consecutivos 
    // ==================================================================
    printf("\n7) Atividade 7: Análise de Valores Lógicos Consecutivos\n");
    printf("---------------------------------------------------\n");

    // Contexto: Em sistemas digitais, frequentemente trabalhamos com valores lógicos (0 ou 1). Esses valores são fundamentais na lógica de programação e no funcionamento de circuitos eletrônicos.

    // Desafio:
    // Implemente um programa que leia três valores lógicos consecutivos e determine se todos são iguais ou se há um valor diferente.

    // TO-DO: 
    // - Solicite ao usuário que insira três valores lógicos consecutivos (um de cada vez).
    // - Analise os valores e determine se todos são '0', todos são '1', ou há uma mistura de '0's e '1's.
    // - Informe ao usuário o resultado da análise.
    
    // Dica: Use estruturas "if-else" para comparar os valores lógicos e determinar a categoria apropriada.

    // ##################################################################
    // 8) Atividade 8: Processamento Iterativo de Sinais 
    // ==================================================================
    printf("\n8) Atividade 8: Processamento Iterativo de Sinais\n");
    printf("---------------------------------------------------\n");

    // Contexto: O processamento de sinais é crucial em sistemas de comunicação. Em muitas situações, precisamos calcular a média de várias leituras para obter um valor representativo ou para filtrar ruído.

    // Desafio:
    // Implemente um programa que leia uma quantidade específica de valores representando leituras de sinal e calcule a média.

    // TO-DO: 
    // - Solicite ao usuário quantas leituras de sinal ele deseja fazer (por exemplo, 5 leituras).
    // - Use um laço para solicitar e acumular cada leitura.
    // - Calcule e exiba a média dos valores inseridos.
    
    // Dica: Use um laço "for" ou "while" para iterar pela quantidade desejada de leituras e acumule a soma dos valores para, em seguida, calcular a média.


        // ##################################################################
    // 9) Atividade 9: Catalogação Automatizada de Componentes
    // ==================================================================
    printf("\n9) Atividade 9: Catalogação Automatizada de Componentes\n");
    printf("---------------------------------------------------\n");

    // Contexto: Em laboratórios e oficinas eletrônicas, os componentes são geralmente identificados por códigos numéricos.

    // Desafio:
    // Implemente um programa que associe códigos numéricos a seus respectivos componentes eletrônicos.
    
    // Classificações:
    // 1 - Resistor
    // 2 - Capacitor
    // 3 - Indutor
    // 4 - Transistor
    // 5 - Diodo

    // TO-DO:
    // - Solicite ao usuário que insira um código numérico (de 1 a 5).
    // - Use desvios condicionais para determinar qual componente corresponde ao código inserido.
    // - Exiba o nome do componente correspondente.
    // - Caso o usuário insira um código fora do intervalo de 1 a 5, informe-o de que o código é inválido.
    
    // Dica: Use estruturas "if-else" ou "switch-case" para mapear códigos a seus respectivos componentes.

    // ##################################################################
    // 10) Atividade 10: Classificação Iterativa de Dados
    // ==================================================================
    printf("\n10) Atividade 10: Classificação Iterativa de Dados\n");
    printf("---------------------------------------------------\n");

    // Contexto: Em processamento de sinais ou análise de dados, frequentemente é necessário categorizar diferentes magnitudes ou intensidades.

    // Desafio:
    // Implemente um programa que leia uma série de valores e classifique cada valor em "Baixo", "Médio" ou "Alto".

    // Classificações:
    // - Baixo: 0 a 3.99
    // - Médio: 4 a 6.99
    // - Alto: 7 a 10

    // TO-DO:
    // - Solicite ao usuário quantos valores ele deseja classificar.
    // - Use um laço para solicitar e classificar cada valor.
    // - Para cada valor inserido, classifique-o conforme as faixas acima e exiba sua categoria.
    // - Se o valor inserido estiver fora do intervalo de 0 a 10, informe o usuário de que o valor é inválido.
    
    // Dica: Use um laço "for" ou "while" para iterar pela quantidade desejada de valores. Em cada iteração, use estruturas "if-else" para determinar e exibir a categoria do valor.


    return 0;
}
