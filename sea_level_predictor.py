# sea_level_predictor.py
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # 1) Importa dados
    df = pd.read_csv("epa-sea-level.csv")

    # 2) Scatter: Year vs CSIRO Adjusted Sea Level
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # 3) Regressão com TODOS os anos (estende até 2050)
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_all = np.arange(1880, 2051)  # início do dataset -> 2050
    y_all = res_all.intercept + res_all.slope * x_all
    ax.plot(x_all, y_all)

    # 4) Regressão usando apenas dados de 2000 em diante (também até 2050)
    df_2000 = df[df["Year"] >= 2000]
    res_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    x_2000 = np.arange(2000, 2051)
    y_2000 = res_2000.intercept + res_2000.slope * x_2000
    ax.plot(x_2000, y_2000)

    # 5) Rótulos e título EXATOS
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # 6) Salva a figura e retorna o eixo (o teste usa isso)
    plt.savefig("sea_level_plot.png")
    return ax
