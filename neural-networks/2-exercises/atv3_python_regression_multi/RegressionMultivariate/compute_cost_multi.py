# Functions/compute_cost_multi.py
"""
@file compute_cost_multi.py
@brief Computes the cost for multivariate linear regression.
@details Este módulo contém uma função para calcular o custo de um modelo de regressão linear
          multivariada utilizando a função de custo de erro quadrático médio.
@author Your Name <your.email@example.com>
"""

import numpy as np


def compute_cost_multi(X, y, theta):
    """
    Calcula o custo para regressão linear multivariada.

    A função de custo é definida como:
        J(θ) = (1 / (2m)) * (Xθ - y)ᵀ (Xθ - y)

    :param (ndarray) X: Matriz de features incluindo o termo de intercepto (shape: m × n+1).
    :param (ndarray) y: Vetor de valores alvo (shape: m,).
    :param (ndarray) theta: Vetor de parâmetros (shape: n+1,).
    :return (float): Valor do custo calculado.
    """
    # get the number of training examples
    m = 
    # compute the predictions using the linear model by formula h(θ) = X @ θ
    # where @ is the matrix multiplication operator
    predictions = 
    # compute the error vector between predictions and actual values
    # The error is the difference between the predicted values and the actual values
    # errors = predictions - y
    errors = 
    # compute the cost as the mean squared error cost function using the formula in the docstring
    cost = 
    return cost
