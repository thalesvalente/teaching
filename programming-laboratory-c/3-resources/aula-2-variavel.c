// Universidade Federal do Maranhão
// Departamento de Engenharia da Computação
// Author: Professor Doutor Thales Levi Azevedo Valente
// Description: Material de Ensino - Laboratório de Programação - Linguagem C
// Date: 01-10-2023

/*
Neste material de ensino, abordaremos os conceitos básicos e fundamentais da linguagem de programação C.
Os tópicos incluem declaração, inicialização, tipos de dados, modificadores de tipo, escopo de variáveis,
conversão de tipos, constantes, operadores (aritméticos, de comparação e binários), e muito mais.

A estrutura é a seguinte:

Estrutura:
1) Variáveis e tipos
    1.1) Declaração de variáveis
    1.2) Inicialização de variáveis
    1.3) Tipos de dados primitivos
    1.4) Conversão de tipos (casting)
    1.5) Modificadores de tipo
    1.6) Escopo de variáveis
    1.7) Constantes
2) Palavras reservadas
3) Atribuições de valor e expressão
4) Operadores
    4.1) Operadores Aritméticos
    4.2) Operadores de Comparação
    4.3) Operadores Binários

Cada seção do código abaixo está claramente marcada com comentários para indicar o início de cada tópico e sub-tópico.
*/


#include <stdio.h> // Incluir a biblioteca padrão de entrada e saída
#include <limits.h> // Para usar as constantes de limites
#include <float.h> // Para usar as constantes de limites de ponto flutuante


int main() { // Função principal

    // 1- Variáveis e Tipos
    // ====================
    // ##################################################################
    // 1.1- Declaração de variáveis
    // ==================================================================
    // Uma variável é um nome dado a uma área de armazenamento que nosso programa pode manipular.
    int idade; // Declaração de uma variável do tipo inteiro

    // As variáveis em C são case-sensitive, ou seja, "idade" e "Idade" seriam duas variáveis diferentes.
    int Idade; // Outra variável diferente de "idade"

    // Regras de Nomenclatura
    // - Deve começar com uma letra ou sublinhado (_)
    // - Pode conter letras, números e sublinhados
    int _idade;
    int idade2;

    // ##################################################################
    // 1.2- Inicialização de variáveis
    // ==================================================================
    // A declaração de variáveis em C sempre começa com um tipo de dado, 
    // seguido pelo nome da variável.
    int inteiro = 10; // Declarando uma variável do tipo inteiro
    float decimal = 3.14; // Declarando uma variável do tipo ponto flutuante
    char caractere = 'A'; // Declarando uma variável do tipo caractere
    
    printf("\n1.1- Declaração de variáveis\n");
    printf("---------------------------------------------------\n");
    // Exibindo os valores das variáveis
    printf("Valor do inteiro: %d\n", inteiro); // %d é usado para inteiros
    printf("Valor do decimal: %f\n", decimal); // %f é usado para ponto flutuante
    printf("Valor do caractere: %c\n", caractere); // %c é usado para caracteres

    // ##################################################################
    // 1.3- Tipos de Dados Primitivos
    // ==================================================================
    int numero = 10;

    printf("\n1.3- Tipos de Dados Primitivos\n");
    printf("---------------------------------------------------\n");
    printf("Tamanho de int: %lu bits\n", sizeof(int) * 8);
    printf("Faixa de valores int: %d to %d\n", INT_MIN, INT_MAX);

    float salario = 1234.56;
    printf("Tamanho de float: %lu bits\n", sizeof(float) * 8);
    printf("Faixa de valores float: %E to %E\n", FLT_MIN, FLT_MAX);

    char simbolo = 'C';
    printf("Tamanho de char: %lu bits\n", sizeof(char) * 8);

    // ##################################################################
    // 1.4- Modificadores de Tipo
    // ==================================================================
    printf("\n1.4- Modificadores de Tipo\n");
    printf("---------------------------------------------------\n");

    short int pequenoNumero = 32767;
    printf("Tamanho de short int: %lu bits\n", sizeof(short int) * 8);

    long int grandeNumero = 2147483647;
    printf("Tamanho de long int: %lu bits\n", sizeof(long int) * 8);

    unsigned int idadePositiva = 20;
    printf("Tamanho de unsigned int: %lu bits\n", sizeof(unsigned int) * 8);

    /*
    Tabela Comparativa de Tipos de Dados e Modificadores em C
    Nota: 
        - Use as funções sizeof() para obter o tamanho em bytes e multiplique por 8 para obter o tamanho em bits.
        - As constantes INT_MIN, INT_MAX, etc., são definidas em <limits.h> e <float.h>.
    */
    // Imprimindo os valores na tabela comparativa
    printf("Tipo de Dado\t\tModificador\t\tTamanho (bits)\tValor Mínimo\t\tValor Máximo\n");
    printf("---------------------------------------------------------------------------------------------------\n");
    printf("int\t\t\t(nenhum)\t\t%lu\t\t%d\t\t%d\n", sizeof(int) * 8, INT_MIN, INT_MAX);
    printf("int\t\t\tshort\t\t\t%lu\t\t%d\t\t\t%d\n", sizeof(short int) * 8, SHRT_MIN, SHRT_MAX);
    printf("int\t\t\tunsigned short\t\t%lu\t\t0\t\t\t%u\n", sizeof(unsigned short int) * 8, USHRT_MAX);
    printf("int\t\t\tlong\t\t\t%lu\t\t%ld\t\t%ld\n", sizeof(long int) * 8, LONG_MIN, LONG_MAX);
    printf("int\t\t\tunsigned long\t\t%lu\t\t0\t\t\t%lu\n", sizeof(unsigned long int) * 8, ULONG_MAX);
    printf("char\t\t\t(nenhum)\t\t%lu\t\t%d\t\t\t%d\n", sizeof(char) * 8, CHAR_MIN, CHAR_MAX);
    printf("char\t\t\tunsigned\t\t%lu\t\t0\t\t\t%u\n", sizeof(unsigned char) * 8, UCHAR_MAX);
    printf("double\t\t\t(nenhum)\t\t%lu\t\t%E\t\t%E\n", sizeof(double) * 8, DBL_MIN, DBL_MAX);
    printf("float\t\t\t(nenhum)\t\t%lu\t\t%E\t\t%E\n", sizeof(float) * 8, FLT_MIN, FLT_MAX);

    // ##################################################################
    // 1.5- Conversão de Tipos (Casting)
    // ==================================================================
    // Casting é o processo de conversão de um tipo de dado para outro.
    int total = 10;
    int contagem = 3;
    float media = (float)total / contagem;
    char convertido = (char)total; // Convertendo total para char
    printf("\n1.5- Conversão de Tipos (Casting)\n");
    printf("---------------------------------------------------\n");
    printf("Média como float: %f\n", media); // Imprimindo o valor convertido para float
    printf("Total como char: %c\n", convertido); // Imprimindo o valor convertido para char

    // ##################################################################
    // 1.6- Escopo de Variáveis
    // ==================================================================
    // O escopo de uma variável refere-se à parte do programa onde a variável pode ser acessada.
    // Variáveis declaradas dentro de funções são locais a essa função.
    // Variáveis declaradas fora de todas as funções são globais.

    // ##################################################################
    // 1.7- Constantes
    // ==================================================================
    const float PI = 3.14;
    const char GRAU = 'g';
    printf("\n1.7- Constantes\n");
    printf("---------------------------------------------------\n");
    printf("Constante PI: %f\n", PI); // Imprimindo o valor da constante PI
    printf("Constante GRAU: %c\n", GRAU); // Imprimindo o valor da constante GRAU
    
    // ##################################################################
    // 2- Palavras Reservadas
    // ==================================================================
    // Palavras reservadas são palavras que têm um significado especial para o compilador e não podem ser usadas para outros fins.
    // Exemplos: int, float, return, if, else, while, for, etc.
    
    // ##################################################################
    // 3- Atribuições de Valor e Expressão
    // ==================================================================
    printf("\n3- Atribuições de Valor e Expressão\n");
    printf("===================================================\n");
    unsigned int a = 5; // Atribuição de valor
    int b = 10;
    int c = a + b; // Atribuição de expressão (soma de a e b)
    
    // Exibindo o resultado da expressão
    printf("Resultado da soma de a e b: %d\n", c);
    
    // ##################################################################
    // 4- Operadores
    // ==================================================================
    printf("\n4- Operadores\n");
    printf("===================================================\n");
    int soma = a + b;
    int subtracao = a - b;
    int multiplicacao = a * b;
    float divisao = (float)a / (float)b; // Convertendo para float para obter resultado decimal
    
    // Exibindo os resultados das operações
    printf("Resultado da soma: %d\n", soma);
    printf("Resultado da subtracao: %d\n", subtracao);
    printf("Resultado da multiplicacao: %d\n", multiplicacao);
    printf("Resultado da divisao: %f\n", divisao);
    
    // Operadores de Comparação
    printf("\n4.1- Operadores de Comparação\n");
    printf("---------------------------------------------------\n");
    printf("a == b: %d\n", a == b);
    printf("a != b: %d\n", a != b);
    printf("a > b: %d\n", a > b);
    printf("a < b: %d\n", a < b);
    printf("a >= b: %d\n", a >= b);
    printf("a <= b: %d\n", a <= b);
    
    // Operadores Binários
    printf("\n4.2- Operadores Binários\n");
    printf("---------------------------------------------------\n");
    a = 5; // binário:  0101
    b = 10; // binário: 1010

    printf("a = 5, que é 0101 em binário\n");
    printf("b = 10, que é 1010 em binário\n\n");
    
    printf("a & b (AND): %d\n", a & b);
    printf("Explicação: 0101 AND 1010 é 0000, ou seja, 0 em decimal\n\n");
    
    printf("a | b (OR): %d\n", a | b);
    printf("Explicação: 0101 OR 1010 é 1111, ou seja, 15 em decimal\n\n");
    
    printf("a ^ b (XOR): %d\n", a ^ b);
    printf("Explicação: 0101 XOR 1010 é 1111, ou seja, 15 em decimal\n\n");
    
    /* No C, quando você faz a negação de um número, o compilador automaticamente trata o número como um número em complemento de dois se ele for negativo.
    Aqui está o que acontece:
    -Todos os bits de a são invertidos: ∼0101=1010.
    -O número resultante é tratado como um número em complemento de dois, então ele é interpretado como −6 em decimal.
    */
   unsigned int z = ~a;
    printf("~a (NOT): %lu\n", z);
    printf("Explicação: NOT 0101 é 1010, ou seja, -6 em decimal (complemento de dois)\n\n");
    
    printf("a << 1 (left shift): %d\n", a << 1);
    printf("Explicação: 0101 deslocado para a esquerda por 1 bit é 1010, ou seja, 10 em decimal\n\n");
    
    printf("a >> 1 (right shift): %d\n", a >> 1);
    printf("Explicação: 0101 deslocado para a direita por 1 bit é 0010, ou seja, 2 em decimal\n\n");

    

    return 0;
}
