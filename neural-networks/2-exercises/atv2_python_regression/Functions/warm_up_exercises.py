"""
@file warm_up_exercise.py
@brief Returns a 5x5 identity matrix.
"""

import numpy as np

def warm_up_exercise1():
    """
    @brief Create and return a 5x5 identity matrix.

    @return np.ndarray Identity matrix (5x5)
    """
    return 

def warm_up_exercise2(m=5):
    """
    @brief Cria um vetor coluna de 1s, utilizado como termo de bias (intercepto) em regressão linear.

    @param m: int
        Número de exemplos (linhas).

    @return np.ndarray
        Vetor de shape (m, 1) com todos os valores iguais a 1.
    """
    return 

def warm_up_exercise3(x):
    """
    @brief Adiciona uma coluna de 1s (bias) ao vetor de entrada x.

    @param x: np.ndarray
        Vetor unidimensional de shape (m,)

    @return np.ndarray
        Matriz de shape (m, 2), com a primeira coluna sendo 1s (bias) e a segunda os valores de x.
    """
    # obtem o número de exemplos
    m = 
    # Garante que x é um vetor coluna usando reshape. Use np.reshape
    x = 
    # Adiciona uma coluna de 1s (bias) ao vetor x. Use np.ones para criar um vetor de 1s
    bias = 
    # Concatena a coluna de 1s (bias) com o vetor x. Use np.hstack para concatenar horizontalmente e retorne
    return 

def warm_up_exercise4(X, theta):
    """
    @brief Realiza a multiplicação matricial entre X e θ, simulando h(θ) = X @ θ.

    @param X: np.ndarray
        Matriz de entrada de shape (m, n)

    @param theta: np.ndarray
        Vetor de parâmetros de shape (n,)

    @return np.ndarray
        Vetor de predições (m,)
    """
    # retorna o resultado da multiplicação matricial entre X e θ
    return 

def warm_up_exercise5(predictions, y):
    """
    @brief Calcula o vetor de erros quadráticos (squared errors) entre as predições e os valores reais.

    @param predictions: np.ndarray
        Vetor de predições (m,)

    @param y: np.ndarray
        Vetor de valores reais (m,)

    @return np.ndarray
        Vetor com os erros quadráticos: (pred - y)^2
    """
    # Calcula o vetor de erros quadráticos (squared errors) entre as predições e os valores reais
    # O vetor de erros quadráticos é calculado como a diferença entre as predições e os valores reais
    return 

def warm_up_exercise6(errors):
    """
    @brief Calcula o custo médio (mean cost) a partir dos erros quadráticos.

    @param errors: np.ndarray
        Vetor de erros quadráticos (m,)

    @return float
        Custo médio (mean cost)
    """
    # O custo médio é calculado como a média dos erros quadráticos
    # Obtenha usando np.mean e não esqueça de dividir por 2
    return 

def warm_up_exercise7(X, y, theta):
    """
    @brief Calcula o custo médio (mean cost) para um modelo de regressão linear.

    @param X: np.ndarray
        Matriz de entrada de shape (m, n)

    @param y: np.ndarray
        Vetor de valores reais (m,)

    @param theta: np.ndarray
        Vetor de parâmetros de shape (n,)

    @return float
        Custo médio (mean cost)
    """
    # Use as funções auxiliares para calcular o custo médio
    # 1. Calcule as predições usando a função warm_up_exercise4
    # 2. Calcule os erros quadráticos usando a função warm_up_exercise5
    # 3. Calcule o custo médio usando a função warm_up_exercise6
    # 4. Retorne o custo médio
    predictions = 
    errors = 
    return 