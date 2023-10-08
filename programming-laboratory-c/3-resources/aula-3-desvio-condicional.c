// Universidade Federal do Maranhão
// Departamento de Engenharia da Computação
// Author: Professor Doutor Thales Levi Azevedo Valente
// Description: Material de Ensino - Laboratório de Programação - Linguagem C
// Date: 08-10-2023

/*
Neste material, exploraremos o conceito dos desvios condicionais na linguagem de programação C. 
Os desvios condicionais são estruturas de controle que permitem bifurcar a execução do código com base em condições específicas.

A capacidade de um programa decidir qual bloco de instruções executar com base nas condições atuais é fundamental para implementar lógicas de decisão.

Os principais tópicos abordados são:
1) Desvio Condicional 'if'
2) 'if' aninhados
3) 'switch-case'

Cada tópico será ilustrado com exemplos práticos relacionados à engenharia da computação e elétrica.
*/

#include <stdio.h>

int main() {
    // ##################################################################
    // 1- Desvio Condicional 'if'
    // ==================================================================
    // O comando 'if' avalia uma expressão. Se essa expressão for verdadeira, o bloco de código associado é executado (o bloco imeidiamente posterior)
    printf("\n1- Desvio Condicional 'if'\n");
    printf("---------------------------------------------------\n");

    // Contexto: Em circuitos eletrônicos, é comum verificar o nível de tensão de um sinal.
    float tensao = 3.3; // Tensão em volts
    if (tensao > 2.5) {
        printf("O sinal elétrico está em alta tensão (%.2fV)\n", tensao);
    } else {
        printf("O sinal elétrico está em baixa tensão (%.2fV)\n", tensao);
    }

    // ##################################################################
    // 2- 'if' aninhados
    // ==================================================================
    // 'if' aninhados permitem combinar múltiplas condições e tomar decisões mais complexas.
    printf("\n2- 'if' aninhados\n");
    printf("---------------------------------------------------\n");

    // Contexto: Diferentes microcontroladores operam em diferentes frequências, o que pode afetar o desempenho e a aplicação.
    float frequencia = 1.5; // Frequência em GHz

    if (frequencia < 1.0) {
        printf("O microcontrolador opera em baixa frequência.\n");
    } else if (frequencia >= 1.0 && frequencia <= 2.0) {
        printf("O microcontrolador opera em média frequência.\n");
    } else {
        printf("O microcontrolador opera em alta frequência.\n");
    }

    // ##################################################################
    // 3- 'switch-case'
    // ==================================================================
    // A estrutura 'switch-case' permite avaliar uma variável ou expressão e, com base no seu valor, escolher um bloco de código a ser executado.
    printf("\n3- 'switch-case'\n");
    printf("---------------------------------------------------\n");

    // Contexto: Em design de circuitos, os componentes são muitas vezes identificados por códigos numéricos.
    int codigoComponente = 2;

    switch (codigoComponente) {
        case 1:
            printf("O componente é um Resistor.\n");
            break;
        case 2:
            printf("O componente é um Capacitor.\n");
            break;
        case 3:
            printf("O componente é um Indutor.\n");
            break;
        default:
            printf("Componente desconhecido.\n");
            break;
    }

    return 0;
}