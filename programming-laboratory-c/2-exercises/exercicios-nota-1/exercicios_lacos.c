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
*   5. Laços de repetição                                                 *
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
*   7- NOME DO ARQUIVO É "NOME_SOBRENOME1_SOBRENOME2"                       *
*   8- Veja os arquivos de casos de testes para ver como deve imprimir as saidas*
* -------------------------------------------------------------------------*
*                                                                         *
* Inicie o código abaixo para começar a exploração.                       *
*                                                                         *
***************************************************************************/


#include <stdio.h>
#include <string.h>

// Protótipos das funções
// OBS. NÃO modifique a assinatura das funções (tipo retorno, nome, parâmetros).
// Apenas implemente o corpo delas trocando o ; por chaves
void monitoramento_continuo_de_tensao();
void analise_de_frequencias_em_um_espectro();
void simulacao_simplificada_de_um_osciloscopio();
void medicao_iterativa_de_resistencia_em_um_circuito();
void monitoramento_de_faixas_de_frequencia();
void treinamento_iterativo_de_um_neuronio_artificial();
void analise_de_sequencias_logicas();
void processamento_iterativo_de_sinais();
void catalogacao_automatizada_de_componentes();
void classificacao_iterativa_de_dados();

// OBS. NÃO modifique a main
int main() {
    char function_name[100];
    scanf("%s", function_name);

    if (strcmp(function_name, "monitoramento_continuo_de_tensao") == 0) {
        monitoramento_continuo_de_tensao();
    } else if (strcmp(function_name, "analise_de_frequencias_em_um_espectro") == 0) {
        analise_de_frequencias_em_um_espectro();
    } else if (strcmp(function_name, "simulacao_simplificada_de_um_osciloscopio") == 0) {
        simulacao_simplificada_de_um_osciloscopio();
    } else if (strcmp(function_name, "medicao_iterativa_de_resistencia_em_um_circuito") == 0) {
        medicao_iterativa_de_resistencia_em_um_circuito();
    } else if (strcmp(function_name, "monitoramento_de_faixas_de_frequencia") == 0) {
        monitoramento_de_faixas_de_frequencia();
    } else if (strcmp(function_name, "treinamento_iterativo_de_um_neuronio_artificial") == 0) {
        treinamento_iterativo_de_um_neuronio_artificial();
    } else if (strcmp(function_name, "analise_de_sequencias_logicas") == 0) {
        analise_de_sequencias_logicas();
    } else if (strcmp(function_name, "processamento_iterativo_de_sinais") == 0) {
        processamento_iterativo_de_sinais();
    } else if (strcmp(function_name, "catalogacao_automatizada_de_componentes") == 0) {
        catalogacao_automatizada_de_componentes();
    } else if (strcmp(function_name, "classificacao_iterativa_de_dados") == 0) {
        classificacao_iterativa_de_dados();
    }

    return 0;
}