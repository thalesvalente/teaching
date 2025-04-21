"""
@file compute_cost.py
@brief Computes the cost for linear regression.
"""

import numpy as np

def compute_cost(X, y, theta):
    """
    Compute the cost for linear regression.

    This function calculates the mean squared error cost function J(θ) for linear regression:
    J(θ) = (1 / (2 * m)) * Σ (h(θ) - y)^2

    where:
    - J(θ) is the cost
    - m is the number of training examples
    - h(θ) is the hypothesis function (X @ theta)
    - y is the vector of observed values

    @param X: np.ndarray
        Feature matrix including the intercept term (shape: m x n).
    @param y: np.ndarray
        Target variable vector (shape: m,).
    @param theta: np.ndarray
        Parameter vector for linear regression (shape: n,).

    @return: float
        The computed cost value as a single float.
    """
    # get the number of training examples
    m = 

    # Compute the predictions using the linear model by formula h(θ) = X @ θ
    # where @ is the matrix multiplication operator
    h_o = 

    # Compute the error vector between predictions and actual values
    # The error is the difference between the predicted values and the actual values
    errors =

    # Compute the cost as the mean squared error cost function using the formula in the docstring
    J_o = 
    J_o = np.sum()

    return 
