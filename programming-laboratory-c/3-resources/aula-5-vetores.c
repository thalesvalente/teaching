#include <stdio.h>

void q1(){
// Crie um programa que leia 3 valores e exiba na ordem inversa
/*
1 passo- declaro vetor com 3 casas
2 passo- declaro o cara do ibge (variavel que anda pelas casas)
3 passo- laco com scanf que le os 10 valores
4 passo- laco inverso para imprimir
*/

    int vetor[3], i; // passos 1 e 2
    //passo 3
    for(i=0; i<3; i++){
        scanf("%d", &vetor[i]);
    }

    //passo 4
    for(i=2; i>=0; i--){
        printf("%d ", vetor[i]);
    }
}

void q2(){

// dado um vetor e um numero informe se o vetor contem o numero
/*
1 passo- iniciar as variaveis (vetor, numero a ser buscado, auxiliar)
2 passo- ler o numero a ser buscado
3 passo- laco percorrendo as casa e vendo se acha fulano pelas casas
*/

// passo 1
    int vetor[5]={3,7,100,56,67};
    int i, numero_buscado;

//passo 2
    scanf("%d", &numero_buscado);
    //int aux=numero_buscado;
//passo 3
    for(i=0; i<5; i++){
        if(numero_buscado == vetor[i]){
            printf("Achei!");
            //aux = -1;
            //break;
        }
        else{
            if(i==4){
                printf("Nao achei");
            }
        }
    }
    //if(aux == numero_buscado){
    //    printf("Nao achei!");
    //}
}

void q3(){
    int vetor[3]={1,3,3};
    int vetor2[3]={0,0,0};
    int i, numero_buscado=3;
    
    for(i=0;i<3;i++){
        if(vetor[i]==numero_buscado){
            vetor2[i]=1;
        }
    }

    for(i=0;i<3;i++){
        if(vetor2[i]==1){
            printf("%d ",i);
        }
    }

/*
1 Passo- declara as variaveis
    . Vetor de casas a serem percorridas
    . Vetor indicando as posicoes em que achei
    . auxiliar i
    . numero_buscado

2 Passo- 
    . percorre as casas procurando numero_buscado
    . se eu achei, indico como verdadeiro no vetor das posicoes
3 Passo-
    . percorre vetor das posicoes
    . se posicao verdeiro, imprimo
*/

}

void main(){
    q3();
}