#include <stdio.h>
#include <string.h>

// Protótipos das funções
// OBS. NÃO modifique a assinatura das funções (tipo retorno, nome, parâmetros).
// Apenas implemente o corpo delas trocando o ; por chaves

/*
Atividade 1: Monitoramento Contínuo de Tensão
Contexto: Em sistemas eletrônicos, o monitoramento contínuo da tensão é fundamental para garantir a segurança e a eficiência do equipamento. Por exemplo, baterias de dispositivos móveis, quando sobrecarregadas, podem sofrer danos ou até mesmo explodir.
Desafio: Implemente um sistema que lê continuamente a tensão (em volts) de um dispositivo. O sistema deve executar em um laço 'while' e monitorar a tensão até que o usuário decida parar a leitura (por exemplo, pressionando a tecla 'q'). Em cada leitura, o sistema deve classificar a tensão como:
    // - Baixa (menor que 3.5V)
    // - Média (entre 3.5V e 4.2V)
    // - Alta (maior que 4.2V)
    // Em caso de tensão alta, um alerta deve ser exibido para o usuário.
*/
void monitoramento_continuo_de_tensao();

/*
Atividade 4: Medição Iterativa de Resistência em um Circuito
Contexto: Em laboratórios de eletrônica e em processos de manutenção, é comum medir a resistência de componentes ou de partes de um circuito várias vezes para garantir precisão e verificar a estabilidade do componente ou circuito.
Desafio: Suponha que você esteja trabalhando com um multímetro digital e deseja medir a resistência de um resistor em diferentes momentos para verificar sua estabilidade.

       // - Utilize um laço 'for' para simular 5 medições de resistência.
   	       // - Em cada iteração, solicite ao usuário que insira o valor medido (em Ohms).
   	       // - Calcule e imprima a média dos valores medidos após todas as iterações.
  // - Caso a variação entre as medições exceda um limite pré-definido (por exemplo, 5% do valor médio), alerte o usuário sobre a possível instabilidade do resistor.
*/
void medicao_iterativa_de_resistencia_em_um_circuito();

/*
Atividade 6: Treinamento Iterativo de um Neurônio Artificial
Contexto: Em aprendizado de máquina, os neurônios artificiais são ajustados iterativamente para melhorar seu desempenho em tarefas específicas. O processo de ajustar o peso de um neurônio com base em um erro é chamado de treinamento.
 Desafio: Simule um treinamento básico de um neurônio. Para cada iteração, ajuste o peso do neurônio com base em um valor de erro fornecido.
    // - Inicie o neurônio com  o peso 0.5.
    // - Em cada iteração, solicite ao usuário um valor de erro (por exemplo, um número entre -1 e 1).
    // - Ajuste o peso do neurônio subtraindo o valor do erro.
    // - Continue o treinamento até que o usuário decida parar, inserindo um valor específico, como -999.
*/
void treinamento_iterativo_de_um_neuronio_artificial();

/*
Atividade 8: Processamento Iterativo de Sinais
Contexto: O processamento de sinais é crucial em sistemas de comunicação. Em muitas situações, precisamos calcular a média de várias leituras para obter um valor representativo ou para filtrar ruído.
Desafio: Implemente um programa que leia uma quantidade específica de valores representando leituras de sinal e calcule a média.
// - Solicite ao usuário quantas leituras de sinal ele deseja fazer (por exemplo, 5 leituras).
// - Use um laço para solicitar e acumular cada leitura.
// - Calcule e exiba a média dos valores inseridos.
*/
void processamento_iterativo_de_sinais();

// OBS. NÃO modifique a main
int main() {
    char function_name[100];
    scanf("%s", function_name);

    if (strcmp(function_name, "monitoramento_continuo_de_tensao") == 0) {
        monitoramento_continuo_de_tensao();
    } else if (strcmp(function_name, "medicao_iterativa_de_resistencia_em_um_circuito") == 0) {
        medicao_iterativa_de_resistencia_em_um_circuito();
    } else if (strcmp(function_name, "treinamento_iterativo_de_um_neuronio_artificial") == 0) {
        treinamento_iterativo_de_um_neuronio_artificial();
    } else if (strcmp(function_name, "processamento_iterativo_de_sinais") == 0) {
        processamento_iterativo_de_sinais();
    }

    return 0;
}