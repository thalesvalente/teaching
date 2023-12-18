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
Atividade 1: Gerador de Sequência de Fibonacci com Limite
Contexto: A Sequência de Fibonacci é uma série de números onde cada número é a soma dos dois anteriores. 
Ela tem aplicações em diversas áreas, incluindo ciência da computação, matemática e até arte.
- Objetivo: Escrever um programa que gera e exibe a Sequência de Fibonacci até um determinado valor limite.
- Entrada: O usuário deve fornecer um número inteiro que representa o valor limite da sequência.
- Processamento:
.Inicie com os dois primeiros números da sequência, a=0 e b=1.
.Utilize um laço para continuar a sequência, somando os dois últimos números para gerar o próximo.
.Pare o laço quando o próximo número da sequência for MAIOR QUE o valor limite fornecido. 
- Saída: Exiba a sequência de Fibonacci até o limite fornecido. Os números devem ser separados por espaços.
*/
void gerador_de_sequencia_de_fibonacci_com_limite() {}

/*
Atividade 2: Verificador de Números Primos
Contexto: Números primos são importantes em várias áreas da matemática e da ciência da computação, como na criptografia.
- Objetivo: Desenvolver um programa que verifica se um número fornecido pelo usuário é primo.
- Entrada: O usuário deve inserir um número inteiro.
- Processamento:
.Verifique se o número é divisível apenas por 1 e por ele mesmo.
.Para verificar isso, use um laço que tenta dividir o número por todos os inteiros entre 2 e a raiz quadrada do número.
- Saída: Informe se o número fornecido é primo ou não. A saída deve ser apenas "sim" ou "nao".
*/
void verificador_de_numeros_primos() {}


/*
Atividade 3: Multiplicação de Matrizes 3x3
Contexto: A multiplicação de matrizes é uma operação fundamental na álgebra linear, com aplicações em diversas áreas, como física, engenharia e economia.
- Objetivo: Implementar um programa que calcula o produto de duas matrizes 3x3 fornecidas pelo usuário.
- Entrada: O usuário deve fornecer os elementos de duas matrizes 3x3.
- Processamento:
    . Leia os elementos das duas matrizes usando scanf.
    . Calcule o produto das matrizes. Para cada elemento C[i][j] da matriz resultante, some os produtos dos elementos correspondentes da linha i da primeira matriz pelos elementos da coluna j da segunda matriz.
- Saída: Exiba a matriz resultante da multiplicação, formatando a saída em linhas e colunas.
*/
void multiplica_matrizes(){}


/*
Atividade 4: Redes Neurais MLP
Contexto: Um Multilayer Perceptron (MLP) é uma rede neural artificial básica que consiste em camadas de neurônios com pesos sinápticos. 
Cada neurônio recebe um conjunto de entradas (features), multiplica por seus pesos e aplica uma função de ativação. 
Desafio: Implemente uma função que simula a geração de saída de uma MLP básica com uma camada oculta, dado um vetor de características como entrada.
    // - A rede deve ter um vetor de entrada (features) com 2 elementos, uma camada oculta com 2 neurônios e uma camada de saída com 1 neurônio.
    // - Os pesos das conexões entre a entrada e a camada oculta devem ser armazenados em uma matriz de pesos 2x2
    // - Os pesos das conexões entre a camada oculta e a camada de saída devem ser armazenados em um vetor de pesos 1x2
    // - Implemente uma função de ativação sigmóide e aplique na saída de cada neurônio.
    // - A função deve ler o vetor de entrada do usuário, multiplicar pelos pesos, aplicar a função de ativação e calcular a saída da rede.
    // - Exiba a saída calculada pela rede.

Instruções adicionais:
    Passo 0 - 
        Inicialize os pesos das conexões entre a entrada e a camada oculta (use os valores {0.5, 0.5} e {0.4, 0.6})
        Inicialize os pesos das conexões entre a camada oculta e a camada de saída (use os valores {0.7, 0.3})
    Passo 1 -
        Faça a alocação dinâmica do vetor de entrada para ser um vetor de 2 posições
        Leia os valores dos neurônios de entrada como float
    Passo 2 - Calcule a saída da camada oculta
        A saída de cada neurônio da camada oculta deve ser calculada como a soma ponderada das entradas, seguida pela aplicação da função sigmoide.
        Ou seja, para cada neurônio da camada oculta, faça a soma ponderada das entradas
            for externo para percorrer a camada oculta e for interno para percorrer nos neurônios da entrada
        Aplique a sigmoide que você implementou em cada saída calculada, ou cada neurônio da camada oculta
    Passo 3 - Calcule a saída final
        A saída final da rede é calculada a partir dos outputs da camada oculta.
        Ou seja, a saída final deve ser calculada como a soma ponderada da saida oculta. 
            Pondere usando pesos da saida oculta. 
            Por fim, aplique a função sigmóide (que você implementou) na saída final.
    Passo 4 - Exiba a saída final da rede como float com duas casas decimais
    OBS. IMPRIMA APENAS A SAÍDA. 
    OBS. QUALQUER DÚVIDA TIRE COM O PROFESSOR EM SALA
*/
//crie a função sigmoid aqui recebendo um double e retornando um double
//a formula é 1/(1 + exp(-valor_recebido))


void multilayer_perceptron(){
    // Inicialização dos vetores e matrizes
    double *entrada; // Vetor de entrada (features) com 2 elementos
    double pesos_entrada_oculta[2][2]; /* inicialização dos pesos */  // Matriz de pesos das conexões entre a entrada e a camada oculta (2 neurônios x 2 entradas)
    double pesos_oculta_saida[2]; /* inicialização dos pesos */  // pesos das conexões entre a camada oculta e a camada de saída (1 neurônio x 2 entradas da camada oculta)
    double saida_oculta[2]; // Saída da camada oculta
    double saida_final;  // Saída final da rede
}


// OBS. NÃO modifique a main
int main() {
    char function_name[100];
    scanf("%s", function_name);

    if (strcmp(function_name, "gerador_de_sequencia_de_fibonacci_com_limite") == 0) {
        gerador_de_sequencia_de_fibonacci_com_limite();
    } else if (strcmp(function_name, "verificador_de_numeros_primos") == 0) {
        verificador_de_numeros_primos();
    } else if (strcmp(function_name, "multiplica_matrizes") == 0) {
        multiplica_matrizes();
    } else if (strcmp(function_name, "multilayer_perceptron") == 0) {
        multilayer_perceptron();
    }

    return 0;
}