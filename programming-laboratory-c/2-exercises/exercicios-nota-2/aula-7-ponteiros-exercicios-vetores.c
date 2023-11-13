/**************************************************************************
*                                                                         *
*           Universidade Federal do Maranhão                              *
*       Departamento de Engenharia da Computação                          *
*                                                                         *
*  Author: Professor Doutor Thales Levi Azevedo Valente                  *
*                                                                         *
*  Description: Material de Ensino - Operações com Vetores                *
*                                                                         *
*  Date: 12-11-2023                                                       *
*                                                                         *
* Este material fornece uma introdução profunda às operações com vetores, *
* usando ponteiros, em C, abordando conceitos como média, máximo,         *
* mínimo, palíndromos, etc.                                               *
* Conteúdos do Material:                                                  *
*   1. Cálculo da média de um vetor de inteiros                           *
*   2. Encontrar o valor máximo em um vetor de floats                     *
*   3. Contar quantas vezes um número específico aparece em um vetor      *
*   4. Somar todos os valores em um vetor de floats                       *
*   5. Inverter a ordem de um vetor de inteiros                           *
*   6. Determinar se um vetor de inteiros é palíndromo                    *
*   7. Cálculo da variância de um vetor de floats                         *
*   8. Encontrar o segundo maior valor em um vetor de inteiros            *
*   9. Verificar se um vetor de inteiros está em ordem crescente          *
*   10. Calcular o produto escalar entre dois vetores de floats            *
*   11. Classificar uma fruta com base em suas características e pesos    *
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
*   7- NOME DO ARQUIVO É "NOME_SOBRENOME1_SOBRENOME2"                     *
*   8- Veja os arquivos de casos de testes para ver como deve imprimir as saídas*
* -------------------------------------------------------------------------*
*                                                                         *
* Inicie o código abaixo para começar a exploração.                       *
*                                                                         *
***************************************************************************/

#include <stdio.h>
#include <string.h>
#include <math.h>
// USE APENAS ARITMÉTICA DE PONTEIROS. NÃO USE INDEXADORES ENTRE COLCHETES (EX:[i][j]).
// Protótipos das funções
/* 
   Enunciado: Implemente uma função que calcula a média de um vetor de inteiros com 3 posições. A média é calculada somando-se todos os elementos e dividindo pelo número de elementos.
   Exemplo: 
   Entrada: 1 2 6
   Saída: 3.00
*/
// USE APENAS ARITMÉTICA DE PONTEIROS. NÃO USE INDEXADORES ENTRE COLCHETES (EX:[i][j]).
void media_vetor_inteiros(){
    int vetor[3];
    int soma = 0;
    int *ptr;

    for (ptr = vetor; ptr < vetor + 3; ptr++) {
        scanf("%d", ptr);
        soma += *ptr;
    }
    printf("%.2f\n", (float)soma / 3);
}


/* 
   Enunciado: Implemente uma função que retorna o valor máximo de um vetor de floats com 3 posições.
   Exemplo: 
   Entrada: 1.2 10.3 9.2
   Saída: 10.30
*/
// USE APENAS ARITMÉTICA DE PONTEIROS. NÃO USE INDEXADORES ENTRE COLCHETES (EX:[i][j]).
void maximo_vetor_floats(){
    float vetor[3];
    float *ptr, maximo = -INFINITY;

    for (ptr = vetor; ptr < vetor + 3; ptr++) {
        scanf("%f", ptr);
        if (*ptr > maximo) {
            maximo = *ptr;
        }
    }

    printf("%.2f\n", maximo);
}

/* 
   Enunciado: Implemente uma função que conta quantas vezes um número específico aparece em um vetor de inteiros com 3 posições.
   Exemplo: 
   Entrada: 1 3 3
            3
   Saída: 2
*/
// USE APENAS ARITMÉTICA DE PONTEIROS. NÃO USE INDEXADORES ENTRE COLCHETES (EX:[i][j]).
void conta_numero_especifico(){
    int vetor[3];
    int numero, contador = 0;
    int *ptr;

    for (ptr = vetor; ptr < vetor + 3; ptr++) {
        scanf("%d", ptr);
    }
    scanf("%d", &numero);

    for (ptr = vetor; ptr < vetor + 3; ptr++) {
        if (*ptr == numero) {
            contador++;
        }
    }

    printf("%d\n", contador);
}

/* 
   Enunciado: Implemente uma função que soma todos os valores de um vetor de floats com 3 posições.
   Exemplo: 
   Entrada: 1.2 2.3 3.4
   Saída: 6.90
*/
// USE APENAS ARITMÉTICA DE PONTEIROS. NÃO USE INDEXADORES ENTRE COLCHETES (EX:[i][j]).
void soma_vetor_floats();

/* 
   Enunciado: Implemente uma função que inverte a ordem de um vetor de inteiros com 3 posições.
   Exemplo: 
   Entrada: 1 2 3
   Saída: 3 2 1
*/
// USE APENAS ARITMÉTICA DE PONTEIROS. NÃO USE INDEXADORES ENTRE COLCHETES (EX:[i][j]).
void inverte_vetor_inteiros();

/* 
   Enunciado: Implemente uma função que encontra o segundo maior valor de um vetor de inteiros com 5 posições. 
   Exemplo: 
   Entrada: 5 3 8 6 4
   Saída: 6
*/
// USE APENAS ARITMÉTICA DE PONTEIROS. NÃO USE INDEXADORES ENTRE COLCHETES (EX:[i][j]).
void segundo_maior_valor_vetor_inteiros();

/* 
   Enunciado: Implemente uma função que verifica se um vetor de inteiros com 10 posições é palíndromo. Um vetor é considerado palíndromo se for igual ao seu reverso.
   Exemplos: 
   Entrada: 1 2 3 4 5 5 4 3 2 1
   Saída: Palindromo

   Entrada: 1 2 3 4 5 6 7 8 9 10
   Saída: Nao Palindromo
*/
// USE APENAS ARITMÉTICA DE PONTEIROS. NÃO USE INDEXADORES ENTRE COLCHETES (EX:[i][j]).
void verifica_palindromo();

/* 
   Enunciado: Implemente uma função que calcula a variância de um vetor de floats com 5 posições. A variância é a média dos quadrados das diferenças entre cada valor e a média dos valores.
   A variância é uma medida de dispersão que indica o quão longe os valores estão da média do conjunto.
   Utilize a fórmula:
   variancia = 1/N * sum((vetor[i] - media)^2) para i de 0 a N-1
   onde N é o número de elementos, vetor[i] é o valor do i-ésimo elemento e media é a média dos valores do vetor.
   Exemplo: 
   Entrada: 5.2 3.4 7.8 6.1 4.3
   Saída: 2.30
*/
// USE APENAS ARITMÉTICA DE PONTEIROS. NÃO USE INDEXADORES ENTRE COLCHETES (EX:[i][j]).
void variancia_vetor_floats();

/* 
   Enunciado: Implemente uma função que verifica se um vetor de inteiros com 5 posições está em ordem crescente.
   Exemplos: 
   Entrada: 1 2 3 4 5
   Saída: Sim

   Entrada: 1 2 7 4 5
   Saída: Nao
*/
// USE APENAS ARITMÉTICA DE PONTEIROS. NÃO USE INDEXADORES ENTRE COLCHETES (EX:[i][j]).
void vetor_em_ordem_crescente();

/* 
   Enunciado: Implemente uma função que calcula o produto escalar entre dois vetores de floats com 3 posições cada. 
   O produto escalar é a soma dos produtos dos elementos correspondentes dos vetores.
   Utilize a fórmula:
   produtoEscalar = sum(vetor1[i] * vetor2[i]) para i de 0 a 2
   Exemplo: 
   Entrada: 1.0 2.0 3.0
            2.0 3.0 4.0
   Saída: 20.00
*/
// USE APENAS ARITMÉTICA DE PONTEIROS. NÃO USE INDEXADORES ENTRE COLCHETES (EX:[i][j]).
void produto_escalar_vetores_floats();

/* 
   Enunciado: Implemente uma função que classifica uma fruta com base em suas características e pesos fornecidos em dois vetores de floats com 3 posições cada. 
   Enunciado (classifica_fruta): Dados um vetor de características e um vetor de pesos, ambos com 3 posições, determine a classe de uma fruta.
   Primeiro, calcule a saída (saida) utilizando:
   saida = sum(caracteristicas[i] * pesos[i]) para i de 0 a 2
   Em seguida, aplique a função sigmoide à saída:
   saida_final = 1 / (1 + exp(-saida))
   Se a saida_final for maior ou igual a 0.5, a fruta é classificada como Classe A; caso contrário, como Classe B.
   Exemplos: 
   Entrada: 0.7 0.5 0.3
            0.7 0.5 0.3
   Saída: Classe A

   Entrada: 0.6 0.4 0.2
            -0.8 -0.2 0.5
   Saída: Classe B
*/
// USE APENAS ARITMÉTICA DE PONTEIROS. NÃO USE INDEXADORES ENTRE COLCHETES (EX:[i][j]).
void classifica_fruta();

// OBS. NÃO modifique a main

int main() {
    char function_name[100];
    scanf("%s", function_name);

    if (strcmp(function_name, "media_vetor_inteiros") == 0) {
        media_vetor_inteiros();
    } else if (strcmp(function_name, "maximo_vetor_floats") == 0) {
        maximo_vetor_floats();
    } else if (strcmp(function_name, "conta_numero_especifico") == 0) {
        conta_numero_especifico();
    } else if (strcmp(function_name, "soma_vetor_floats") == 0) {
        soma_vetor_floats();
    } else if (strcmp(function_name, "inverte_vetor_inteiros") == 0) {
        inverte_vetor_inteiros();
    } else if (strcmp(function_name, "verifica_palindromo") == 0) {
        verifica_palindromo();
    } else if (strcmp(function_name, "variancia_vetor_floats") == 0) {
        variancia_vetor_floats();
    } else if (strcmp(function_name, "segundo_maior_valor_vetor_inteiros") == 0) {
        segundo_maior_valor_vetor_inteiros();
    } else if (strcmp(function_name, "vetor_em_ordem_crescente") == 0) {
        vetor_em_ordem_crescente();
    } else if (strcmp(function_name, "produto_escalar_vetores_floats") == 0) {
        produto_escalar_vetores_floats();
    }else if (strcmp(function_name, "classifica_fruta") == 0) {
        classifica_fruta();
    }

    return 0;
}
