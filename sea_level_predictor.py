# sea_level_predictor.py  # nome do arquivo (apenas informativo)
import pandas as pd  # importa a biblioteca pandas para ler/organizar os dados em DataFrames
import matplotlib.pyplot as plt  # importa matplotlib para criar gráficos
from scipy.stats import linregress  # importa linregress para calcular a regressão linear (inclui slope e intercept)
import numpy as np  # importa NumPy para criar sequências numéricas (anos até 2050)


def draw_plot():  # define a função principal exigida pelos testes da FCC
    # 1) Importa dados
    df = pd.read_csv("epa-sea-level.csv")  # lê o arquivo CSV com as colunas 'Year' e 'CSIRO Adjusted Sea Level'

    # 2) Scatter: Year vs CSIRO Adjusted Sea Level
    fig, ax = plt.subplots(figsize=(10, 6))  # cria a figura e o eixo do gráfico, definindo o tamanho
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])  # plota o diagrama de dispersão (pontos) de Ano vs Nível do Mar

    # 3) Regressão com TODOS os anos (estende até 2050)
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])  # calcula a reta de melhor ajuste para todo o período
    x_all = np.arange(1880, 2051)  # início do dataset -> 2050  # cria um array de anos de 1880 até 2050 (inclusive)
    y_all = res_all.intercept + res_all.slope * x_all  # aplica a equação da reta: y = intercept + slope * x
    ax.plot(x_all, y_all)  # desenha a linha de melhor ajuste (todos os anos) no gráfico

    # 4) Regressão usando apenas dados de 2000 em diante (também até 2050)
    df_2000 = df[df["Year"] >= 2000]  # filtra o DataFrame mantendo apenas linhas com ano >= 2000
    res_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])  # regressão linear só para dados 2000+
    x_2000 = np.arange(2000, 2051)  # cria os anos de 2000 até 2050 (inclusive)
    y_2000 = res_2000.intercept + res_2000.slope * x_2000  # calcula os valores previstos para a regressão 2000+
    ax.plot(x_2000, y_2000)  # plota a linha de melhor ajuste (2000+) no gráfico

    # 5) Rótulos e título EXATOS
    ax.set_xlabel("Year")  # define o rótulo do eixo X exatamente como exigido
    ax.set_ylabel("Sea Level (inches)")  # define o rótulo do eixo Y exatamente como exigido
    ax.set_title("Rise in Sea Level")  # define o título do gráfico exatamente como exigido

    # 6) Salva a figura e retorna o eixo (o teste usa isso)
    plt.savefig("sea_level_plot.png")  # salva a imagem do gráfico no arquivo PNG
    return ax  # retorna o objeto de eixo para que os testes possam inspecionar o gráfico
