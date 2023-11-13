#include <stdio.h>
#include <string.h>

// Protótipos das funções

// Inverta a string fornecida e retorne a saída.
void inversao_de_strings() {
    char str[100];
    int length;
    scanf("%s", str);
    length = strlen(str);
    for(int i = length - 1; i >= 0; i--) {
        printf("%c", str[i]);
    }
    printf("\n");
}

// Conte o número de vogais na string fornecida.
void contagem_de_vogais() {
    char str[100];
    int count = 0;
    scanf("%s", str);
    for(int i = 0; i < strlen(str); i++) {
        if(str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u' ||
           str[i] == 'A' || str[i] == 'E' || str[i] == 'I' || str[i] == 'O' || str[i] == 'U') {
            count++;
        }
    }
    printf("%d\n", count);
}

// Converta todos os caracteres da string fornecida em maiúsculas.
void transformacao_para_maiusculas() {
    char str[100];
    scanf("%s", str);
    for(int i = 0; i < strlen(str); i++) {
        if(str[i] >= 'a' && str[i] <= 'z') {
            str[i] = str[i] - 32;
        }
    }
    printf("%s\n", str);
}

// Verifique se a string fornecida é um palíndromo.
void verificacao_de_palindromo() {
    char str[100], reversed[100];
    int flag = 1;
    scanf("%s", str);
    int length = strlen(str);
    for(int i = 0; i < length; i++) {
        reversed[i] = str[length - i - 1];
    }
    reversed[length] = '\0';

    for(int i = 0; i < length; i++) {
        if(reversed[i] != str[i]) {
            flag = 0;
            break;
        }
    }
    if(flag) {
        printf("E um palindromo\n");
    } else {
        printf("Nao e um palindromo\n");
    }
}

// Conte o número de palavras na string fornecida.
void contagem_de_palavras() {
    char str[200];
    int count = 1;
    scanf(" %[^\n]", str);
    for(int i = 0; i < strlen(str); i++) {
        if(str[i] == ' ') {
            count++;
        }
    }
    printf("%d\n", count);
}


// Converta a primeira letra de cada palavra na string fornecida em maiúsculas.
void capitalize() {
    char str[200];
    scanf(" %[^\n]", str);
    if(str[0] >= 'a' && str[0] <= 'z') {
        str[0] = str[0] - 32;
    }
    for(int i = 1; i < strlen(str); i++) {
        if(str[i - 1] == ' ' && (str[i] >= 'a' && str[i] <= 'z')) {
            str[i] = str[i] - 32;
        }
    }
    printf("%s\n", str);
}

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
