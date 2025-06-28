import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Cargar datos
df = pd.read_csv("baseparaIA.csv")

# Asegúrate de que las columnas tengan los nombres correctos
columnas_totales = ["Total D1", "Total D2", "Total D3", "Total global"]

# Agrupar por sexo y calcular promedios
promedios_por_sexo = df.groupby("Sexo")[columnas_totales].mean().reset_index()

st.title("Dashboard de Promedios por Género")
st.write("Promedios de Total D1, Total D2, Total D3 y Total Global por género")

# --- Gráfica 1: Promedios por género (barplot general) ---
st.subheader("1. Promedio por Género (General)")
fig1, ax1 = plt.subplots()
promedios_por_sexo.set_index("Sexo")[columnas_totales].plot(kind="bar", ax=ax1)
ax1.set_ylabel("Promedio")
ax1.set_title("Promedios por Género en D1, D2, D3 y Total Global")
st.pyplot(fig1)

# --- Gráfica 2: Comparativa individual por dimensión ---
st.subheader("2. Comparativa por Dimensión")
fig2, axs2 = plt.subplots(2, 2, figsize=(12, 8))
axs2 = axs2.flatten()

for i, col in enumerate(columnas_totales):
    sns.barplot(x="Sexo", y=col, data=df, ax=axs2[i])
    axs2[i].set_title(f"Promedio por Género - {col}")
    axs2[i].set_ylabel("Promedio")

plt.tight_layout()
st.pyplot(fig2)

# --- Gráfica 3: Radar Chart ---
st.subheader("3. Gráfica de Radar por Género")

# Preparar datos para radar
categorias = columnas_totales
N = len(categorias)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

fig3 = plt.figure(figsize=(6, 6))
ax3 = plt.subplot(111, polar=True)

for i, sexo in enumerate(promedios_por_sexo["Sexo"]):
    valores = promedios_por_sexo.loc[i, columnas_totales].tolist()
    valores += valores[:1]
    ax3.plot(angles, valores, label=sexo)
    ax3.fill(angles, valores, alpha=0.25)

ax3.set_xticks(angles[:-1])
ax3.set_xticklabels(categorias)
ax3.set_title("Radar de Promedios por Género")
ax3.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
st.pyplot(fig3)
