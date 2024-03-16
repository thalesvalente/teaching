#include <stdio.h>
#include <string.h>
#include <math.h>

void soma_matrizes_3x3() {
    int A[3][3], B[3][3], C[3][3], i, j;

    // Lendo a Matriz A
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
            scanf("%d", *(A + i) + j);

    // Lendo a Matriz B
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
            scanf("%d", *(B + i) + j);

    // Somando as matrizes A e B e armazenando em C
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
            *(*(C + i) + j) = *(*(A + i) + j) + *(*(B + i) + j);

    // Imprimindo a Matriz C
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            printf("%d ", *(*(C + i) + j));
        }
        printf("\n");
    }
}

void transposicao_matriz_3x3() {
    int A[3][3], T[3][3], i, j;

    // Lendo a Matriz A
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
            scanf("%d", *(A + i) + j);

    // Transpondo a Matriz A em T
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
            *(*(T + j) + i) = *(*(A + i) + j);

    // Imprimindo a Matriz Transposta T
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            printf("%d ", *(*(T + i) + j));
        }
        printf("\n");
    }
}

void multiplicacao_matrizes_3x3() {
    int A[3][3], B[3][3], C[3][3], i, j, k;

    // Lendo a Matriz A
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
            scanf("%d", *(A + i) + j);

    // Lendo a Matriz B
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
            scanf("%d", *(B + i) + j);

    // Inicializando a Matriz C com zero
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
            *(*(C + i) + j) = 0;

    // Multiplicando as matrizes A e B e armazenando em C
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
            for (k = 0; k < 3; k++)
                *(*(C + i) + j) += *(*(A + i) + k) * *(*(B + k) + j);

    // Imprimindo a Matriz C
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            printf("%d ", *(*(C + i) + j));
        }
        printf("\n");
    }
}


void verifica_matriz_identidade_3x3() {
    int A[3][3], identidade = 1, i, j;

    // Lendo a Matriz A
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
            scanf("%d", *(A + i) + j);

    // Verificando se a Matriz A é identidade
    for (i = 0; i < 3 && identidade; i++)
        for (j = 0; j < 3; j++)
            if ((i == j && *(*(A + i) + j) != 1) || (i != j && *(*(A + i) + j) != 0)) {
                identidade = 0;
                break;
            }

    if (identidade)
        printf("Identidade\n");
    else
        printf("Nao Identidade\n");
}


void calculo_traco_matriz_3x3() {
    int A[3][3], traco = 0, i;

    // Lendo a Matriz A
    for (i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            scanf("%d", *(A + i) + j);

    // Calculando o traço da Matriz A
    for (i = 0; i < 3; i++)
        traco += *(*(A + i) + i);

    printf("%d\n", traco);
}

/* 
   Enunciado: Implemente uma função que processa sinais vitais usando uma rede neural com pesos pré-definidos e classifica a saída.
   Exemplo: 
   Entrada: 
   Sinais vitais: [70, 120, 98]
   Pesos: [[0.2, 0.8, -0.5], [0.7, 0.1, 0.3], [0.4, -0.2, 0.5]]
   Saída esperada nos comentários: 
   [0.88]
   [0.64]
   [0.62]
*/
void diagnostico_medico_assistido() {
    float sinais_vitais[3] = {70, 120, 98}; // Valores de exemplo
    float pesos[3][3] = {{0.2, 0.8, -0.5}, {0.7, 0.1, 0.3}, {0.4, -0.2, 0.5}};
    float resultado[3];
    int i, j;

    // Multiplica pesos por sinais vitais e aplica sigmoide
    for (i = 0; i < 3; i++) {
        *(resultado + i) = 0;
        for (j = 0; j < 3; j++) {
            *(resultado + i) += *(*(pesos + i) + j) * *(sinais_vitais + j);
        }
        *(resultado + i) = 1.0 / (1.0 + exp(-*(resultado + i)));
    }

    // Imprime os resultados esperados
    for (i = 0; i < 3; i++) {
        printf("[%.2f]\n", *(resultado + i));
    }
}



/* 
   Enunciado: Implemente uma função que simula as tensões em um circuito elétrico dadas as resistências e correntes.
   Exemplo: 
   Entrada: 
   Correntes: [0.5, 0.3, 0.4]
   Resistências: [[5, 0, 0], [0, 10, 0], [0, 0, 15]]
   Saída esperada nos comentários: 
   [2.50]
   [3.00]
   [6.00]
*/
void simulacao_circuito_eletrico() {
    float correntes[3] = {0.5, 0.3, 0.4}; // Valores de exemplo
    float resistencias[3][3] = {{5, 0, 0}, {0, 10, 0}, {0, 0, 15}};
    float tensoes[3];
    int i;

    // Calcula tensão para cada componente
    for (i = 0; i < 3; i++) {
        *(tensoes + i) = *(*(resistencias + i) + i) * *(correntes + i);
    }

    // Imprime os resultados esperados
    for (i = 0; i < 3; i++) {
        printf("[%.2f]\n", *(tensoes + i));
    }
}

/* 
   Enunciado: Implemente uma função que aplica transformações geométricas a um ponto no espaço.
   Exemplo: 
   Entrada: 
   Ponto: [1, 2, 3]
   Transformações: Rotação, Translação, Escala (matrizes fornecidas)
   Saída esperada nos comentários: 
   [4.00]
   [5.00]
   [6.00]
*/
void transformacoes_geometricas() {
    float ponto[3] = {1, 2, 3}; // Valores de exemplo
    float rotacao[3][3] = {{0, -1, 0}, {1, 0, 0}, {0, 0, 1}};
    float translacao[3][3] = {{1, 0, 1}, {0, 1, 1}, {0, 0, 1}};
    float escala[3][3] = {{2, 0, 0}, {0, 2, 0}, {0, 0, 2}};
    float temp[3], resultado[3];
    int i, j;

    // Aplica rotação
    for (i = 0; i < 3; i++) {
        *(temp + i) = 0;
        for (j = 0; j < 3; j++) {
            *(temp + i) += *(*(rotacao + i) + j) * *(ponto + j);
        }
    }

    // Aplica translação
    for (i = 0; i < 3; i++) {
        *(ponto + i) = *(temp + i) + *(*(translacao + i) + 2);
    }

    // Aplica escala
    for (i = 0; i < 3; i++) {
        *(resultado + i) = 0;
        for (j = 0; j < 3; j++) {
            *(resultado + i) += *(*(escala + i) + j) * *(ponto + j);
        }
    }

    // Imprime os resultados esperados
    for (i = 0; i < 3; i++) {
        printf("[%.2f]\n", *(resultado + i));
    }
}


// Função main
int main() {
    char function_name[100];
    scanf("%s", function_name);

    if (strcmp(function_name, "soma_matrizes_3x3") == 0) {
        soma_matrizes_3x3();
    } else if (strcmp(function_name, "transposicao_matriz_3x3") == 0) {
        transposicao_matriz_3x3();
    } else if (strcmp(function_name, "multiplicacao_matrizes_3x3") == 0) {
        multiplicacao_matrizes_3x3();
    } else if (strcmp(function_name, "verifica_matriz_identidade_3x3") == 0) {
        verifica_matriz_identidade_3x3();
    } else if (strcmp(function_name, "calculo_traco_matriz_3x3") == 0) {
        calculo_traco_matriz_3x3();
    } else if (strcmp(function_name, "diagnostico_medico_assistido") == 0) {
        diagnostico_medico_assistido();
    } else if (strcmp(function_name, "simulacao_circuito_eletrico") == 0) {
        simulacao_circuito_eletrico();
    } else if (strcmp(function_name, "transformacoes_geometricas") == 0) {
        transformacoes_geometricas();
    }

    return 0;
}