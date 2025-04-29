# Functions/normal_eqn.py
"""
@file normal_eqn.py
@brief Calcula os parâmetros θ usando a Equação Normal.
@details Este módulo contém uma função para calcular os parâmetros de um modelo
          de regressão linear utilizando a equação normal.
@author Your Name <your.email@example.com>
"""

import numpy as np


def normal_eqn(X, y):
    """
    Resolve os parâmetros θ utilizando a equação normal.

    A equação normal é definida como:
        θ = (XᵀX)⁻¹ Xᵀ y

    :param (ndarray) X: Matriz de features com bias, onde cada linha é uma amostra
                        e cada coluna é uma feature (shape: m × n+1).
    :param (ndarray) y: Vetor de valores alvo (shape: m,).
    :return (ndarray): Vetor de parâmetros θ (shape: n+1,).
    """
    # Calcula os parâmetros θ utilizando a equação normal
    # A equação normal é uma solução fechada para o problema de regressão linear
    # que minimiza a soma dos erros quadráticos entre as previsões e os valores reais
    # Implemente aqui a equação normal descrita na docstring. Use a função np.linalg.pinv
    # para calcular a pseudo-inversa de uma matriz, que é útil quando a matriz não é quadrada
    # ou não é invertível.
    # A pseudo-inversa é uma generalização da inversa de uma matriz e pode ser usada para resolver
    # sistemas de equações lineares que não têm uma solução única ou que são mal condicionados.
    return 
