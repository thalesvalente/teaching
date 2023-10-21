/**************************************************************************
*                                                                         *
*           Universidade Federal do Maranhão                              *
*       Departamento de Engenharia da Computação                          *
*                                                                         *
*  Author: Professor Doutor Thales Levi Azevedo Valente                  *
*                                                                         *
*  Description: Material de Ensino - Laboratório de Programação C         *
*                                                                         *
*  Date: 16-10-2023                                                       *
*                                                                         *
* Este material fornece uma introdução abrangente às funções de entrada   *
* e saída em C, com foco nas funções printf, scanf, desvios condicionais *
* e o início de funções. Ele explora a                                    *
* utilização de especificadores de formato para diferentes tipos de      *
* dados, bem como técnicas de captura de entrada.                         *
*                                                                         *
* Conteúdos do Material:                                                  *
*   1. Demonstração de printf                                            *
*   2. Demonstração de scanf                                              *
*   3. Operadores                                                         *
*   4. Desvios Condicionais                                             *
*   4. Código de Exemplo                                                  *
*                                                                         *
* Inicie o código abaixo para começar a exploração.                       *
*                                                                         *
***************************************************************************
* -------------------------------------------------------------------------*
*   IMPORTANTE:                                                           *
*   1- NÃO modifique a assinatura das funções (tipo retorno, nome, parâm.)*
*   2- Apenas implemente o corpo das funções trocando o ; por chaves      *
*   3- NÃO modifique a main                                               *
*   4- Veja o arquivo "exemplo.c"                                         *
*   5- Use printf APENAS para imprimir o resultado                        *
*   6- CUIDADO ao usar o scanf                                            *
* -------------------------------------------------------------------------*
*                                                                         *
* Inicie o código abaixo para começar a exploração.                       *
*                                                                         *
***************************************************************************/

#include <stdio.h>
#include <math.h>
#include <string.h>

// Protótipos das funções:
void sistema_monitoramento_tensao(){
    double tensao;
    scanf("%lf", &tensao);
    if (tensao < 1) {
        printf("Baixa\n");
    } else if (tensao >= 1 && tensao <= 3) {
        printf("Media\n");
    } else {
        printf("Alta\n");
    }
}
void calculo_potencia(){
    double base, expoente, potencia;
    scanf("%lf", &base);
    scanf("%lf", &expoente);
    potencia = pow(base, expoente);
    printf("%.2lf\n", potencia);
}
void conversao_bases_numericas(){
    int numero;
    scanf("%d", &numero);
    switch(numero) {
        case 0: printf("000\n"); break;
        case 1: printf("001\n"); break;
        case 2: printf("010\n"); break;
        case 3: printf("011\n"); break;
        case 4: printf("100\n"); break;
        case 5: printf("101\n"); break;
        case 6: printf("110\n"); break;
        case 7: printf("111\n"); break;
        default: printf("Invalido\n");
    }
}
void lei_ohm(){
    double corrente, resistencia, tensaoOhm;
    scanf("%lf", &corrente);
    scanf("%lf", &resistencia);
    tensaoOhm = corrente * resistencia;
    printf("%.2lfV\n", tensaoOhm);
}
void simulador_espectro_frequencia(){
    double frequencia;
    scanf("%lf", &frequencia);
    if (frequencia < 1) {
        printf("Radio\n");
    } else if (frequencia >= 1 && frequencia <= 100) {
        printf("Micro-ondas\n");
    } else {
        printf("Terahertz\n");
    }
}
void saida_neuronio_simples(){
    double entrada, peso, bias, saida;
    scanf("%lf", &entrada);
    scanf("%lf", &peso);
    scanf("%lf", &bias);
    saida = entrada * peso + bias;
    printf("%.2lf\n", saida);
}
void identificacao_circuitos_logicos(){
    int codigoCircuito;
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
            printf("Invalido\n");
    }
}
void normalizacao_dados(){
    double x, min, max, x_norm;
    scanf("%lf", &x);
    scanf("%lf", &min);
    scanf("%lf", &max);
    x_norm = (x - min) / (max - min);
    printf("%.2lf\n", x_norm);
}
void catalogo_componentes_eletronicos(){
    int codigoComponente;
    scanf("%d", &codigoComponente);
    switch(codigoComponente) {
        case 1: 
            printf("Resistor\n");
            break;
        case 2:
            printf("Capacitor\n");
            break;
        case 3:
            printf("Diodo\n");
            break;
        default: 
            printf("Invalido\n");
    }
}
void classificacao_binaria_simples(){
    double entrada, limiar;
    scanf("%lf", &entrada);
    scanf("%lf", &limiar);
    if (entrada > limiar) {
        printf("Classe A\n");
    } else {
        printf("Classe B\n");
    }
}

int main() {
    char function_name[50];
    scanf("%s", function_name);
    
    //1
    if (strcmp(function_name, "sistema_monitoramento_tensao") == 0) {
        sistema_monitoramento_tensao();
        //2
    } else if (strcmp(function_name, "calculo_potencia") == 0) {
        calculo_potencia();
        //3
    } else if (strcmp(function_name, "conversao_bases_numericas") == 0) {
        conversao_bases_numericas();
        //4
    } else if (strcmp(function_name, "lei_ohm") == 0) {
        lei_ohm();
        //5
    } else if (strcmp(function_name, "simulador_espectro_frequencia") == 0) {
        simulador_espectro_frequencia();
        //6
    } else if (strcmp(function_name, "saida_neuronio_simples") == 0) {
        saida_neuronio_simples();
        //7
    } else if (strcmp(function_name, "identificacao_circuitos_logicos") == 0) {
        identificacao_circuitos_logicos();
        //8
    } else if (strcmp(function_name, "normalizacao_dados") == 0) {
        normalizacao_dados();
        //9
    } else if (strcmp(function_name, "catalogo_componentes_eletronicos") == 0) {
        catalogo_componentes_eletronicos();
        //10
    } else if (strcmp(function_name, "classificacao_binaria_simples") == 0) {
        classificacao_binaria_simples();
    }

    return 0;
}