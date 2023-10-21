/**************************************************************************
*                                                                         *
*           Universidade Federal do Maranhão                              *
*       Departamento de Engenharia da Computação                          *
*                                                                         *
*  Author: Professor Doutor Thales Levi Azevedo Valente                  *
*                                                                         *
*  Description: Material de Ensino - Laboratório de Programação C         *
*                                                                         *
*  Date: 16-10-2023                                                       *
*                                                                         *
* Este material fornece uma introdução abrangente às funções de entrada   *
* e saída em C, com foco nas funções printf, scanf, desvios condicionais *
* e o início de funções. Ele explora a                                    *
* utilização de especificadores de formato para diferentes tipos de      *
* dados, bem como técnicas de captura de entrada.                         *
*                                                                         *
* Conteúdos do Material:                                                  *
*   1. Demonstração de printf                                            *
*   2. Demonstração de scanf                                              *
*   3. Operadores                                                         *
*   4. Desvios Condicionais                                                *
*   5. Laços de Repetição                                                 *
*   6. Código de Exemplo                                                  *
*                                                                         *
* Inicie o código abaixo para começar a exploração.                       *
*                                                                         *
***************************************************************************
* -------------------------------------------------------------------------*
*   IMPORTANTE:                                                           *
*   1- NÃO modifique a assinatura das funções (tipo retorno, nome, parâm.)*
*   2- Apenas implemente o corpo das funções trocando o ; por chaves      *
*   3- NÃO modifique a main                                               *
*   4- Veja o arquivo "exemplo.c"                                         *
*   5- Use printf APENAS para imprimir o resultado                        *
*   6- CUIDADO ao usar o scanf                                            *
* -------------------------------------------------------------------------*
*                                                                         *
* Inicie o código abaixo para começar a exploração.                       *
*                                                                         *
***************************************************************************/


#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

// Protótipos das funções
// OBS. NÃO modifique a assinatura das funções (tipo retorno, nome, parâmetros).
// Apenas implemente o corpo delas trocando o ; por chaves
void monitoramento_continuo_de_tensao() {
    char continuar = 'y';
    float tensao;

    while (continuar != 'q') {
        scanf("%f", &tensao);

        if (tensao < 3.5) {
            printf("Baixa\n");
        } else if (tensao >= 3.5 && tensao <= 4.2) {
            printf("Media\n");
        } else {
            printf("Alta\n");
        }

        //printf("Pressione 'q' para sair ou qualquer outra tecla para continuar: ");
        scanf(" %c", &continuar);
    }
}

void analise_de_frequencias_em_um_espectro() {
    for (int i = 0; i <= 90; i += 10) {
        printf("Analisando faixa de %dGHz a %dGHz: ", i, i + 10);
        if (i < 10) {
            printf("Comunicacao movel\n");
        } else if (i < 20) {
            printf("Satelite\n");
        } else if (i < 30) {
            printf("Radar\n");
        } else if (i < 40) {
            printf("Comunicacao por fibra otica\n");
        } else if (i < 50) {
            printf("Wi-Fi\n");
        } else if (i < 60) {
            printf("Radiodifusao\n");
        } else if (i < 70) {
            printf("Pesquisa astronomica\n");
        } else if (i < 80) {
            printf("Medicina e imagiologia\n");
        } else if (i < 90) {
            printf("Comunicacoes militares\n");
        } else {
            printf("Pesquisa cientifica\n");
        }
    }
}

void simulacao_simplificada_de_um_osciloscopio() {
    int frequencia;
    scanf("%d", &frequencia);

    if (frequencia <= 5) {
        printf("-------\n");  // Linha reta
    } else {
        printf("/\\/\\/\n"); // Onda senoidal
    }
}

void medicao_iterativa_de_resistencia_em_um_circuito() {
    float resistencia, total = 0, media, maior_resistencia = 0, menor_resistencia = 1000000;  // assumindo um valor inicial alto para menor_resistencia

    for (int i = 0; i < 5; i++) {
        //printf("Digite o valor da resistência na medição %d (em Ohms): ", i + 1);
        scanf("%f", &resistencia);
        total += resistencia;
        if (resistencia > maior_resistencia) {
            maior_resistencia = resistencia;
        }
        if (resistencia < menor_resistencia) {
            menor_resistencia = resistencia;
        }
    }

    media = total / 5;
    //printf("Média das resistências: %.2f Ohms\n", media);
    printf("%.2f\n", media);
    if ((maior_resistencia - menor_resistencia) > 0.05 * media) {
        printf("Alerta! Possivel instabilidade do resistor detectada.\n");
    }
}

void monitoramento_de_faixas_de_frequencia() {
    int frequencia;
    char continuar = 'y';

    while (continuar != 'n') {
        //printf("Digite uma frequência em MHz: ");
        scanf("%d", &frequencia);

        if (frequencia >= 88 && frequencia <= 108) {
            printf("Radio FM\n");
        } else if (frequencia >= 2400 && frequencia <= 2500) {
            printf("Wi-Fi\n");
        } else if (frequencia == 1575) {
            printf("GPS\n");
        } else {
            printf("Frequencia nao corresponde a nenhum servico conhecido.\n");
        }

        //printf("Deseja continuar? (y/n): ");
        scanf(" %c", &continuar);
    }
}

void treinamento_iterativo_de_um_neuronio_artificial() {
    srand(time(0));
    float peso = 0.5;
    float erro;

    //printf("Peso inicial: %.2f\n", peso);
    do {
        //printf("Digite o valor do erro (-1 a 1, ou -999 para sair): ");
        scanf("%f", &erro);

        if (erro != -999) {
            peso -= erro;
            //printf("Novo peso: %.2f\n", peso);
        }

    } while (erro != -999);
    printf("%.2f\n", peso);
}

void analise_de_sequencias_logicas() {
    int valor1, valor2, valor3;
    //printf("Digite o primeiro valor lógico (0 ou 1): ");
    scanf("%d", &valor1);
    //printf("Digite o segundo valor lógico (0 ou 1): ");
    scanf("%d", &valor2);
    //printf("Digite o terceiro valor lógico (0 ou 1): ");
    scanf("%d", &valor3);

    if (valor1 == valor2 && valor2 == valor3) {
        if (valor1 == 0) {
            printf("Todos os valores sao 0\n");
        } else {
            printf("Todos os valores sao 1\n");
        }
    } else {
        printf("Os valores sao uma mistura de 0 e 1\n");
    }
}

void processamento_iterativo_de_sinais() {
    int numLeituras;
    float valor, soma = 0;

    //printf("Quantas leituras de sinal você deseja fazer? ");
    scanf("%d", &numLeituras);

    for (int i = 0; i < numLeituras; i++) {
        //printf("Digite o valor da leitura %d: ", i+1);
        scanf("%f", &valor);
        soma += valor;
    }

    //printf("Média dos valores: %.2f\n", soma / numLeituras);
    printf("%.2f\n", soma / numLeituras);
}

void catalogacao_automatizada_de_componentes() {
    int codigo;

    //printf("Digite um código numérico (1 a 5): ");
    scanf("%d", &codigo);

    switch (codigo) {
        case 1:
            printf("Resistor\n");
            break;
        case 2:
            printf("Capacitor\n");
            break;
        case 3:
            printf("Indutor\n");
            break;
        case 4:
            printf("Transistor\n");
            break;
        case 5:
            printf("Diodo\n");
            break;
        default:
            printf("Codigo invalido!\n");
    }
}

void classificacao_iterativa_de_dados() {
    int numValores;
    float valor;

    //printf("Quantos valores você deseja classificar? ");
    scanf("%d", &numValores);

    for (int i = 0; i < numValores; i++) {
        //printf("Digite o valor %d (0 a 10): ", i+1);
        scanf("%f", &valor);

        if (valor >= 0 && valor <= 3.99) {
            printf("Baixo\n");
        } else if (valor >= 4 && valor <= 6.99) {
            printf("Medio\n");
        } else if (valor >= 7 && valor <= 10) {
            printf("Alto\n");
        } else {
            printf("Valor invalido!\n");
        }
    }
}

// OBS. NÃO modifique a main
int main() {
    char function_name[100];
    scanf("%s", function_name);

    if (strcmp(function_name, "monitoramento_continuo_de_tensao") == 0) {
        monitoramento_continuo_de_tensao();
    } else if (strcmp(function_name, "analise_de_frequencias_em_um_espectro") == 0) {
        analise_de_frequencias_em_um_espectro();
    } else if (strcmp(function_name, "simulacao_simplificada_de_um_osciloscopio") == 0) {
        simulacao_simplificada_de_um_osciloscopio();
    } else if (strcmp(function_name, "medicao_iterativa_de_resistencia_em_um_circuito") == 0) {
        medicao_iterativa_de_resistencia_em_um_circuito();
    } else if (strcmp(function_name, "monitoramento_de_faixas_de_frequencia") == 0) {
        monitoramento_de_faixas_de_frequencia();
    } else if (strcmp(function_name, "treinamento_iterativo_de_um_neuronio_artificial") == 0) {
        treinamento_iterativo_de_um_neuronio_artificial();
    } else if (strcmp(function_name, "analise_de_sequencias_logicas") == 0) {
        analise_de_sequencias_logicas();
    } else if (strcmp(function_name, "processamento_iterativo_de_sinais") == 0) {
        processamento_iterativo_de_sinais();
    } else if (strcmp(function_name, "catalogacao_automatizada_de_componentes") == 0) {
        catalogacao_automatizada_de_componentes();
    } else if (strcmp(function_name, "classificacao_iterativa_de_dados") == 0) {
        classificacao_iterativa_de_dados();
    }

    return 0;
}