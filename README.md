import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración inicial
st.set_page_config(page_title="Dashboard de Promedios", layout="wide")
st.title("Análisis de Promedios por Género")
st.markdown("### Basado en las columnas C, D, E y F")

# Cargar datos
@st.cache_data
def cargar_datos():
    return pd.read_csv("baseparaIA.csv")

df = cargar_datos()

# Verifica que las columnas necesarias existan
columnas_datos = ['C', 'D', 'E', 'F']
if 'Genero' not in df.columns or not all(col in df.columns for col in columnas_datos):
    st.error("Asegúrate de que el archivo contenga la columna 'Genero' y las columnas C, D, E, F.")
    st.stop()

# Agrupar por género y calcular promedios
promedios = df.groupby('Genero')[columnas_datos].mean().reset_index()

# Gráfica 1: Barras
st.subheader("Gráfica de Barras: Promedio por Género")
fig1, ax1 = plt.subplots()
promedios.set_index('Genero').plot(kind='bar', ax=ax1)
plt.ylabel("Promedio")
st.pyplot(fig1)

# Gráfica 2: Líneas
st.subheader("Gráfica de Líneas: Comparativa de Promedios")
fig2, ax2 = plt.subplots()
for genero in promedios['Genero']:
    ax2.plot(columnas_datos, promedios[promedios['Genero'] == genero][columnas_datos].values.flatten(), label=genero)
ax2.set_ylabel("Promedio")
ax2.set_xlabel("Columnas")
ax2.legend()
st.pyplot(fig2)

# Gráfica 3: Boxplot o violín (datos individuales para más detalle)
st.subheader("Gráfica de Violín: Distribución por Género")
fig3, ax3 = plt.subplots(figsize=(10, 5))
df_melt = df.melt(id_vars='Genero', value_vars=columnas_datos, var_name='Variable', value_name='Valor')
sns.violinplot(data=df_melt, x='Variable', y='Valor', hue='Genero', split=True, ax=ax3)
st.pyplot(fig3)
