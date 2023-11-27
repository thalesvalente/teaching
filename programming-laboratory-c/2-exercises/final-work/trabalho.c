/**************************************************************************
*                                                                         *
*           Universidade Federal do Maranhão                              *
*       Departamento de Engenharia da Computação                          *
*                                                                         *
*  Author: Prof. Dr. Thales Levi Azevedo Valente                           *
*                                                                         *
*  Description: Processamento de Imagens em C                              *
*                                                                         *
*  Date: 27-11-2023                                                       *
*                                                                         *
* Este material fornece um programa simples para processamento de imagens *
* em C, incluindo filtros como negativo, escala de cinza, blur e Sobel.    *
*                                                                         *
* Conteúdos do Material:                                                  *
*   1. Carregamento de uma imagem em C                                    *
*   2. Aplicação de filtros: negativo, escala de cinza, blur e Sobel       *
*   3. Salvamento da imagem processada                                    *
*   4. Manipulação de Dados e Ponteiros                                   *
*   5. Criação de Menu                                                   *
*                                                                         *
***************************************************************************
* -------------------------------------------------------------------------*
*   IMPORTANTE:                                                           *
*   1- NÃO modifique a assinatura das funções (tipo retorno, nome, parâm.)*
*   2- Apenas implemente o corpo das funções trocando o ; por chaves      *
*   3- NÃO modifique a main                                               *
*   4- Veja o arquivo "exemplo.c"                                         *
*   5- NOME DO ARQUIVO É "NOME_SOBRENOME1_SOBRENOME2"                     *
* -------------------------------------------------------------------------*
*                                                                         *
* Inicie o código abaixo para começar a exploração.                       *
*                                                                         *
***************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"

void applyNegativeFilter(unsigned char *img, int width, int height, int channels);
void applyGrayScaleFilter(unsigned char *img, int width, int height, int channels);
void applyBlurFilter(unsigned char *img, int width, int height, int channels);
void applySobelFilter(unsigned char *img, int width, int height, int channels);
void saveImage(const unsigned char *img, int width, int height, int channels, const char *outputFileName);

int main() {
    int width, height, channels;
    char inputFile[100] = "Y:\\eng\\input.jpg";
    char outputFileName[100];


    // Carregar a imagem
    unsigned char *img = stbi_load(inputFile, &width, &height, &channels, 0);
    if (img == NULL) {
        fprintf(stderr, "Erro ao carregar a imagem.\n");
        return 1;
    }

    int choice;
    printf("Escolha o filtro a ser aplicado:\n");
    printf("1: Negativo\n");
    printf("2: Escala de Cinza\n");
    printf("3: Blur\n");
    printf("4: Sobel\n");
    printf("Digite sua escolha: ");
    scanf("%d", &choice);

    switch(choice) {
        case 1:
            applyNegativeFilter(img, width, height, channels);
            strcpy(outputFileName, "negativo.jpg");
            break;
        case 2:
            applyGrayScaleFilter(img, width, height, channels);
            strcpy(outputFileName, "escala_de_cinza.jpg");
            break;
        case 3:
            applyBlurFilter(img, width, height, channels);
            strcpy(outputFileName, "blur.jpg");
            break;
        case 4:
            applyGrayScaleFilter(img, width, height, channels); // Para Sobel, primeiro converte para escala de cinza
            applySobelFilter(img, width, height, channels);
            strcpy(outputFileName, "sobel.jpg");
            break;
        default:
            printf("Escolha inválida!\n");
            stbi_image_free(img);
            return 1;
    }

    // Salvar a imagem processada com o nome apropriado
    saveImage(img, width, height, channels, outputFileName);

    // Liberar memória
    stbi_image_free(img);
    return 0;
}

void applySobelFilter(unsigned char *img, int width, int height, int channels) {
    // Aqui, você precisa implementar a lógica para aplicar o filtro Sobel em X e Y
    // e, em seguida, combinar os resultados usando a distância euclidiana.
    // Esta é uma tarefa avançada que requer manipulação detalhada dos pixels e do buffer de imagem.
}

// Implementação das outras funções de filtro...1
// ...

void saveImage(const unsigned char *img, int width, int height, int channels, const char *outputFileName) {
    char outputPath[200];
    sprintf(outputPath, "Y:\\\\eng\\\\%s", outputFileName); // Constrói o caminho no diretório atual
    stbi_write_jpg(outputPath, width, height, channels, img, 100);
    printf("%s", outputPath);
}


void applyNegativeFilter(unsigned char *img, int width, int height, int channels) {
    // Implementação do Filtro Negativo
}

void applyGrayScaleFilter(unsigned char *img, int width, int height, int channels) {
    // Implementação do filtro de escala de cinza
}

void applyBlurFilter(unsigned char *img, int width, int height, int channels) {
    // Implementação do filtro de blur
}

