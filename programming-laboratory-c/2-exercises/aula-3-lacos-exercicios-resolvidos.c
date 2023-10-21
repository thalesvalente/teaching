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
#include <stdlib.h>
#include <time.h>

int main() {

    // ##################################################################
    // 1) Atividade 1: Monitoramento Contínuo de Tensão 
    // ==================================================================
    printf("\n1) Atividade 1: Monitoramento Contínuo de Tensão\n");
    printf("---------------------------------------------------\n");

    char continuar = 'y';
    float tensao;

    while (continuar != 'q') {
        printf("Digite a tensão atual (em volts): ");
        scanf("%f", &tensao);

        if (tensao < 3.5) {
            printf("Tensão Baixa!\n");
        } else if (tensao >= 3.5 && tensao <= 4.2) {
            printf("Tensão Média!\n");
        } else {
            printf("Tensão Alta! Alerta!\n");
        }

        printf("Pressione 'q' para sair ou qualquer outra tecla para continuar: ");
        scanf(" %c", &continuar);
    }

    // ##################################################################
    // 2) Atividade 2: Análise de Frequências em um Espectro 
    // ==================================================================
    printf("\n2) Atividade 2: Análise de Frequências em um Espectro\n");
    printf("---------------------------------------------------\n");

    for (int i = 0; i <= 90; i += 10) {
        printf("Analisando faixa de %dGHz a %dGHz: ", i, i + 10);
        if (i < 10) {
            printf("Comunicação móvel\n");
        } else if (i < 20) {
            printf("Satélite\n");
        } else if (i < 30) {
            printf("Radar\n");
        } else if (i < 40) {
            printf("Comunicação por fibra ótica\n");
        } else if (i < 50) {
            printf("Wi-Fi\n");
        } else if (i < 60) {
            printf("Radiodifusão\n");
        } else if (i < 70) {
            printf("Pesquisa astronômica\n");
        } else if (i < 80) {
            printf("Medicina e imagiologia\n");
        } else if (i < 90) {
            printf("Comunicações militares\n");
        } else {
            printf("Pesquisa científica\n");
        }
    }

    // ##################################################################
    // 3) Atividade 3: Simulação Simplificada de um Osciloscópio 
    // ==================================================================
    printf("\n3) Atividade 3: Simulação Simplificada de um Osciloscópio\n");
    printf("---------------------------------------------------\n");

    int frequencia;
    printf("Insira uma frequência (número entre 1 e 10): ");
    scanf("%d", &frequencia);

    if (frequencia <= 5) {
        printf("-------\n");  // Linha reta
    } else {
        printf("/\\/\\/\n"); // Onda senoidal
    }

    // ##################################################################
    // 4) Atividade 4: Medição Iterativa de Resistência em um Circuito 
    // ==================================================================
    printf("\n4) Atividade 4: Medição Iterativa de Resistência em um Circuito\n");
    printf("---------------------------------------------------\n");

    float resistencia, total = 0, media, maior_resistencia = 0, menor_resistencia = 1000000;  // assumindo um valor inicial alto para menor_resistencia

    for (int i = 0; i < 5; i++) {
        printf("Digite o valor da resistência na medição %d (em Ohms): ", i + 1);
        scanf("%f", &resistencia);
        total += resistencia;
        if (resistencia > maior_resistencia) {
            maior_resistencia = resistencia;
        }
        if (resistencia < menor_resistencia) {
            menor_resistencia = resistencia;
        }
    }

    media = total / 5;
    printf("Média das resistências: %.2f Ohms\n", media);

    if ((maior_resistencia - menor_resistencia) > 0.05 * media) {
        printf("Alerta! Possível instabilidade do resistor detectada.\n");
    }

    // ##################################################################
    // 5) Atividade 5: Monitoramento de Faixas de Frequência 
    // ==================================================================
    printf("\n5) Atividade 5: Monitoramento de Faixas de Frequência\n");
    printf("---------------------------------------------------\n");

    float freq;
    continuar = 'y';

    while (continuar != 'n') {
        printf("Digite uma frequência em MHz: ");
        scanf("%f", &freq);

        if (freq >= 88 && freq <= 108) {
            printf("Rádio FM\n");
        } else if (freq >= 2400 && freq <= 2500) {
            printf("Wi-Fi\n");
        } else if (freq == 1575.42) {
            printf("GPS\n");
        } else {
            printf("Frequência não corresponde a nenhum serviço conhecido.\n");
        }

        printf("Deseja continuar? (y/n): ");
        scanf(" %c", &continuar);
    }

    // ##################################################################
    // 6) Atividade 6: Treinamento Iterativo de um Neurônio Artificial 
    // ==================================================================
    printf("\n6) Atividade 6: Treinamento Iterativo de um Neurônio Artificial\n");
    printf("---------------------------------------------------\n");

    srand(time(0));
    float peso = (float)rand() / RAND_MAX;  // Peso inicial aleatório entre 0 e 1
    float erro;

    printf("Peso inicial: %.2f\n", peso);
    do {
        printf("Digite o valor do erro (-1 a 1, ou -999 para sair): ");
        scanf("%f", &erro);

        if (erro != -999) {
            peso -= erro;
            printf("Novo peso: %.2f\n", peso);
        }

    } while (erro != -999);

    // ##################################################################
    // 7) Atividade 7: Análise de Valores Lógicos Consecutivos 
    // ==================================================================
    printf("\n7) Atividade 7: Análise de Valores Lógicos Consecutivos\n");
    printf("---------------------------------------------------\n");

    int valor1, valor2, valor3;
    printf("Digite o primeiro valor lógico (0 ou 1): ");
    scanf("%d", &valor1);
    printf("Digite o segundo valor lógico (0 ou 1): ");
    scanf("%d", &valor2);
    printf("Digite o terceiro valor lógico (0 ou 1): ");
    scanf("%d", &valor3);

    if (valor1 == valor2 && valor2 == valor3) {
        if (valor1 == 0) {
            printf("Todos os valores são '0'\n");
        } else {
            printf("Todos os valores são '1'\n");
        }
    } else {
        printf("Os valores são uma mistura de '0's e '1's\n");
    }

    // ##################################################################
    // 8) Atividade 8: Processamento Iterativo de Sinais 
    // ==================================================================
    printf("\n8) Atividade 8: Processamento Iterativo de Sinais\n");
    printf("---------------------------------------------------\n");

    int numLeituras;
    float valor, soma = 0;

    printf("Quantas leituras de sinal você deseja fazer? ");
    scanf("%d", &numLeituras);

    for (int i = 0; i < numLeituras; i++) {
        printf("Digite o valor da leitura %d: ", i+1);
        scanf("%f", &valor);
        soma += valor;
    }

    printf("Média dos valores: %.2f\n", soma / numLeituras);

    // ##################################################################
    // 9) Atividade 9: Catalogação Automatizada de Componentes
    // ==================================================================
    printf("\n9) Atividade 9: Catalogação Automatizada de Componentes\n");
    printf("---------------------------------------------------\n");

    int codigo;

    printf("Digite um código numérico (1 a 5): ");
    scanf("%d", &codigo);

    switch (codigo) {
        case 1:
            printf("Resistor\n");
            break;
        case 2:
            printf("Capacitor\n");
            break;
        case 3:
            printf("Indutor\n");
            break;
        case 4:
            printf("Transistor\n");
            break;
        case 5:
            printf("Diodo\n");
            break;
        default:
            printf("Código inválido!\n");
    }

    // ##################################################################
    // 10) Atividade 10: Classificação Iterativa de Dados
    // ==================================================================
    printf("\n10) Atividade 10: Classificação Iterativa de Dados\n");
    printf("---------------------------------------------------\n");

    int numValores;

    printf("Quantos valores você deseja classificar? ");
    scanf("%d", &numValores);

    for (int i = 0; i < numValores; i++) {
        printf("Digite o valor %d (0 a 10): ", i+1);
        scanf("%f", &valor);

        if (valor >= 0 && valor <= 3.99) {
            printf("Baixo\n");
        } else if (valor >= 4 && valor <= 6.99) {
            printf("Médio\n");
        } else if (valor >= 7 && valor <= 10) {
            printf("Alto\n");
        } else {
            printf("Valor inválido!\n");
        }
    }

    return 0;
}
