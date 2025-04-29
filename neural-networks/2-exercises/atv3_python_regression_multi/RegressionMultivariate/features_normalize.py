# Functions/feature_normalize.py
"""
@file features_normalizes.py
@brief Funções para normalização de features em datasets.
@details Este módulo contém funções para normalizar as features de um dataset
          utilizando diferentes abordagens, como média e desvio padrão, ou
          mínimo e máximo.
@author Your Name <your.email@example.com>
"""
import numpy as np


def features_normalize_by_std(X):
    """
    Normaliza as features de um dataset para média zero e desvio padrão unitário.
    Matematicamente, a formula utilizada é:
        X_norm = (X - mu) / sigma
    onde:
        - X é a matriz de entrada (m x n) onde m é o número de amostras e n é o número de features.
        - mu é o vetor de médias (1 x n) de cada feature.
        - sigma é o vetor de desvios padrão (1 x n) de cada feature.

    :param (ndarray) X: Matriz de entrada onde cada linha é uma amostra e cada coluna é uma feature.
    :return (tuple): Uma tripla contendo:
        - X_norm (ndarray): Matriz normalizada.
        - mu (ndarray): Vetor com as médias de cada feature.
        - sigma (ndarray): Vetor com os desvios padrão de cada feature.
    """
    # Calcula a média de cada feature (coluna)
    mu = 

    # Calcula o desvio padrão de cada feature (coluna)
    sigma = 
    
    # Normaliza as features subtraindo a média e dividindo pelo desvio padrão
    # Verifica se sigma é zero (o que indicaria que todas as amostras têm o mesmo valor na feature)
    # Se sigma for zero, substitui por 1 para evitar divisão por zero
    # Isso garante que a normalização não cause problemas numéricos
    # e que a feature não seja eliminada do conjunto de dados
    if np.any(sigma == 0):
        sigma[sigma == 0] = 1
    # Normaliza as features
    X_norm = 
    return X_norm, mu, sigma


def features_normalizes_by_min_max(X):
    """
    Normaliza as features de um dataset para o intervalo [0, 1] utilizando o mínimo e o máximo.
    Matematicamente, a formula utilizada é:
        X_norm = (X - min) / (max - min)
    onde:
        - X é a matriz de entrada (m x n) onde m é o número de amostras e n é o número de features.
        - min é o vetor de mínimos (1 x n) de cada feature.
        - max é o vetor de máximos (1 x n) de cada feature.

    :param (ndarray) X: Matriz de entrada onde cada linha é uma amostra e cada coluna é uma feature.
    :return (tuple): Uma tupla contendo:
        - X_norm (ndarray): Matriz normalizada.
        - min (ndarray): Vetor com os valores mínimos de cada feature.
        - max (ndarray): Vetor com os valores máximos de cada feature.
    """
    # Calcula o mínimo de cada feature (coluna)
    min = 
    # Calcula o máximo de cada feature (coluna)
    max = 
    # Normaliza as features subtraindo o mínimo e dividindo pela diferença entre máximo e mínimo
    # Verifica se max - min é zero (o que indicaria que todas as amostras têm o mesmo valor na feature)
    # Se max - min for zero, substitui por 1 para evitar divisão por zero
    # Isso garante que a normalização não cause problemas numéricos
    # e que a feature não seja eliminada do conjunto de dados
    if np.any(max - min == 0):
        max[min == max] = 1
    # Normaliza as features
    X_norm = 
    return X_norm, min, max
