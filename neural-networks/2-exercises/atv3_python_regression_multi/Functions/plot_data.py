"""
@file plot_data.py
@brief Plots the data points.
"""

import matplotlib.pyplot as plt

def plot_data(x, y):
    """
    @brief Plot training data as red crosses.

    @param x np.ndarray Independent variable (population)
    @param y np.ndarray Dependent variable (profit)
    """
    plt.figure()
    plt.plot(x, y, 'rx', markersize=5)
    plt.xlabel('Population of City in 10,000s')
    plt.ylabel('Profit in $10,000s')
    plt.title('Training Data')
    plt.grid(True)
    plt.show()
