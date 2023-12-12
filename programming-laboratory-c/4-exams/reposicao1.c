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
Atividade 3: Verificador de Números Primos
Contexto: Um número perfeito é um número inteiro para o qual a soma de todos os seus divisores positivos, 
excluindo o próprio número, é igual ao próprio número. Por exemplo, 6 é um número perfeito porque 1 + 2 + 3 = 6.
- Objetivo: Implementar um programa que verifica se um número é um número perfeito.
- Entrada: O usuário fornece um número inteiro.
- Processamento:
.Calcule a soma de todos os divisores do número, exceto o próprio número.
- Saída: Indique se o número é perfeito ou não. A saída deve ser apenas "sim" ou "nao".
*/
void verificacao_de_numeros_perfeitos() {}


/*
Atividade 4: Calculadora de Fatorial
Contexto: O fatorial de um número inteiro não negativo é o produto de todos os inteiros positivos menores 
ou iguais a esse número. Por exemplo, o fatorial de 5 é 120 (5 * 4 * 3 * 2 * 1).
- Objetivo: Criar um programa que calcula o fatorial de um número fornecido pelo usuário.
- Entrada: O usuário insere um número inteiro não negativo.
- Processamento:
.Calcule o fatorial do número fornecido
.Trate o caso especial do fatorial de 0, que é 1.
- Saída: Exiba o fatorial do número. Imprima SOMENTE o fatorial.
*/
void calculadora_de_fatorial() {}

// OBS. NÃO modifique a main
int main() {
    char function_name[100];
    scanf("%s", function_name);

    if (strcmp(function_name, "gerador_de_sequencia_de_fibonacci_com_limite") == 0) {
        gerador_de_sequencia_de_fibonacci_com_limite();
    } else if (strcmp(function_name, "verificador_de_numeros_primos") == 0) {
        verificador_de_numeros_primos();
    } else if (strcmp(function_name, "verificacao_de_numeros_perfeitos") == 0) {
        verificacao_de_numeros_perfeitos();
    } else if (strcmp(function_name, "calculadora_de_fatorial") == 0) {
        calculadora_de_fatorial();
    }

    return 0;
}