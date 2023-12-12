#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// Protótipos das funções
// OBS. NÃO modifique a assinatura das funções (tipo retorno, nome, parâmetros).
// Apenas implemente o corpo delas trocando o ; por chaves

/*
Atividade 1: Gerador de Sequência de Fibonacci com Limite
Contexto: A Sequência de Fibonacci é uma série de números onde cada número é a soma dos dois anteriores. 
Ela tem aplicações em diversas áreas, incluindo ciência da computação, matemática e até arte.
- Objetivo: Escrever um programa que gera e exibe a Sequência de Fibonacci até um determinado valor limite.
- Entrada: O usuário deve fornecer um número inteiro que representa o valor limite da sequência.
- Processamento:
.Inicie com os dois primeiros números da sequência, a=0 e b=1.
.Utilize um laço para continuar a sequência, somando os dois últimos números para gerar o próximo.
.Pare o laço quando o próximo número da sequência for MAIOR QUE o valor limite fornecido. Para fazer isso, use a condição a <= limite.
(você pode testar a condição proximo < limite para ver a diferença, mas não irá dar a resposta correta)
- Saída: Exiba a sequência de Fibonacci até o limite fornecido. Os números devem ser separados por espaços.
*/
void gerador_de_sequencia_de_fibonacci_com_limite() {
    int limite, a = 0, b = 1, proximo = 0;
    //printf("Digite o valor limite para a sequência de Fibonacci: ");
    scanf("%d", &limite);

    while (a <= limite) {
        printf("%d ", a);
        proximo = a + b;
        a = b;
        b = proximo;
    }
    printf("\n");
}

/*
Atividade 2: Verificador de Números Primos
Contexto: Números primos são importantes em várias áreas da matemática e da ciência da computação, como na criptografia.
- Objetivo: Desenvolver um programa que verifica se um número fornecido pelo usuário é primo.
- Entrada: O usuário deve inserir um número inteiro.
- Processamento:
.Verifique se o número é divisível apenas por 1 e por ele mesmo.
.Para fazer isso, use um laço que tenta dividir o número por todos os inteiros entre 2 e a raiz quadrada do número.
.Se o número for divisível por qualquer um desses, ele não é primo.
- Saída: Informe se o número fornecido é primo ou não. A saída deve ser apenas "sim" ou "nao".
*/
void verificador_de_numeros_primos() {
    int numero, i, ehPrimo = 1;
    //printf("Digite um número para verificar se é primo: ");
    scanf("%d", &numero);

    if (numero < 2) {
        ehPrimo = 0;
    }

    for (i = 2; i <= sqrt(numero); ++i) {
        if (numero % i == 0) {
            ehPrimo = 0;
            break;
        }
    }

    if (ehPrimo) {
        printf("sim");
    } else {
        printf("nao");
    }
}

/*
Atividade 3: Verificador de Números Primos
Contexto: Um número perfeito é um número inteiro para o qual a soma de todos os seus divisores positivos, 
excluindo o próprio número, é igual ao próprio número. Por exemplo, 6 é um número perfeito porque 1 + 2 + 3 = 6.
- Objetivo: Implementar um programa que verifica se um número é um número perfeito.
- Entrada: O usuário fornece um número inteiro.
- Processamento:
.Calcule a soma de todos os divisores do número, exceto o próprio número. Um número é divisor de outro quando o resto (operador \%) da divisão é zero.
.Use um laço para encontrar todos os divisores, somando-os.
- Saída: Indique se o número é perfeito ou não. A saída deve ser apenas "sim" ou "nao".
*/
void verificacao_de_numeros_perfeitos() {
    int numero, soma = 0, i;
    //printf("Digite um número para verificar se é um número perfeito: ");
    scanf("%d", &numero);

    for (i = 1; i < numero; i++) {
        if (numero % i == 0) {
            soma += i;
        }
    }

    if (soma == numero) {
        printf("sim");
    } else {
        printf("nao");
    }
}


/*
Atividade 4: Calculadora de Fatorial
Contexto: O fatorial de um número inteiro não negativo é o produto de todos os inteiros positivos menores 
ou iguais a esse número. Por exemplo, o fatorial de 5 é 120 (5 * 4 * 3 * 2 * 1).
- Objetivo: Criar um programa que calcula o fatorial de um número fornecido pelo usuário.
- Entrada: O usuário insere um número inteiro não negativo.
- Processamento:
.Calcule o fatorial multiplicando todos os números inteiros de 1 até o número fornecido.
.Trate o caso especial do fatorial de 0, que é 1.
- Saída: Exiba o fatorial do número. Imprima SOMENTE o número.
*/
void calculadora_de_fatorial() {
    int numero, i;
    unsigned long long fatorial;
    //printf("Digite um número para calcular o fatorial: ");
    scanf("%d", &numero);

    if (numero == 0) {
        fatorial = 1;
    } else {
        for (i = 1; i <= numero; ++i) {
            fatorial *= i;
        }
        printf("%d", fatorial);
    }
}

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