#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// Protótipos das funções
// OBS. NÃO modifique a assinatura das funções (tipo retorno, nome, parâmetros).
// Apenas implemente o corpo delas trocando o ; por chaves
// 1 - O nome do arquivo OBRIGATORIAMENTE deve ser "nome_sobrenome1.c". Arquivos diferentes serão desconsiderados sera considerado como prova sem nome, ou seja, 0.0 na prova.
// 2 - O arquivo deve conter APENAS as funções pedidas no enunciado.
// 3 - As saídas devem ser exatamente como especificadas nos enunciados. Saídas diferentes serão consideradas ERRADAS (zero na questão).
// 4 - Funções que não compilarão receberão nota ZERO para a função.
// 5 - Funções que apresentarem comportamento diferente do especificado nos enunciados serão consideradas ERRADAS.
// 6 - Arquivos que não compilarem receberão nota ZERO. Então, teste seu código antes de enviar.
// 7 - Arquivos que não seguirem o padrão de nomeação receberão nota ZERO.
// 8 - Funções que entrarem em loop infinito ou travarem o computador receberão nota ZERO.
// 9 - Funções que não passarem pelo autograder receberão nota ZERO.

/*
Atividade 1: Inversão de Vetor
Contexto: Inverter um vetor é uma operação comum em processamento de dados, onde os elementos do vetor são rearranjados em ordem inversa.
- Objetivo: Implementar um programa que inverte a ordem dos elementos de um vetor de inteiros fornecido pelo usuário.
- Entrada: O usuário deve fornecer 10 números inteiros que serão armazenados no vetor.
- Processamento:
    . Leia os 10 números usando scanf e armazene-os em um vetor.
    . Inverta a ordem dos elementos do vetor. Isso pode ser feito trocando o primeiro elemento com o último, o segundo com o penúltimo, e assim por diante, até chegar ao meio do vetor.
- Saída: Exiba o vetor invertido, separando os números por espaços.
*/
void inverte_vetor() {}

/*
Atividade 2: Multiplicação de Matrizes 3x3
Contexto: A multiplicação de matrizes é uma operação fundamental na álgebra linear, com aplicações em diversas áreas, como física, engenharia e economia.
- Objetivo: Implementar um programa que calcula o produto de duas matrizes 3x3 fornecidas pelo usuário.
- Entrada: O usuário deve fornecer os elementos de duas matrizes 3x3.
- Processamento:
    . Leia os elementos das duas matrizes usando scanf.
    . Calcule o produto das matrizes. Para cada elemento C[i][j] da matriz resultante, some os produtos dos elementos correspondentes da linha i da primeira matriz pelos elementos da coluna j da segunda matriz.
- Saída: Exiba a matriz resultante da multiplicação, formatando a saída em linhas e colunas. (numeros separados por espacos e linhas separadas por \n)
*/
void multiplica_matrizes() {}

/*
Atividade 3: Verificação de Matriz Triangular Superior
Contexto: Em álgebra linear, uma matriz triangular superior é uma matriz em que todos os elementos abaixo da diagonal principal são zero.
- Objetivo: Implementar um programa que verifica se uma matriz 3x3 fornecida pelo usuário é uma matriz triangular superior.
- Entrada: O usuário deve fornecer os elementos de uma matriz 3x3.
- Processamento:
    . Leia os elementos da matriz usando scanf.
    . Verifique se todos os elementos abaixo da diagonal principal (ou seja, elementos da forma matriz[i][j] onde i > j) são zero.
- Saída: Exiba "sim" se a matriz for triangular superior; caso contrário, exiba "nao".
*/
void verifica_matriz_triangular_superior() {}


/*
Atividade 4: Implementação do Counting Sort
Contexto: Counting Sort é um algoritmo de ordenação que conta o número de ocorrências de cada elemento para organizar o conjunto de dados. Ele é eficiente quando o intervalo dos elementos do conjunto é conhecido e limitado.
- Objetivo: Implementar o algoritmo Counting Sort para ordenar um vetor de inteiros fornecido pelo usuário.
- Entrada: O usuário deve fornecer 10 números inteiros entre 0 e 9.
- Processamento:
    . Leia os 10 números e armazene-os em um vetor.
    . Use um vetor auxiliar para contar o número de ocorrências de cada número de 0 a 9 no vetor original.
    . Imprima o vetor ordenado usando o vetor de contagem.
- Saída: Exiba o vetor ordenado, separando os números por espaços
*/
void counting_sort() {}

/*
Atividade 5: Transposição de Matriz
Contexto: Em álgebra linear, a transposição de uma matriz é uma operação que troca as linhas pelas colunas.
- Objetivo: Implementar um programa que realiza a transposição de uma matriz 3x3 fornecida pelo usuário.
- Entrada: O usuário deve fornecer os elementos de uma matriz 3x3.
- Processamento:
    . Leia os elementos da matriz usando scanf.
    . Crie uma nova matriz onde o elemento na linha i e coluna j é igual ao elemento na linha j e coluna i da matriz original.
- Saída: Exiba a matriz transposta, formatando a saída em linhas e colunas.
*/
void transpoe_matriz() {}

// OBS. NÃO modifique a main
int main() {
    char function_name[100];
    scanf("%s", function_name);

    if (strcmp(function_name, "inverte_vetor") == 0) {
        inverte_vetor();
    } else if (strcmp(function_name, "multiplica_matrizes") == 0) {
       multiplica_matrizes();
    } else if (strcmp(function_name, "verifica_matriz_triangular_superior") == 0) {
        verifica_matriz_triangular_superior();
    } else if (strcmp(function_name, "counting_sort") == 0) {
        counting_sort();
    } else if (strcmp(function_name, "transpoe_matriz") == 0) {
        transpoe_matriz();
    }

    return 0;
}