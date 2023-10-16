
#include <stdio.h>
#include <math.h>
#include <string.h>

void sistema_monitoramento_tensao() {
    double tensao;
    scanf("%lf", &tensao);
    if (tensao < 1) {
        printf("Baixa\n");
    } else if (tensao >= 1 && tensao <= 3) {
        printf("Media\n");
    } else {
        printf("Alta\n");
    }
}

void calculo_potencia() {
    double base, expoente, potencia;
    scanf("%lf %lf", &base, &expoente);
    potencia = pow(base, expoente);
    printf("%.2lf\n", potencia);
}

int main() {
    char function_name[50];
    scanf("%s", function_name);
    if (strcmp(function_name, "sistema_monitoramento_tensao") == 0) {
        sistema_monitoramento_tensao();
    } else if (strcmp(function_name, "calculo_potencia") == 0) {
        calculo_potencia();
    }
    return 0;
}
