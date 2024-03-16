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

int main() {
    // ##################################################################
    // 1) Atividade 1: Sistema de Monitoramento de Tensão 
    // ==================================================================
    printf("\n1) Atividade 1: Sistema de Monitoramento de Tensão\n");
    printf("---------------------------------------------------\n");
    // Contexto: Em sistemas elétricos e eletrônicos, monitorar a tensão é crucial para garantir a segurança e o correto funcionamento dos dispositivos.
    // TO-DO: Implemente um sistema que lê a tensão (em volts) e classifica como:
    // - Baixa (menor que 1V)
    // - Média (entre 1V e 3V)
    // - Alta (maior que 3V)
    // O sistema deve exibir alertas adequados para cada faixa de tensão.

    // ##################################################################
    // 2) Atividade 2: Cálculo de Potência 
    // ==================================================================
    printf("\n2) Atividade 2: Cálculo de Potência\n");
    printf("---------------------------------------------------\n");
    // Contexto: A potência é uma operação matemática fundamental em engenharia, frequentemente usada em análises de circuitos elétricos, cálculos de energia e outros.
    // Formula: Potência = Base^Expoente
    // TO-DO: Solicite ao usuário a base e o expoente, e calcule a potência.

    // ##################################################################
    // 3) Atividade 3: Conversão Simplificada de Bases Numéricas
    // ==================================================================
    printf("\n3) Atividade 3: Conversão Simplificada de Bases Numéricas\n");
    printf("---------------------------------------------------\n");
    // Contexto: A conversão entre bases numéricas é fundamental em computação. Enquanto computadores operam internamente com base binária, os humanos geralmente usam base decimal.
    // TO-DO: Solicite ao usuário um número decimal de 0 a 7 e converta-o para binário usando apenas desvios condicionais.


    // ##################################################################
    // 4) Atividade 4: Lei de Ohm 
    // ==================================================================
    printf("\n4) Atividade 4: Lei de Ohm\n");
    printf("---------------------------------------------------\n");
    // Contexto: A Lei de Ohm é fundamental na análise e design de circuitos elétricos. Ela relaciona a tensão, corrente e resistência em um circuito.
    // Formula: V = I * R
    // TO-DO: Solicite ao usuário os valores de corrente (I) e resistência (R) e calcule a tensão (V).

    // ##################################################################
    // 5) Atividade 5: Simulador de Espectro de Frequência 
    // ==================================================================
    printf("\n5) Atividade 5: Simulador de Espectro de Frequência\n");
    printf("---------------------------------------------------\n");

    // Contexto: 
    // Em engenharia da computação e em telecomunicações, o espectro de frequência é fundamental. As faixas de frequência são meticulosamente alocadas para evitar interferências entre diferentes tecnologias e serviços. Por exemplo, estações de rádio FM não interferem no Wi-Fi doméstico porque operam em diferentes faixas de frequência. Cada faixa tem suas propriedades e usos específicos em diferentes aplicações, desde comunicação móvel até satélites e radar.

    // Desafio:
    // Você está desenvolvendo um sistema de monitoramento e precisa classificar rapidamente as faixas de frequência para identificar potenciais interferências ou alocar novos serviços.
    // TO-DO: Implemente um simulador que lê a frequência (em GHz) do usuário e determina a que faixa pertence, como:
    // - Frequência de rádio (menor que 1GHz)
    // - Frequência de micro-ondas (entre 1GHz e 100GHz)
    // - Frequência de terahertz (maior que 100GHz)

    // ##################################################################
    // 6) Atividade 6: Cálculo da Saída de um Neurônio Simples 
    // ==================================================================
    printf("\n6) Atividade 6: Cálculo da Saída de um Neurônio Simples\n");
    printf("---------------------------------------------------\n");

    // Contexto: 
    //  Nas últimas décadas, as redes neurais têm sido uma ferramenta fundamental em várias aplicações de aprendizado de máquina, 
    //  desde reconhecimento de voz até detecção de objetos em imagens. O nome "rede neural" é inspirado no funcionamento do cérebro 
    //  humano e, da mesma forma que o cérebro é composto por neurônios interconectados, uma rede neural é composta por neurônios artificiais 
    //  interconectados. Um neurônio artificial simples processa a informação multiplicando sua entrada por um peso, adicionando um bias e, 
    //  em seguida, possivelmente passando o resultado por uma função de ativação. Esse modelo simplificado é poderoso o suficiente para 
    //  permitir que redes neurais aprendam uma variedade incrível de tarefas.
    // Desafio:
    //  Imagine que você está começando a desenvolver um sistema de reconhecimento de padrões e quer entender o cálculo básico realizado 
    //  por um neurônio individual antes de mergulhar em redes mais complexas.
    // TO-DO: Solicite ao usuário valores para a entrada, o peso e o bias de um neurônio. Calcule e exiba a saída, conforme a fórmula: Saída = Entrada x Peso + Bias.


    // ##################################################################
    // 7) Atividade 7: Identificação de Circuitos Lógicos
    // ==================================================================
    printf("\n7) Atividade 7: Identificação de Circuitos Lógicos\n");
    printf("---------------------------------------------------\n");

    // Contexto:
    //  Em nossos dispositivos eletrônicos diários, de smartphones a computadores de alto desempenho, o processamento de informações ocorre em nível binário. 
    //  Os circuitos lógicos, também conhecidos como portas lógicas, são fundamentais nesse processo. São os blocos de construção básicos dos chips de computador 
    //  e são usados para realizar operações lógicas básicas que estão no núcleo da aritmética do computador e da tomada de decisão.

    // Desafio:
    //  A capacidade de identificar e compreender a função desses circuitos é fundamental para qualquer engenheiro ou entusiasta da eletrônica. 
    //  Vamos associar cada circuito lógico a um número para facilitar sua identificação:
    //  1 - AND
    //  2 - OR
    //  3 - NOT
    //  ... (e assim por diante, se desejado)

    // TO-DO: 
    //  1. Solicite ao usuário que insira um número correspondente a um tipo específico de circuito lógico.
    //  2. Usando desvios condicionais, identifique o tipo de circuito com base no número fornecido e imprima na tela o nome do circuito e uma breve descrição da sua função.

    // ##################################################################
    // 8) Atividade 8: Normalização de Dados
    // ==================================================================
    printf("\n8) Atividade 8: Normalização de Dados\n");
    printf("---------------------------------------------------\n");

    // Contexto:
    //  Em muitos problemas de aprendizado de máquina, os dados de entrada podem variar amplamente em magnitude. Por exemplo, a idade de uma pessoa pode estar entre 0 e 100, enquanto seu salário pode variar de milhares a milhões. Quando esses dados são usados para treinar modelos, características com magnitudes maiores podem dominar o treinamento, levando a modelos subótimos. 
    //  A normalização é uma técnica de pré-processamento que ajuda a transformar todas as características para uma escala comum, geralmente entre 0 e 1. Ao fazer isso, cada característica tem a mesma importância durante o treinamento, tornando o processo mais eficiente e produzindo um modelo mais equilibrado. A técnica apresentada aqui, onde subtraímos o mínimo e dividimos pelo intervalo (máximo - mínimo), é uma das abordagens mais comuns para normalização.

    // Formula: x_norm = (x - min) / (max - min)

    // TO-DO: 
    //  1. Solicite ao usuário valores de x, min e max.
    //  2. Calcule o valor normalizado usando a fórmula acima.
    //  3. Mostre o valor normalizado ao usuário.


    // ##################################################################
    // 9) Atividade 9: Catálogo de Componentes Eletrônicos 
    // ==================================================================
    printf("\n9) Atividade 9: Catálogo de Componentes Eletrônicos\n");
    printf("---------------------------------------------------\n");

    // Contexto:
    //  A engenharia eletrônica abrange uma variedade de componentes, cada um com suas características e aplicações específicas. Para engenheiros, técnicos e entusiastas, é vital identificar rapidamente componentes para projetar, construir e depurar circuitos de maneira eficiente. Um catálogo eletrônico permite uma rápida referência e identificação de componentes, auxiliando na tomada de decisões durante o projeto e a análise de circuitos.

    // TO-DO:
    //  1. Implemente um catálogo que lê um código numérico.
    //  2. Exiba o componente associado ao código.
    //  3. Caso o código não corresponda a um componente, exiba "Código inválido".

    // ##################################################################
    // 10) Atividade 10: Classificação Binária Simples
    // ==================================================================
    printf("\n10) Atividade 10: Classificação Binária Simples\n");
    printf("---------------------------------------------------\n");

    // Contexto:
    //  Em muitos problemas de aprendizado de máquina, especialmente em áreas como processamento de linguagem natural, visão computacional e análise de sentimento, os dados são categorizados em duas classes distintas. Isso é conhecido como classificação binária. Por exemplo, um email pode ser "spam" ou "não spam", ou uma imagem pode conter um gato ou não. A capacidade de classificar com precisão esses dados é crucial para muitas aplicações modernas. Utilizar um limiar para decidir a classe de uma entrada é uma das abordagens mais básicas e fundamentais na classificação binária.

    // TO-DO:
    //  1. Solicite ao usuário um valor de entrada e um limiar.
    //  2. Se a entrada for maior que o limiar, imprima "Classe A".
    //  3. Caso contrário, imprima "Classe B".

    return 0;
}
