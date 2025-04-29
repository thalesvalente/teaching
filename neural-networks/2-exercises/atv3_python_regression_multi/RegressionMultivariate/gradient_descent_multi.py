# Functions/gradient_descent_multi.py
"""
@file gradient_descent_multi.py
@brief Performs gradient descent for multivariate regression.
@details Este módulo contém uma função para executar o gradiente descendente
          para regressão linear multivariada, atualizando os parâmetros θ
          iterativamente para minimizar a função de custo.
@author Your Name <your.email@example.com>
"""

import numpy as np
from RegressionMultivariate.compute_cost_multi import compute_cost_multi


def gradient_descent_multi(X, y, theta, alpha, num_iters):
    """
    Executa o gradiente descendente para aprender os parâmetros θ.

    Atualiza θ realizando num_iters passos de gradiente com taxa de aprendizado α usando a fórmula:
        θ := θ - α * (1/m) * (Xᵀ * (Xθ - y))
    onde:
        - θ é o vetor de parâmetros (n+1,).
        - m é o número de amostras.
        - X é a matriz de features (m × n+1).
        - y é o vetor de valores alvo (m,).
        - α é a taxa de aprendizado.

    :param (ndarray) X: Matriz de features com termo de bias (shape: m × n+1).
    :param (ndarray) y: Vetor de valores alvo (shape: m,).
    :param (ndarray) theta: Vetor de parâmetros iniciais (shape: n+1,).
    :param (float) alpha: Taxa de aprendizado.
    :param (int) num_iters: Número de iterações.
    :return (tuple): Uma tupla com 2 elementos contendo:
        - theta (ndarray): Parâmetros aprendidos (shape: n+1,).
        - J_history (ndarray): Custo em cada iteração (shape: num_iters,).
    """
    # obtenha o número de exemplos de treinamento
    m = 
    
    # inicialize o vetor de custo para armazenar o custo em cada iteração com 0s
    # O vetor J_history armazena o custo em cada iteração do gradiente descendente
    J_history = 

    # loop para atualizar os parâmetros θ usando o gradiente descendente
    # O loop itera num_iters vezes, atualizando os parâmetros θ a cada iteração
    for i in range():
        # calcule o erro entre as previsões e os valores reais
        # O erro é a diferença entre os valores previstos e os valores reais
        error = 

        # calcule o gradiente para atualizar os parâmetros θ
        # O gradiente é a derivada da função de custo em relação aos parâmetros θ
        # O gradiente é um vetor que aponta na direção de maior aumento da função de custo
        # O gradiente é calculado como a média do erro multiplicado pela matriz de features transposta
        # O gradiente é um vetor que representa a direção e a magnitude da mudança necessária
        gradient = 

        # A atualização dos parâmetros θ é feita usando a fórmula do gradiente descendente
        # A taxa de aprendizado α controla o tamanho do passo na direção do gradiente
        # A atualização dos parâmetros θ é feita na direção oposta ao gradiente
        # para minimizar a função de custo
        # Atualize os parâmetros θ subtraindo pelo gradiente multiplicado pela taxa de aprendizado α
        theta = 

        # Agora Calcule o custo atual e armazene-o no vetor J_history
        # O custo é calculado usando a função de custo definida na função compute_cost_multi
        # O custo é uma medida de quão bem o modelo se ajusta aos dados de treinamento
        # Quando o custo é baixo, significa que o modelo está fazendo previsões precisas
        J_history[i] = 

    return theta, J_history


def gradient_descent_multi_with_history(X, y, theta, alpha, num_iters):
    """
    Executa o gradiente descendente para aprender os parâmetros θ.

    Atualiza θ realizando num_iters passos de gradiente com taxa de aprendizado α usando a fórmula:
        θ := θ - α * (1/m) * (Xᵀ * (Xθ - y))
    onde:
        - θ é o vetor de parâmetros (n+1,).
        - m é o número de amostras.
        - X é a matriz de features (m × n+1).
        - y é o vetor de valores alvo (m,).
        - α é a taxa de aprendizado.

    :param (ndarray) X: Matriz de features com termo de bias (shape: m × n+1).
    :param (ndarray) y: Vetor de valores alvo (shape: m,).
    :param (ndarray) theta: Vetor de parâmetros iniciais (shape: n+1,).
    :param (float) alpha: Taxa de aprendizado.
    :param (int) num_iters: Número de iterações.
    :return (tuple): Uma tupla com 2 elementos contendo:
        - theta (ndarray): Parâmetros aprendidos (shape: n+1,).
        - J_history (ndarray): Custo em cada iteração (shape: num_iters,).
        - theta_history (ndarray): Histórico dos parâmetros θ em cada iteração (shape: num_iters × n+1).
    """
    # obtenha o número de exemplos de treinamento
    m = 

    # obtenha o número de parâmetros
    n = 
    
    # inicialize o vetor de custo para armazenar o custo em cada iteração com 0s
    # O vetor J_history armazena o custo em cada iteração do gradiente descendente
    J_history = 

    # inicialize o vetor de histórico de parâmetros para armazenar os parâmetros em cada iteração com 0s
    # O vetor theta_history armazena os parâmetros em cada iteração do gradiente descendente
    # Deve ter o mesmo número de linhas que o número de iterações+1 e o mesmo número de colunas que o número de parâmetros
    theta_history = 

    # armazene os parâmetros iniciais no vetor de histórico de parâmetros
    # Faça uma cópia dos parâmetros iniciais para evitar modificações indesejadas
    # Agora você sabe porque o vetor theta_history tem num_iters+1 linhas
    theta_history[0] = 

    # loop para atualizar os parâmetros θ usando o gradiente descendente
    # O loop itera num_iters vezes, atualizando os parâmetros θ a cada iteração
    for i in range(num_iters):
        # calcule o erro entre as previsões e os valores reais
        # O erro é a diferença entre os valores previstos e os valores reais
        error = 

        # calcule o gradiente para atualizar os parâmetros θ
        # O gradiente é a derivada da função de custo em relação aos parâmetros θ
        # O gradiente é um vetor que aponta na direção de maior aumento da função de custo
        # O gradiente é calculado como a média do erro multiplicado pela matriz de features transposta
        # O gradiente é um vetor que representa a direção e a magnitude da mudança necessária
        gradient = 

        # A atualização dos parâmetros θ é feita usando a fórmula do gradiente descendente
        # A taxa de aprendizado α controla o tamanho do passo na direção do gradiente
        # A atualização dos parâmetros θ é feita na direção oposta ao gradiente
        # para minimizar a função de custo
        # Atualize os parâmetros θ subtraindo pelo gradiente multiplicado pela taxa de aprendizado α
        theta = 

        # Agora Calcule o custo atual e armazene-o no vetor J_history
        # O custo é calculado usando a função de custo definida na função compute_cost_multi
        # O custo é uma medida de quão bem o modelo se ajusta aos dados de treinamento
        # Quando o custo é baixo, significa que o modelo está fazendo previsões precisas
        J_history[i] = 

        # Agora aqui é que vem a mágica, a diferença entre essa função e a anterior
        # Armazene os parâmetros θ atuais no vetor de histórico de parâmetros
        # Isso é útil para visualizar como os parâmetros mudam ao longo do tempo
        # Faça uma cópia dos parâmetros theta atuais para evitar modificações indesejadas
        # Use o i+1 para armazenar os parâmetros na linha correta do vetor de histórico de parâmetros
        theta_history[i+1] = 

    return theta, J_history, theta_history
