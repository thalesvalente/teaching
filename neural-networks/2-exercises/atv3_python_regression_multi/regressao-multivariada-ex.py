# regressao-multivariada-ex.py
"""
@file regressao-multivariada-ex.py
@brief Multivariate linear regression exercise with gradient descent and normal equation.
@details Este script executa um fluxo de trabalho completo para regressão linear multivariada,
          incluindo normalização de features, cálculo de parâmetros via gradiente descendente
          e equação normal, além de comparação de custos.
@author Your Name <your.email@example.com>
"""

import numpy as np
import matplotlib.pyplot as plt
import os

from RegressionMultivariate.features_normalize import features_normalize_by_std
from RegressionMultivariate.features_normalize import features_normalizes_by_min_max
from RegressionMultivariate.compute_cost_multi import compute_cost_multi
from RegressionMultivariate.gradient_descent_multi import gradient_descent_multi
from RegressionMultivariate.gradient_descent_multi import gradient_descent_multi_with_history
from RegressionMultivariate.normal_eqn import normal_eqn

def costs_from_history(X_b: np.ndarray, y: np.ndarray, thetas: np.ndarray) -> np.ndarray:
    """Calcula o custo J(θ) para cada θ em *thetas*."""
    return np.array([compute_cost_multi(X_b, y, th) for th in thetas])

def main():
    """
    Executa o fluxo de trabalho de regressão multivariada.

    1. Carrega os dados de ex1data2.txt.
    2. Normaliza features e adiciona bias.
    3. Roda gradient descent e plota convergência.
    4. Prediz preço com θ encontrado.
    5. Calcula θ via equação normal e prediz.
    6. Compara custo das duas abordagens.
    7. Plota superfície de custo e trajetória do GD.
    8. Plota contorno de custo e trajetória do GD.
    9. Plota plano de regressão ajustado com dados originais.

    Ao fim, escreva um relatório com os resultados obtidos.
    Descreva:
    - As diferentes abordagens utilizadas (GD e NE). Qual foi a vantagem que você encontrou 
    na equação normal? Porque ela é mais rápida? Compare o custo minimo encontrado com as duas abordagens.
    - O que você aprendeu sobre a relação entre o custo e os parâmetros θ. Como o custo muda à medida que os parâmetros são ajustados?
    - O que você aprendeu sobre a normalização de features e como ela afeta o desempenho do GD. Qual a importância da normalização de features?
    ( Faça testes com e sem normalização de features e testando ambos os tipos de normalização. Faça gráficos comparativos explicando eles.)
    - Explique a diferença entre o custo calculado com θ_ne em X_ne (original) e o custo calculado com θ_gd em X_b (normalizado). (Discutir a escala dos dados.)
    - Explique porque a ultima plotagem originou um plano sobre os dados. O que isso significa?

    Obs. O relatório não precisa ser grande, mas precisa ter os gráficos e as explicações. Separe as discuções com subtítulos ou tópicos.

    """
    # 1) Cria pasta de figuras
    os.makedirs("Figures", exist_ok=True)

    # 2) Carrega dados
    data = np.loadtxt('Data/ex1data2.txt', delimiter=',')
    # Carregue todas as linhas, mas somente as 2 primeiras colunas para (X)
    # As duas primeiras colunas são as features (tamanho em pés e número de quartos)
    # O vetor X terá dimensão (m, 2), onde m é o número de amostras
    X = 
    # Carregue a terceira coluna como (y) (preço da casa)
    # A terceira coluna é o preço da casa, que é o valor alvo que queremos prever
    # O vetor y terá dimensão (m,), onde m é o número de amostras
    y = 
    
    # obtenha o número de exemplos de treinamento
    # O número de exemplos de treinamento é o número de linhas em y
    m = 

    print('Primeiros 10 exemplos de treinamento:')
    print(np.column_stack((X[:10], y[:10])))
    """
    Resposta esperada:
    Primeiros 10 exemplos de treinamento:
    [[2.10400e+03 3.00000e+00 3.99900e+05]
    [1.60000e+03 3.00000e+00 3.29900e+05]
    [2.40000e+03 3.00000e+00 3.69000e+05]
    [1.41600e+03 2.00000e+00 2.32000e+05]
    [3.00000e+03 4.00000e+00 5.39900e+05]
    [1.98500e+03 4.00000e+00 2.99900e+05]
    [1.53400e+03 3.00000e+00 3.14900e+05]
    [1.42700e+03 3.00000e+00 1.98999e+05]
    [1.38000e+03 3.00000e+00 2.12000e+05]
    [1.49400e+03 3.00000e+00 2.42500e+05]]
    """
    # 3) Normaliza features
    X_norm, mu, sigma = 
    # Agora devemos adicionar uma coluna de 1s para o termo de bias (intercepto) em X usando np.column_stack
    # Adicione uma coluna de 1s para o termo de bias (intercepto) em X usando np.column_stack
    # A função np.column_stack empilha as colunas de X_norm e uma coluna de 1s
    X_b =   # X para GD
    # imprime os parâmetros de normalização
    print('\nParâmetros de normalização:')
    print(f'Média (mu): {mu}')
    print(f'Desvio Padrão (sigma): {sigma}')
    """
    Resposta esperada:
    Parâmetros de normalização:
    Média (mu): [2000.68085106   3.17021277]
    Desvio Padrão (sigma): [7.86202619e+02 7.52842809e-01]
    """

    # 4) Gradient Descent Multivariado
    alpha = 0.01
    num_iters = 400
    # Inicialize theta com zeros (tamanho n+1, onde n é o número de features)
    # O vetor theta terá dimensão (n+1,), onde n é o número de features
    # e 1 é para o termo de bias (intercepto)
    # O vetor theta é inicializado com zeros, o que significa que inicialmente não temos informações sobre os parâmetros
    # do modelo
    theta_gd = 

    # Chame a função gradient_descent_multi para calcular os parâmetros θ usando o gradiente descendente
    # A função gradient_descent_multi retorna os parâmetros θ aprendidos e o histórico de custo J_history
    # O vetor J_history armazena o custo em cada iteração do gradiente descendente
    theta_gd, J_history = gradient_descent_multi(
    )
    print('\nTheta via Gradient Descent:')
    print(theta_gd)
    """
    Resposta esperada:
    Theta via Gradient Descent:
    [340412.65957447 110631.66014019  -6558.64872094]
    """

    # 4a) Plot de convergência (GD)
    plt.figure()
    # Coloque o J_history aqui para ser plotado
    plt.plot(np.arange(1, num_iters + 1), XXXX, 'b-', linewidth=2)
    plt.xlabel('Iteração')
    plt.ylabel('Custo J(θ)')
    plt.title('Convergência do Gradiente (Multivariada)')
    plt.grid(True)
    plt.savefig('Figures/convergencia_custo_multi.png', dpi=300, bbox_inches='tight')
    plt.savefig('Figures/convergencia_custo_multi.svg', format='svg', bbox_inches='tight')
    plt.show()

    # 5) Predição com GD
    example = np.array([1650, 3]) # features originais
    # Normalize o novo caso de teste usando os mesmos coeficientes de normalização
    # obtidos no treinamento do modelo
    example_norm =  # normaliza
    x_pred = np.concatenate(([1], example_norm)) # adiciona bias
    # Agora podemos fazer a predição usando o vetor theta_gd
    # A predição é feita multiplicando o vetor x_pred pelo vetor theta_gd
    # A predição é o produto escalar entre o vetor x_pred e o vetor theta_gd
    price_gd =  # faz a predição
    print(f'\nPreço previsto (GD) para [1650,3]: ${price_gd:.2f}')
    """
    Resposta esperada:
    Preço previsto (GD) para [1650,3]: $289221.55
    """

    # 6) Equação Normal
    # A equação normal não requer normalização
    # Adicione uma coluna de 1s para o termo de bias (intercepto) em X usando np.column_stack
    # A função np.column_stack empilha as colunas de X e uma coluna de 1s
    # Obs. ne de normal equation
    X_ne =   # X original com bias
    # A equação normal é uma solução fechada para o problema de regressão linear
    # que minimiza a soma dos erros quadráticos entre as previsões e os valores reais
    # Chame a função normal_eqn para calcular os parâmetros θ usando a equação normal
    # A função normal_eqn retorna os parâmetros θ calculados pela equação normal
    theta_ne = 
    
    # Agora vamos fazer uma predição com a equação normal
    # O vetor example tem dimensão (n+1,), onde n é o número de features
    # e 1 é para o termo de bias (intercepto)
    example = np.array([1, 1650, 3]) # features originais com bias
    # Agora podemos fazer a predição usando a equação normal
    # A predição é feita multiplicando o vetor example pelo vetor theta_ne
    # A predição é o produto escalar entre o vetor example e o vetor theta_ne
    # O resultado é um escalar que representa o preço previsto
    # Obs. use o @ para multiplicação de matrizes (ou vetores)
    price_ne =  # faz a predição
    print('\nTheta via Equação Normal:')
    print(theta_ne)
    print(f'Preço previsto (NE) para [1650,3]: ${price_ne:.2f}')
    """
    Resposta esperada:
    Theta via Equação Normal:
    [89597.90954361   139.21067402 -8738.01911255]
    Preço previsto (NE) para [1650,3]: $293081.46
    """

    # --- Comparação de custos ---

    # 6.1) **Forma errada**: aplicar θ_ne em X_b (normalizado)
    #    Isso está **INCORRETO** porque θ_ne foi calculado para X_ne (não normalizado).
    cost_ne_errado = compute_cost_multi(X_b, y, theta_ne)
    print(f'\n[CUSTO ERRADO] Custo usando θ_ne em X_NORMALIZADO (X_b): {cost_ne_errado:.2f}')
    # Note que esse valor não reflete o mínimo global para este modelo,
    # pois X_b e θ_ne não combinam.

    # 6.2) **Forma correta**: aplicar θ_ne em X_ne (original)
    #    Agora θ_ne e X_ne estão na mesma “escala”.
    cost_ne_correto = compute_cost_multi(X_ne, y, theta_ne)
    print(f'[CUSTO CORRETO] Custo usando θ_ne em X_ORIGINAL (X_ne): {cost_ne_correto:.2f}')

    # Também podemos comparar visualmente no gráfico:
    plt.figure()
    plt.plot(np.arange(1, num_iters + 1), J_history,
             'b-', label='Gradiente Descendente')
    plt.hlines(cost_ne_correto, 1, num_iters,
               colors='r', linestyles='--',
               label='Equação Normal (correto)')
    # Se quiséssemos, poderíamos plotar também a linha do custo errado:
    plt.hlines(cost_ne_errado, 1, num_iters, colors='k', linestyles=':', label='NE (errado)')
    plt.xlabel('Iteração')
    plt.ylabel('Custo J(θ)')
    plt.title('GD vs Normal Equation')
    plt.legend()
    plt.grid(True)
    plt.savefig('Figures/convergencia_custo_vs_ne.png', dpi=300, bbox_inches='tight')
    plt.savefig('Figures/convergencia_custo_vs_ne.svg', format='svg', bbox_inches='tight')
    plt.show()

    # -------------- Visualizações 3D / Contorno para multivariada ----------------------------
    # Para visualizar a função de custo J(θ) em 3D ou contorno, precisamos
    # você precisa implementar a função compute_cost_multi_with_history, que calcula o custo
    # e armazena o histórico de parâmetros θ em cada iteração.
    # A função compute_cost_multi_with_history é semelhante à função compute_cost_multi,
    theta_gd, J_history, theta_history = gradient_descent_multi_with_history(
        
    )
    theta_ne_norm = 
    # ------------------------------------------------------------------
    # 7) Contorno J(θ1, θ2) (θ0 fixo em θ_gd[0]). Malha de custo centrada no ótimo
    t1_hist, t2_hist = theta_history[:, 1], theta_history[:, 2]
    max_dev1 = np.max(np.abs(t1_hist - theta_ne_norm[1]))
    max_dev2 = np.max(np.abs(t2_hist - theta_ne_norm[2]))
    span1 = span2 = 1.5 * max(max_dev1, max_dev2)  # mesma escala nos 2 eixos

    t1_vals = np.linspace(theta_ne_norm[1] - span1, theta_ne_norm[1] + span1, 120)
    t2_vals = np.linspace(theta_ne_norm[2] - span2, theta_ne_norm[2] + span2, 120)
    T1, T2 = np.meshgrid(t1_vals, t2_vals)

    J_mesh = np.zeros_like(T1)
    for i in range(T1.shape[0]):
        for j in range(T1.shape[1]):
            J_mesh[i, j] = compute_cost_multi(X_b, y, [theta_ne_norm[0], T1[i, j], T2[i, j]])

    # ------------------------------------------------------------------
    # 8) Superfície J(θ1, θ2) + trajetória GD + NE (normalizado)
    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(111, projection="3d")
    surf = ax.plot_surface(T1, T2, J_mesh, cmap="viridis", alpha=0.85, linewidth=0)
    ax.plot(t1_hist, t2_hist, costs_from_history(X_b, y, theta_history), "r.-", label="Trajetória GD")
    ax.scatter(theta_ne_norm[1], theta_ne_norm[2], compute_cost_multi(X_b, y, theta_ne_norm),
               s=80, marker="x", color="black", linewidths=2, label="NE (norm)")
    fig.colorbar(surf, ax=ax, shrink=0.6, label="Custo J(θ)")
    ax.set_xlabel(r"$\theta_1$"); ax.set_ylabel(r"$\theta_2$"); ax.set_zlabel("Custo J(θ)")
    ax.set_title("Superfície J(θ1, θ2)")
    ax.view_init(elev=30, azim=-60)
    ax.legend()
    fig.savefig("Figures/superficie_GD_vs_NE.png", dpi=300)

    # --------------------------------------------------------------
    # 8a) Contorno J(θ1, θ2) + trajetória GD + NE (normalizado)
    # O gráfico de contorno é uma projeção 2D da superfície 3D
    from matplotlib.colors import LogNorm
    plt.figure(figsize=(7, 5))
    levels = np.logspace(np.log10(J_mesh.min()), np.log10(J_mesh.max()), 60)
    cf = plt.contourf(T1, T2, J_mesh, levels=levels, norm=LogNorm(), cmap="viridis")
    plt.colorbar(cf, label="Custo J(θ)")
    plt.plot(t1_hist, t2_hist, "r.-", ms=2, label="Trajetória GD")
    plt.scatter(theta_ne_norm[1], theta_ne_norm[2], s=80, marker="x", color="black", label="NE (norm)")
    plt.xlabel(r"$\theta_1$"); plt.ylabel(r"$\theta_2$")
    plt.title("Contorno J(θ1, θ2)"); plt.legend()
    plt.savefig("Figures/contorno_GD_vs_NE.png", dpi=300)
    plt.show()

    # ------------------------------------------------------------------
    # 9) Plano de regressão ajustado + pontos originais (3‑D) ------------
    # ------------------------------------------------------------------
    fig2 = plt.figure(figsize=(7, 5))
    ax2 = fig2.add_subplot(111, projection="3d")

    # Pontos originais (feature1 = tamanho; feature2 = quartos)
    ax2.scatter(X[:, 0], X[:, 1], y, c="red", marker="x", label="Dados de treino")

    # Plano de regressão (usando θ_gd já calculado no início do script)
    # Gera malha nas escalas originais (não normalizadas)
    f1_vals = np.linspace(X[:, 0].min(), X[:, 0].max(), 40)
    f2_vals = np.linspace(X[:, 1].min(), X[:, 1].max(), 40)
    F1, F2 = np.meshgrid(f1_vals, f2_vals)

    # Precisamos do θ na escala original → convertemos θ_gd (normalizado) para original
    theta_gd_orig = np.zeros_like(theta_ne)
    theta_gd_orig[1:] = theta_gd[1:] / sigma  # coeficientes revertidos
    theta_gd_orig[0] = theta_gd[0] - np.sum((mu / sigma) * theta_gd[1:])  # intercepto

    Z = theta_gd_orig[0] + theta_gd_orig[1] * F1 + theta_gd_orig[2] * F2
    surf2 = ax2.plot_surface(
        F1, F2, Z, alpha=0.5, cmap="viridis", rstride=1, cstride=1
    )

    ax2.set_xlabel("Tamanho (pés²)")
    ax2.set_ylabel("Quartos")
    ax2.set_zlabel("Preço (US$)")
    ax2.set_title("Ajuste da Regressão Linear Multivariada")
    ax2.view_init(elev=25, azim=-135)
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch

    handles = [
        Line2D([], [], color="red", marker="x", linestyle="", label="Dados de treino"),
        Patch(facecolor=surf2.get_facecolor()[0], edgecolor="none", alpha=0.5, label="Plano GD"),
    ]
    ax2.legend(handles=handles)
    fig2.tight_layout()
    fig2.savefig("Figures/ajuste_regressao_multivariada.png", dpi=300)
    plt.show()

if __name__ == '__main__':
    main()
