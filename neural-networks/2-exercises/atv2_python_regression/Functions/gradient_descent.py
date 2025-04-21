"""
@file gradient_descent.py
@brief Implementa o algoritmo de descida do gradiente para regressão linear.
"""

import numpy as np
from Functions.compute_cost import compute_cost


def gradient_descent(X, y, theta, alpha, num_iters):
    """
    Executa a descida do gradiente para minimizar a função de custo J(θ)
    no contexto de regressão linear.

    A cada iteração, os parâmetros theta são atualizados com base
    no gradiente da função de custo em relação aos parâmetros atuais.

    @param X: np.ndarray
        Matriz de entrada (m amostras × n atributos), incluindo termo de bias.
    @param y: np.ndarray
        Vetor de saída esperado com dimensão (m,).
    @param theta: np.ndarray
        Vetor de parâmetros inicial (n,).
    @param alpha: float
        Taxa de aprendizado (learning rate).
    @param num_iters: int
        Número de iterações da descida do gradiente.

    @return: tuple[np.ndarray, np.ndarray]
        theta: vetor otimizado de parâmetros (n,).
        J_history: vetor com o histórico do valor da função de custo em cada iteração (num_iters,).
        theta_history: parâmetros em cada iteração (num_iters+1, n).
    """
    # Obtem o número de amostras
    m = len(y)
    # Inicializa o vetor de custo J_history para armazenar o custo em cada iteração com zeros
    # O vetor J_history tem o mesmo tamanho que o número de iterações
    J_history = 

    # Inicializa o vetor theta_history para armazenar os parâmetros em cada iteração
    # O vetor theta_history tem o tamanho (num_iters + 1, n)
    # O vetor theta_history é inicializado com zeros
    # num_iters é o número de iterações
    # O +1 é para armazenar os parâmetros iniciais antes de começar as iterações
    # n é o número de parâmetros (atributos) no vetor theta
    # Em resumo, theta_history é uma matriz onde cada linha representa os parâmetros em uma iteração
    # e a primeira linha (índice 0) contém os parâmetros theta iniciais
    theta_history = 

    # Armazena os parâmetros iniciais no vetor theta_history
    # Isso é útil para visualizar como os parâmetros evoluem ao longo das iterações
    # e como eles convergem para os valores ótimos
    # theta_history é uma matriz onde cada linha representa os parâmetros em uma iteração
    # A primeira linha (índice 0) contém os parâmetros theta iniciais
    # Isso permite acompanhar a evolução dos parâmetros ao longo do processo de otimização
    # As demais linhas serão preenchidas com os parâmetros atualizados em cada iteração
    theta_history[0] = 

    for i in range():
        # Calcula as previsões (hipótese) com base nos parâmetros atuais
        # A hipótese (predições) é calculada como o produto escalar entre a matriz de entrada X e o vetor de parâmetros theta
        predictions = 

        # Calcula o erro entre as previsões e os valores reais
        # O erro é a diferença entre as previsões e os valores reais
        # Isso fornece uma medida de quão longe as previsões estão dos valores reais
        # O erro é usado para calcular o gradiente da função de custo
        erro = 

        # Calcula o gradiente da função de custo em relação a theta
        # O gradiente é calculado como a média do erro multiplicado pela matriz de entrada X
        # Isso fornece uma medida de quão sensível é a função de custo em relação a cada parâmetro
        # O gradiente é um vetor que aponta na direção de maior aumento da função de custo
        # Portanto, para minimizar a função de custo, os parâmetros devem ser ajustados na direção oposta ao gradiente
        gradient = 

        # Atualiza os parâmetros theta
        # O novo valor de theta é obtido subtraindo o produto da taxa de aprendizado
        # pelo gradiente da função de custo em relação a theta
        # Isso ajusta os parâmetros na direção oposta ao gradiente, minimizando a função de custo
        theta = 

        # Armazena o custo da iteração atual para análise
        J_history[i] = 

        # Armazena os parâmetros theta da iteração atual para análise
        # Isso permite visualizar como os parâmetros evoluem ao longo das iterações
        # Isso pode ser útil para entender o comportamento do algoritmo de descida do gradiente
        # e como os parâmetros convergem para os valores ótimos
        theta_history[i + 1] = 

    return theta, J_history, theta_history