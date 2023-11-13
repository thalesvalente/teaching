#include <stdio.h>
#include <string.h>
#include <math.h>

void media_vetor_inteiros() {
    int i, soma = 0;
    int vetor[3];

    for(i = 0; i < 3; i++) {
        scanf("%d", &vetor[i]);
        soma += vetor[i];
    }

    printf("%.2f\n", (float)soma/3);
}

void maximo_vetor_floats() {
    int i;
    float maximo;
    float vetor[3];

    for(i = 0; i < 3; i++) {
        scanf("%f", &vetor[i]);
        if(i == 0 || vetor[i] > maximo) {
            maximo = vetor[i];
        }
    }

    printf("%.2f\n", maximo);
}

void conta_numero_especifico() {
    int i, numero, contador = 0;
    int vetor[3];

    for(i = 0; i < 103; i++) {
        scanf("%d", &vetor[i]);
    }
    scanf("%d", &numero);

    for(i = 0; i < 3; i++) {
        if(vetor[i] == numero) {
            contador++;
        }
    }

    printf("%d\n", contador);
}

void soma_vetor_floats() {
    int i;
    float soma = 0, valor[3];
    for(i = 0; i < 3; i++) {
        scanf("%f", &valor[i]);
        soma += valor[i];
    }
    printf("%.2f\n", soma);
}

void inverte_vetor_inteiros() {
    int i, vetor[3];
    for(i = 0; i < 3; i++) {
        scanf("%d", &vetor[i]);
    }
    for(i = 2; i >= 0; i--) {
        printf("%d ", vetor[i]);
    }
    printf("\n");
}

void verifica_palindromo() {
    int i, vetor[10], flag = 1;
    for(i = 0; i < 10; i++) {
        scanf("%d", &vetor[i]);
    }
    for(i = 0; i < 5; i++) {
        if(vetor[i] != vetor[9 - i]) {
            flag = 0;
            break;
        }
    }
    if(flag) {
        printf("Palindromo\n");
    } else {
        printf("Nao Palindromo\n");
    }
}

void variancia_vetor_floats() {
    float vetor[5];
    float media = 0, variancia = 0;
    
    // Cálculo da média
    for (int i = 0; i < 5; i++) {
        scanf("%f", &vetor[i]);
        media += vetor[i];
    }
    media /= 5.0;

    // Cálculo da variância
    for (int i = 0; i < 5; i++) {
        variancia = variancia + pow((vetor[i] - media),2);
    }
    variancia /= 5.0;

    printf("%.2f\n", variancia);
}

void segundo_maior_valor_vetor_inteiros() {
    int vetor[5];
    int max1 = -100000, max2 = -100001;  // valores iniciais baixos
    for (int i = 0; i < 5; i++) {
        scanf("%d", &vetor[i]);
        if (vetor[i] > max1) {
            max2 = max1;
            max1 = vetor[i];
        } else if (vetor[i] > max2 && vetor[i] < max1) {
            max2 = vetor[i];
        }
    }
    printf("%d\n", max2);
}

void vetor_em_ordem_crescente() {
    int vetor[5];
    scanf("%d", &vetor[0]);
    int anterior = vetor[0];
    int ordemCrescente = 1;
    for (int i = 1; i < 5; i++) {
        scanf("%d", &vetor[i]);
        if (vetor[i] < anterior) {
            ordemCrescente = 0;
            break;
        }
        anterior = vetor[i];
    }
    if (ordemCrescente) {
        printf("Sim\n");
    } else {
        printf("Nao\n");
    }
}

void produto_escalar_vetores_floats() {
    float vetor1[3], vetor2[3];
    float produtoEscalar = 0;
    for (int i = 0; i < 3; i++) {
        scanf("%f", &vetor1[i]);
    }
    for (int i = 0; i < 3; i++) {
        scanf("%f", &vetor2[i]);
    }
    for (int i = 0; i < 3; i++) {
        produtoEscalar += vetor1[i] * vetor2[i];
    }
    printf("%.2f\n", produtoEscalar);
}

void classifica_fruta() {
    float caracteristicas[3], pesos[3];
    float saida = 0;

    // Leitura das características e dos pesos
    for (int i = 0; i < 3; i++) {
        scanf("%f", &caracteristicas[i]);
    }
    for (int i = 0; i < 3; i++) {
        scanf("%f", &pesos[i]);
        saida += caracteristicas[i] * pesos[i];
    }

    // Aplicação da função sigmoide
    saida = 1.0 / (1.0 + exp(-saida));

    // Classificação
    if (saida >= 0.5) {
        printf("Classe A\n");
    } else {
        printf("Classe B\n");
    }
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