

// Bibliotecas
#include <stdio.h>
//...

// Função principal MAIN
int main() {
    
    /* 
    Código
    ...
    ...
    ...
    ...
    */
   int a=1, b=1;
   int x = soma(a,b);
   printf("%d", x);
}


// Somar dois números
int soma(int a, int b) {
    return a + b;
}

// Subtrair dois números
int subtracao(int a, int b) {
    return a - b;
}

// ler 2 numeros do teclado e somar
int soma_lendo_teclado() {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d", soma(a, b));
}

// ler 3 numeros e verificar se formam triangulo
int forma_triangulo() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    if (a + b > c && a + c > b && b + c > a) {
        printf("Forma triangulo");
    } else {
        printf("Nao forma triangulo");
    }
}

// calcular area da circunferencia
float area_circunferencia(float raio) {
    return 3.14 * raio * raio;
}

// calcular area do quadrado
float area_quadrado(float lado) {
    return lado * lado;
}


//calcular area do triangulo
float area_triangulo(float base, float altura) {
    return (base * altura) / 2;
}