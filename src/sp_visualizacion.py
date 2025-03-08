import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def subplot_col_cat(df):
  """
  Función que crea un subplot de visualizacion con la distribución de las columnas categóricas
  """
  #Variable de las columnas categoricas
  col_catg = df.select_dtypes(include=['O', 'category']).columns
  
  if len(col_catg) == 0:
    print('No hay columnas categoricas en el DataFrame')
    return
  
  #Configuracion del tamaño de la figura
  num_cols = len(col_catg)
  num_filas = (num_cols + 2) // 3 #calcular el número de filas necesarias
  fig, axes = plt.subplots(num_filas, 3, figsize=(15, num_filas * 5))
  axes = axes.flatten() #convertir los ejes a un array de una 1d plano para facilitar la iteración
  
  #Generar graficos para cada columna categorica
  for i, col in enumerate(col_catg):
      sns.countplot(data=df, 
                    x=col, 
                    ax=axes[i],
                    hue=col,
                    palette="tab10",
                    legend=False)
      axes[i].set_title(f'Distribución de {col}')
      axes[i].set_xlabel(col)
      axes[i].set_ylabel('Frecuencia')
      axes[i].tick_params(axis='x', rotation=90) #rotar etiquitas si es necesario
  #Elimina ejes sbrantes si hay menos columnas que subplots
  for j in range(i + 1, len(axes)):
      fig.delaxes(axes[j])
  #Ajustar el espacio entre los subplots
  fig.tight_layout()
  plt.show()