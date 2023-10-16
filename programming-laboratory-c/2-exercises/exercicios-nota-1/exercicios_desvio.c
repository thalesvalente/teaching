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
*   5. Código de Exemplo                                                  *
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
*   7- NOME DO ARQUIVO É "NOME_SOBRENOME1_SOBRENOME2"                     *                                     *
* -------------------------------------------------------------------------*
*                                                                         *
* Inicie o código abaixo para começar a exploração.                       *
*                                                                         *
***************************************************************************/

#include <stdio.h>
#include <math.h>
#include <string.h>


// Protótipos das funções
void sistema_monitoramento_tensao();
void calculo_potencia();
void conversao_bases_numericas();
void lei_ohm();
void simulador_espectro_frequencia();
void saida_neuronio_simples();
void identificacao_circuitos_logicos();
void normalizacao_dados();
void catalogo_componentes_eletronicos();
void classificacao_binaria_simples();

int main() {
    char function_name[50];
    scanf("%s", function_name);
    
    if (strcmp(function_name, "sistema_monitoramento_tensao") == 0) {
        sistema_monitoramento_tensao();
    } else if (strcmp(function_name, "calculo_potencia") == 0) {
        calculo_potencia();
    } else if (strcmp(function_name, "conversao_bases_numericas") == 0) {
        // Chame a função de Conversão Simplificada de Bases Numéricas aqui
    } else if (strcmp(function_name, "lei_ohm") == 0) {
        // Chame a função Lei de Ohm aqui
    } else if (strcmp(function_name, "simulador_espectro_frequencia") == 0) {
        // Chame a função Simulador de Espectro de Frequência aqui
    } else if (strcmp(function_name, "saida_neuronio_simples") == 0) {
        // Chame a função Cálculo da Saída de um Neurônio Simples aqui
    } else if (strcmp(function_name, "identificacao_circuitos_logicos") == 0) {
        // Chame a função Identificação de Circuitos Lógicos aqui
    } else if (strcmp(function_name, "normalizacao_dados") == 0) {
        // Chame a função Normalização de Dados aqui
    } else if (strcmp(function_name, "catalogo_componentes_eletronicos") == 0) {
        // Chame a função Catálogo de Componentes Eletrônicos aqui
    } else if (strcmp(function_name, "classificacao_binaria_simples") == 0) {
        // Chame a função Classificação Binária Simples aqui
    }

    return 0;
}