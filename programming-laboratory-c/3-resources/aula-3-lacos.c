// Universidade Federal do Maranhão
// Departamento de Engenharia da Computação
// Author: Professor Doutor Thales Levi Azevedo Valente
// Description: Material de Ensino - Laboratório de Programação - Linguagem C
// Date: 08-10-2023

/*
Neste material, exploraremos o conceito de laços de repetição na linguagem de programação C. 
Os laços de repetição são estruturas de controle que permitem executar um bloco de código várias vezes.

A capacidade de um programa repetir a execução de um bloco de código é fundamental para realizar tarefas como processamento de dados em série, operações matemáticas iterativas e testes automatizados.

Os principais tópicos abordados são:
1) Laço 'for'
2) Laço 'while'
3) Laço 'do...while'

Cada tópico será ilustrado com exemplos práticos relacionados à engenharia da computação e elétrica.
*/

#include <stdio.h>

int main() {
    // ########################   NIVEL 1   ##################################
    // 1- Laço 'for'
    // ==================================================================
    // O laço 'for' é utilizado quando se sabe quantas vezes um bloco de código deve ser repetido.
    printf("\n1- Laço 'for'\n");
    printf("---------------------------------------------------\n");

    // Contexto: Imprimir os primeiros 10 números naturais.
    for(int i = 1; i <= 10; i++) {
        printf("%d ", i);
    }
    printf("\n");

    // ##################################################################
    // 2- Laço 'while'
    // ==================================================================
    // O laço 'while' repete um bloco de código enquanto uma condição for verdadeira.
    printf("\n2- Laço 'while'\n");
    printf("---------------------------------------------------\n");

    // Contexto: Imprimir os números começando de 10 e decrescendo até 1.
    int j = 10;
    while(j >= 1) {
        printf("%d ", j);
        j--;
    }
    printf("\n");

    // ##################################################################
    // 3- Laço 'do...while'
    // ==================================================================
    // O laço 'do...while' é semelhante ao 'while', mas verifica a condição após a execução do bloco, garantindo que o bloco seja executado pelo menos uma vez.
    printf("\n3- Laço 'do...while'\n");
    printf("---------------------------------------------------\n");

    // Contexto: Solicitar ao usuário que insira um número. Continuar pedindo até que um número positivo seja inserido.
    float numero;
    do {
        printf("Insira um número positivo: ");
        scanf("%f", &numero);
    } while(numero <= 0);
    printf("Número positivo inserido: %.2f\n", numero);

    // ####################################################################
    // ########################   NIVEL 2   ###############################
    // ####################################################################

    // ##################################################################
    // 1- Laço 'for'
    // ==================================================================
    // O laço 'for' é útil quando sabemos de antemão quantas vezes queremos repetir uma ação.
    printf("\n1- Laço 'for'\n");
    printf("---------------------------------------------------\n");

    // Contexto: Imagine que você deseja acender e apagar um LED 10 vezes. Em vez de escrever o código de acender e apagar 10 vezes, podemos usar um laço.
    for(int i = 1; i <= 10; i++) {
        printf("LED aceso pela %dª vez.\n", i);
        printf("LED apagado.\n");
    }

    // ##################################################################
    // 2- Laço 'while'
    // ==================================================================
    // O laço 'while' é mais flexível e permite repetir uma ação enquanto uma condição for verdadeira.
    printf("\n2- Laço 'while'\n");
    printf("---------------------------------------------------\n");

    // Contexto: Suponha que você esteja carregando uma bateria e queira monitorá-la até que esteja completamente carregada.
    int cargaBateria = 0;
    while(cargaBateria < 100) {
        printf("Carregando... Bateria a %d%%.\n", cargaBateria);
        cargaBateria += 10; // Simulando o carregamento.
    }
    printf("Bateria completamente carregada!\n");

    // ##################################################################
    // 3- Laço 'do...while'
    // ==================================================================
    // O laço 'do...while' garante que o bloco de código seja executado pelo menos uma vez, independentemente da condição.
    printf("\n3- Laço 'do...while'\n");
    printf("---------------------------------------------------\n");

    // Contexto: Em um sistema de entrada, você deseja que o usuário insira uma senha, mas ele tem no máximo três tentativas.
    int tentativas = 0;
    int senhaCorreta = 1234;
    int senhaInserida;
    do {
        printf("Insira a senha: ");
        scanf("%d", &senhaInserida);
        tentativas++;
        if (senhaInserida == senhaCorreta) {
            printf("Acesso concedido!\n");
            break;
        } else if (tentativas < 3) {
            printf("Senha incorreta. Tente novamente.\n");
        }
    } while(tentativas < 3);

    if (senhaInserida != senhaCorreta) {
        printf("Acesso negado após 3 tentativas.\n");
    }
}