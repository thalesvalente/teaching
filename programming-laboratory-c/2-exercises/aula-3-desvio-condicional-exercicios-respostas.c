// Universidade Federal do Maranhão
// Departamento de Engenharia da Computação
// Author: Professor Doutor Thales Levi Azevedo Valente
// Description: Atividades - Laboratório de Programação - Linguagem C
// Date: 08-10-2023

/*
Neste material de nível 2, você será desafiado a resolver problemas mais complexos relacionados à engenharia da computação e elétrica, usando desvios condicionais em C. O objetivo é aplicar e consolidar o conhecimento adquirido sobre o tópico.

Vamos começar!

Estrutura:
1) Atividade 1: Sistema de Monitoramento de Tensão 
2) Atividade 2: Cálculo de Potência 
3) Atividade 3: Conversão de Bases Numéricas
4) Atividade 4: Lei de Ohm 
5) Atividade 5: Simulador de Espectro de Frequência
6) Atividade 6: Cálculo da Saída de um Neurônio Simples
7) Atividade 7: Identificação de Circuitos Lógicos
8) Atividade 8: Normalização de Dados 
9) Atividade 9: Catálogo de Componentes Eletrônicos
10) Atividade 10: Classificação Binária Simples 
*/

#include <stdio.h>
#include <math.h> // para a função pow()

int main() {
    
    // Variáveis
    double tensao, base, expoente, corrente, resistencia, potencia, tensaoOhm;

    // ##################################################################
    // 1) Atividade 1: Sistema de Monitoramento de Tensão
    // ==================================================================
    printf("\n1) Atividade 1: Sistema de Monitoramento de Tensão\n");
    printf("---------------------------------------------------\n");
    printf("Insira a tensão (em volts): ");
    scanf("%lf", &tensao);
    
    if (tensao < 1) {
        printf("Alerta: Tensão Baixa!\n");
    } else if (tensao >= 1 && tensao <= 3) {
        printf("Tensão Média.\n");
    } else {
        printf("Alerta: Tensão Alta!\n");
    }

    // ##################################################################
    // 2) Atividade 2: Cálculo de Potência
    // ==================================================================
    printf("\n2) Atividade 2: Cálculo de Potência\n");
    printf("---------------------------------------------------\n");
    printf("Insira a base: ");
    scanf("%lf", &base);
    printf("Insira o expoente: ");
    scanf("%lf", &expoente);
    
    potencia = pow(base, expoente);
    printf("Potência: %.2lf\n", potencia);

    // ##################################################################
    // 3) Atividade 3: Conversão Simplificada de Bases Numéricas
    // ==================================================================
    printf("\n3) Atividade 3: Conversão Simplificada de Bases Numéricas\n");
    printf("---------------------------------------------------\n");
    int numero;
    printf("Insira um número decimal de 0 a 7: ");
    scanf("%d", &numero);
    
    switch(numero) {
        case 0: printf("Binário: 000\n"); break;
        case 1: printf("Binário: 001\n"); break;
        case 2: printf("Binário: 010\n"); break;
        case 3: printf("Binário: 011\n"); break;
        case 4: printf("Binário: 100\n"); break;
        case 5: printf("Binário: 101\n"); break;
        case 6: printf("Binário: 110\n"); break;
        case 7: printf("Binário: 111\n"); break;
        default: printf("Número inválido.\n");
    }

    // ##################################################################
    // 4) Atividade 4: Lei de Ohm
    // ==================================================================
    printf("\n4) Atividade 4: Lei de Ohm\n");
    printf("---------------------------------------------------\n");
    printf("Insira a corrente (I): ");
    scanf("%lf", &corrente);
    printf("Insira a resistência (R): ");
    scanf("%lf", &resistencia);
    
    tensaoOhm = corrente * resistencia;
    printf("Tensão (V): %.2lfV\n", tensaoOhm);

    // Variáveis
    double frequencia, entrada, peso, bias, saida;
    int codigoCircuito;

    // ##################################################################
    // 5) Atividade 5: Simulador de Espectro de Frequência
    // ==================================================================
    printf("\n5) Atividade 5: Simulador de Espectro de Frequência\n");
    printf("---------------------------------------------------\n");
    printf("Insira a frequência (em GHz): ");
    scanf("%lf", &frequencia);
    
    if (frequencia < 1) {
        printf("Frequência de rádio.\n");
    } else if (frequencia >= 1 && frequencia <= 100) {
        printf("Frequência de micro-ondas.\n");
    } else {
        printf("Frequência de terahertz.\n");
    }

    // ##################################################################
    // 6) Atividade 6: Cálculo da Saída de um Neurônio Simples
    // ==================================================================
    printf("\n6) Atividade 6: Cálculo da Saída de um Neurônio Simples\n");
    printf("---------------------------------------------------\n");
    printf("Insira a entrada do neurônio: ");
    scanf("%lf", &entrada);
    printf("Insira o peso do neurônio: ");
    scanf("%lf", &peso);
    printf("Insira o bias do neurônio: ");
    scanf("%lf", &bias);
    
    saida = entrada * peso + bias;
    printf("Saída do neurônio: %.2lf\n", saida);

    // ##################################################################
    // 7) Atividade 7: Identificação de Circuitos Lógicos
    // ==================================================================
    printf("\n7) Atividade 7: Identificação de Circuitos Lógicos\n");
    printf("---------------------------------------------------\n");
    printf("Insira um número correspondente ao circuito lógico (1-AND, 2-OR, 3-NOT): ");
    scanf("%d", &codigoCircuito);
    
    switch(codigoCircuito) {
        case 1: 
            printf("Circuito AND: Este circuito retorna 1 se ambas as entradas forem 1, caso contrário, retorna 0.\n");
            break;
        case 2:
            printf("Circuito OR: Este circuito retorna 1 se pelo menos uma das entradas for 1, caso contrário, retorna 0.\n");
            break;
        case 3:
            printf("Circuito NOT: Este circuito inverte a entrada, retornando 0 se a entrada for 1 e 1 se a entrada for 0.\n");
            break;
        default: 
            printf("Código inválido.\n");
    }

    // Variáveis
    double x, min, max, x_norm, limiar, entrada;
    int codigoComponente;

    // ##################################################################
    // 8) Atividade 8: Normalização de Dados
    // ==================================================================
    printf("\n8) Atividade 8: Normalização de Dados\n");
    printf("---------------------------------------------------\n");
    printf("Insira o valor de x: ");
    scanf("%lf", &x);
    printf("Insira o valor mínimo: ");
    scanf("%lf", &min);
    printf("Insira o valor máximo: ");
    scanf("%lf", &max);
    
    x_norm = (x - min) / (max - min);
    printf("Valor normalizado: %.2lf\n", x_norm);

    // ##################################################################
    // 9) Atividade 9: Catálogo de Componentes Eletrônicos
    // ==================================================================
    printf("\n9) Atividade 9: Catálogo de Componentes Eletrônicos\n");
    printf("---------------------------------------------------\n");
    printf("Insira um código numérico para o componente: ");
    scanf("%d", &codigoComponente);
    
    switch(codigoComponente) {
        case 1: 
            printf("Componente: Resistor\n");
            break;
        case 2:
            printf("Componente: Capacitor\n");
            break;
        case 3:
            printf("Componente: Diodo\n");
            break;
        // ... pode adicionar mais componentes conforme necessário
        default: 
            printf("Código inválido.\n");
    }

    // ##################################################################
    // 10) Atividade 10: Classificação Binária Simples 
    // ==================================================================
    printf("\n10) Atividade 10: Classificação Binária Simples\n");
    printf("---------------------------------------------------\n");
    printf("Insira um valor de entrada: ");
    scanf("%lf", &entrada);
    printf("Insira um limiar: ");
    scanf("%lf", &limiar);
    
    if (entrada > limiar) {
        printf("Classe A\n");
    } else {
        printf("Classe B\n");
    }

    return 0;

    return 0;
}
