/**************************************************************************
*                                                                         *
*           Universidade Federal do Maranhão                              *
*       Departamento de Engenharia da Computação                          *
*                                                                         *
*  Author: Professor Doutor Thales Levi Azevedo Valente                  *
*                                                                         *
*  Description: Material de Ensino - Laboratório de Programação C         *
*                                                                         *
*  Date: 29-10-2023                                                       *
*                                                                         *
* Este material fornece uma introdução profunda às operações de strings   *
* em C, com foco nas funções de manipulação e verificação de strings,     *
* bem como técnicas para processar e analisar texto.                      *
*                                                                         *
* Conteúdos do Material:                                                  *
*   1. Inversão de Strings                                                *
*   2. Contagem de Vogais                                                 *
*   3. Transformação para Maiúsculas                                      *
*   4. Verificação de Palíndromo                                          *
*   5. Contagem de Palavras                                               *
*   6. Capitalização de Strings                                           *
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

/* 
   Enunciado: Implemente uma função que inverte a string dada.
   Exemplo: 
   Entrada: "Hello"
   Saída: "olleH"
*/
void inversao_de_strings();

/* 
   Enunciado: Implemente uma função que conta o número de vogais na string dada.
   Exemplo: 
   Entrada: "Hello World"
   Saída: 3
*/
void contagem_de_vogais();

/* 
   Enunciado: Implemente uma função que transforma todos os caracteres da string dada em maiúsculas.
   Exemplo: 
   Entrada: "Hello"
   Saída: "HELLO"
*/
void transformacao_para_maiusculas();

/* 
   Enunciado: Implemente uma função que verifica se a string dada é um palíndromo.
   Exemplo: 
   Entrada: "level"
   Saída: "É um palíndromo"
*/
void verificacao_de_palindromo();


/* 
   Enunciado: Implemente uma função que conta o número de palavras na string dada.
   Exemplo: 
   Entrada: "Hello World from C"
   Saída: 4
*/
void contagem_de_palavras();


/* 
   Enunciado: Implemente uma função que capitalize a primeira letra de cada palavra na string dada.
   Exemplo: 
   Entrada: "hello world"
   Saída: "Hello World"
*/
void capitalize();

// OBS. NÃO modifique a main
int main() {
    char function_name[100];
    scanf("%s", function_name);

    if (strcmp(function_name, "inversao_de_strings") == 0) {
        inversao_de_strings();
    } else if (strcmp(function_name, "contagem_de_vogais") == 0) {
        contagem_de_vogais();
    } else if (strcmp(function_name, "transformacao_para_maiusculas") == 0) {
        transformacao_para_maiusculas();
    } else if (strcmp(function_name, "verificacao_de_palindromo") == 0) {
        verificacao_de_palindromo();
    } else if (strcmp(function_name, "contagem_de_palavras") == 0) {
        contagem_de_palavras();
    } else if (strcmp(function_name, "capitalize") == 0) {
        capitalize();
    }

    return 0;
}
