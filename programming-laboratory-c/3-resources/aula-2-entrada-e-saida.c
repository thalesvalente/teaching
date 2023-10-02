// Universidade Federal do Maranhão
// Departamento de Engenharia da Computação
// Author: Professor Doutor Thales Levi Azevedo Valente
// Description: Material de Ensino - Laboratório de Programação - Linguagem C
// Date: 01-10-2023

// Este material é uma introdução abrangente às funções de entrada e saída em C, 
// focando principalmente nas funções printf e scanf. O objetivo é fornecer um 
// entendimento claro e conciso de como essas funções são usadas para exibir 
// saídas e receber entradas do usuário, respectivamente.

// A função printf é explorada com vários especificadores de formato que permitem 
// a impressão de diferentes tipos de dados, como inteiros, floats, caracteres e strings, 
// bem como em formatos específicos, como hexadecimal e notação científica.

// A função scanf é detalhada com ênfase no uso correto dos especificadores de formato e 
// na captura eficiente de diferentes tipos de dados de entrada do usuário.

// A seção de demonstração inclui um código de exemplo completo que ilustra o uso prático 
// de printf e scanf, demonstrando como eles podem ser usados para interagir com o usuário, 
// exibindo mensagens informativas e capturando entradas de usuário de várias formas.

// Estrutura:
// 1) Demonstração de printf - Exemplos de uso da função printf com diferentes especificadores de formato.
// 2) Demonstração de scanf - Exemplos de uso da função scanf para capturar entrada do usuário.
// 3) Código de Exemplo - Um código de exemplo completo mostrando printf e scanf em ação.

// O material a seguir deve fornecer uma base sólida para a compreensão da entrada e saída 
// em C, permitindo uma aplicação prática eficiente desses conceitos em programação C.

// Inicie o código abaixo para começar a exploração.

#include <stdio.h>

int main() {
    // 1) Demonstração de printf
    // =========================
    printf("\n1) Demonstração de printf\n");
    printf("=========================\n");
    
    int i = 10;
    float f = 3.14;
    char c = 'A';
    char s[] = "Olá, mundo!";
    
    printf("Inteiro: %d\n", i); // %d é usado para inteiros
    printf("Ponto flutuante: %f\n", f); // %f é usado para float
    printf("Caractere: %c\n", c); // %c é usado para char
    printf("String: %s\n", s); // %s é usado para strings
    printf("Hexadecimal: %x\n", i); // %x é usado para representação hexadecimal
    printf("Científico: %e\n", f); // %e é usado para notação científica
    
    // 2) Demonstração de scanf
    // ========================
    printf("\n2) Demonstração de scanf\n");
    printf("=========================\n");
    
    printf("Digite um inteiro: ");
    scanf("%d", &i); // %d é usado para inteiros
    
    printf("Digite um float: ");
    scanf("%f", &f); // %f é usado para float
    
    printf("Digite um caractere: ");
    scanf(" %c", &c); // %c é usado para char, note o espaço antes do %c para consumir o último Enter
    
    char str[50];
    printf("Digite uma string: ");
    scanf("%s", str); // %s é usado para strings
    
    // 3) Código de Exemplo
    // ====================
    printf("\n3) Você digitou:\n");
    printf("===================\n");
    printf("Inteiro: %d\n", i);
    printf("Float: %f\n", f);
    printf("Caractere: %c\n", c);
    printf("String: %s\n", str);
    
    return 0;
}