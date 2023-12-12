#include <stdio.h>
#include <string.h>

// Protótipos das funções
// OBS. NÃO modifique a assinatura das funções (tipo retorno, nome, parâmetros).
// Apenas implemente o corpo delas trocando o ; por chaves
// 1 - O nome do arquivo OBRIGATORIAMENTE deve ser "nome_sobrenome1_sobrenome2.c". Arquivos diferentes serão desconsiderados.
// 2 - O arquivo deve conter APENAS as funções pedidas no enunciado.
// 3 - As saídas devem ser exatamente como especificadas nos enunciados. Saídas diferentes serão consideradas ERRADAS.
// 4 - Funções que não compilarão receberão nota ZERO para a função.
// 5 - Funções que apresentarem comportamento diferente do especificado nos enunciados serão consideradas ERRADAS.
// 6 - Arquivos que não compilarem receberão nota ZERO.
// 7 - Arquivos que não seguirem o padrão de nomeação receberão nota ZERO.
// 8 - Funções que entrarem em loop infinito ou travarem o computador receberão nota ZERO.

/*
Atividade 1: Verificação de Palíndromos
Contexto: Palíndromos são palavras ou frases que se leem da mesma forma tanto da esquerda para a direita 
quanto da direita para a esquerda. Eles são frequentemente usados em jogos de palavras, testes de lógica 
e em diversas aplicações de processamento de texto e dados.
Desafio: Implemente um programa que verifica se uma string fornecida pelo usuário é um palíndromo. 
O programa deve solicitar ao usuário uma string e, em seguida, verificar se ela é um palíndromo.
Use a função scanf para ler a string fornecida pelo usuário.
    // - Se a string for um palíndromo, exibir: "sim".
    // - Se não for um palíndromo, exibir: "nao".
    // O programa deve tratar a string de forma que a verificação seja feita independentemente de maiúsculas ou minúsculas, mas não é necessário considerar espaços ou caracteres especiais.
    // A verificação deve ser feita em um laço, analisando se cada caractere da primeira metade da string corresponde ao seu par na segunda metade.
*/
// Exemplo de uso:
// Entrada: "Level" ou "Palindromo"
// Saída: "sim" ou "nao"
// OBS. IMPRIMA SOMENTE "sim" OU "nao", NÃO IMPRIMA MENSAGENS.
void verificacao_de_palindromo() {
    char str[101];
    scanf("%100s", str);
    
    int len = strlen(str);
    for (int i = 0; i < len / 2; i++) {
        if (tolower(str[i]) != tolower(str[len - i - 1])) {
            printf("nao");
            return;
        }
    }
    printf("sim");
}

/*
Atividade 2: Encontrando o Segundo Maior Valor em um Vetor
Contexto: Em análise de dados, frequentemente encontramos a necessidade de classificar e comparar 
elementos em um conjunto. Encontrar o segundo maior valor em um conjunto de dados pode ser útil 
em situações onde o maior valor é uma anomalia (outlier) ou em competições onde os dois melhores 
resultados são premiados.
Desafio: Implemente um programa que encontra o segundo maior valor em um vetor de inteiros. O vetor 
deve ter 5 posições e os valores devem ser fornecidos pelo usuário através da função scanf.
    // - O programa deve ler 5 valores inteiros do usuário e armazená-los em um vetor.
    // - Em seguida, deve encontrar e exibir o segundo maior valor dentre os fornecidos.
    // - Considere que os valores podem não ser únicos e que o vetor pode conter valores repetidos.
    OBS. IMPRIMA SOMENTE O NÚMERO, NÃO IMPRIMA MENSAGENS.
*/

// Exemplo de uso:
// Entrada: 5 3 8 6 4
// Saída: 6
void segundo_maior_valor_vetor_inteiros() {
    int nums[5];
    for (int i = 0; i < 5; i++) {
        scanf("%d", &nums[i]);
    }

    int max = nums[0] > nums[1] ? nums[0] : nums[1];
    int second_max = nums[0] < nums[1] ? nums[0] : nums[1];

    for (int i = 2; i < 5; i++) {
        if (nums[i] > max) {
            second_max = max;
            max = nums[i];
        } else if (nums[i] > second_max && nums[i] != max) {
            second_max = nums[i];
        }
    }

    printf("%d", second_max);
}

/*
Atividade 3: Soma de Matrizes 3x3
Contexto: A soma de matrizes é uma operação fundamental na álgebra linear, utilizada em várias aplicações 
práticas como em gráficos computacionais, processamento de sinais e sistemas de controle.
Desafio: Implemente uma função que soma duas matrizes 3x3 pré-definidas e retorna o resultado. 
As matrizes são fornecidas no código, e você deve implementar a lógica para somá-las.
    // - ATENÇÃO! As matrizes para a soma estão definidas tal como está no enunciado.
    // - Implemente uma função que calcula a soma dessas duas matrizes.
    // - A função deve retornar uma nova matriz que é a soma das duas matrizes fornecidas.
    // OBS. IMPRIMA A SOMA TAL COMO ESTÁ NO ENUNCIADO EM "Saída esperada após a soma". I
    // OBS. IMPRIMA SOMENTE A MATRIZ RESULTANTE DA SOMA, NÃO IMPRIMA AS MATRIZES DE ENTRADA E NEM MENSAGENS.

Matrizes fornecidas:
Matriz A:
1 2 3
4 5 6
7 8 9

Matriz B:
9 8 7
6 5 4
3 2 1

Saída esperada após a soma:
10 10 10
10 10 10
10 10 10

Exemplo de declaração das matrizes no código:
void soma_matrizes() {
    int matrizA[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int matrizB[3][3] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
    int matrizSoma[3][3]; // Matriz para armazenar o resultado da soma

    // Aqui vai a lógica para somar as matrizes e armazenar o resultado em matrizSoma
    // ...

    // Imprimir matrizSoma
    // ...
}
*/
void soma_matrizes() {
    int matrizA[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int matrizB[3][3] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
    int matrizSoma[3][3];

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            matrizSoma[i][j] = matrizA[i][j] + matrizB[i][j];
            printf("%d ", matrizSoma[i][j]);
        }
        printf("\n");
    }
}

/*
Atividade: Verificação de Matriz Transposta de Si Mesma usando ponteiros
Contexto: Em álgebra linear, uma matriz que é igual à sua transposta é chamada de matriz simétrica. 
Este conceito é importante em várias áreas da matemática e engenharia. 
Desafio: Implemente uma função que verifica se uma matriz 3x3 fornecida é igual à sua transposta. 
A matriz é definida no código, e você deve implementar a lógica para verificar se a matriz é sua 
própria transposta. É proibido o uso de indexadores com [] nessa questão. Use somente ponteiros.
    // - As matrizes para verificação devem ser definidas no código.
    // - Implemente uma função que verifica se a matriz é igual à sua transposta.
    // - A função deve imprimir "sim" se a matriz for sua própria transposta, e "nao" caso contrário.
    // OBS. IMPRIMA SOMENTE "sim" OU "nao", NÃO IMPRIMA MENSAGENS.

Matriz fornecida para verificação:
Matriz A (Simétrica):
1 2 3
2 5 6
3 6 9

Matriz B (Não simétrica):
1 2 3
4 5 6
7 8 9

Exemplo de declaração das matrizes no código:
void verifica_matriz_simetrica() {
    int matrizA[3][3] = {{1, 2, 3}, {2, 5, 6}, {3, 6, 9}};
    int matrizB[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

    // Aqui vai a lógica para verificar se A é sua própria transposta e imprimir "sim" ou "nao"
}
*/
void verifica_matriz_simetrica() {
    int matrizA[3][3] = {{1, 2, 3}, {2, 5, 6}, {3, 6, 9}};
    int matrizB[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

    // Verifica se matrizA é simétrica
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < i; j++) {
            if (*( *(matrizA + i) + j) != *( *(matrizA + j) + i)) {
                printf("nao");
                return;
            }
        }
    }
    printf("sim");
}

// OBS. NÃO modifique a main
int main() {
    char function_name[100];
    scanf("%s", function_name);

    if (strcmp(function_name, "verificacao_de_palindromo") == 0) {
        verificacao_de_palindromo();
    } else if (strcmp(function_name, "segundo_maior_valor_vetor_inteiros") == 0) {
        segundo_maior_valor_vetor_inteiros();
    } else if (strcmp(function_name, "soma_matrizes()") == 0) {
        soma_matrizes();
    } else if (strcmp(function_name, "verifica_matriz_simetrica") == 0) {
        verifica_matriz_simetrica();
    }

    return 0;
}