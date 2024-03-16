#include <stdio.h>
#include <string.h>
#include <math.h>
#include <limits.h>

void media_vetor_inteiros() {
    int vetor[3];
    int soma = 0;
    int *ptr;

    for (ptr = vetor; ptr < vetor + 3; ptr++) {
        scanf("%d", ptr);
        soma += *ptr;
    }

    printf("%.2f\n", (float)soma / 3);
}

void maximo_vetor_floats() {
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

void conta_numero_especifico() {
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

void soma_vetor_floats() {
    float soma = 0, valor;
    int i;

    for (i = 0; i < 3; i++) {
        scanf("%f", &valor);
        soma += valor;
    }

    printf("%.2f\n", soma);
}

void inverte_vetor_inteiros() {
    int vetor[3];
    int *ptr;

    for (ptr = vetor; ptr < vetor + 3; ptr++) {
        scanf("%d", ptr);
    }

    for (ptr = vetor + 2; ptr >= vetor; ptr--) {
        printf("%d ", *ptr);
    }
    printf("\n");
}

void verifica_palindromo() {
    int vetor[10];
    int *ptr1, *ptr2;
    int flag = 1;

    for (ptr1 = vetor; ptr1 < vetor + 10; ptr1++) {
        scanf("%d", ptr1);
    }

    ptr1 = vetor;
    ptr2 = vetor + 9;

    while (ptr1 < ptr2) {
        if (*ptr1 != *ptr2) {
            flag = 0;
            break;
        }
        ptr1++;
        ptr2--;
    }

    printf(flag ? "Palindromo\n" : "Nao Palindromo\n");
}

void variancia_vetor_floats() {
    float vetor[5];
    float media = 0, variancia = 0;
    float *ptr;

    for (ptr = vetor; ptr < vetor + 5; ptr++) {
        scanf("%f", ptr);
        media += *ptr;
    }
    media /= 5.0;

    for (ptr = vetor; ptr < vetor + 5; ptr++) {
        variancia += pow((*ptr - media), 2);
    }
    variancia /= 5.0;

    printf("%.2f\n", variancia);
}

void segundo_maior_valor_vetor_inteiros() {
    int vetor[5];
    int max1 = -100000, max2 = -100001;  // valores iniciais baixos
    int *ptr;

    for (ptr = vetor; ptr < vetor + 5; ptr++) {
        scanf("%d", ptr);
        if (*ptr > max1) {
            max2 = max1;
            max1 = *ptr;
        } else if (*ptr > max2 && *ptr < max1) {
            max2 = *ptr;
        }
    }
    printf("%d\n", max2);
}

void vetor_em_ordem_crescente() {
    int vetor[5];
    int *ptr, anterior = INT_MIN;
    int ordemCrescente = 1;

    for (ptr = vetor; ptr < vetor + 5; ptr++) {
        scanf("%d", ptr);
        if (*ptr < anterior) {
            ordemCrescente = 0;
            break;
        }
        anterior = *ptr;
    }

    printf(ordemCrescente ? "Sim\n" : "Nao\n");
}

void produto_escalar_vetores_floats() {
    float vetor1[3], vetor2[3];
    float *ptr1, *ptr2;
    float produtoEscalar = 0;

    for (ptr1 = vetor1; ptr1 < vetor1 + 3; ptr1++) {
        scanf("%f", ptr1);
    }

    for (ptr2 = vetor2; ptr2 < vetor2 + 3; ptr2++) {
        scanf("%f", ptr2);
    }

    for (ptr1 = vetor1, ptr2 = vetor2; ptr1 < vetor1 + 3; ptr1++, ptr2++) {
        produtoEscalar += *ptr1 * *ptr2;
    }

    printf("%.2f\n", produtoEscalar);
}

void classifica_fruta() {
    float caracteristicas[3], pesos[3];
    float *ptr_car, *ptr_pesos;
    float saida = 0;

    for (ptr_car = caracteristicas; ptr_car < caracteristicas + 3; ptr_car++) {
        scanf("%f", ptr_car);
    }

    for (ptr_pesos = pesos; ptr_pesos < pesos + 3; ptr_pesos++) {
        scanf("%f", ptr_pesos);
        saida += *ptr_car * *ptr_pesos;
    }

    saida = 1.0 / (1.0 + exp(-saida));

    printf(saida >= 0.5 ? "Classe A\n" : "Classe B\n");
}

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
