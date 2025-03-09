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

def subplot_col_num (df, col):
  num_graph = len(col) # Número de gráficos a mostrar
  num_rows = (num_graph +2) // 2 # Número de filas
  fig, axes = plt.subplots(num_graph, 2, figsize=(15, 5 * num_rows)) # Definimos la figura

  for i, col in enumerate(col):
    sns.histplot(data = df, 
                x = col, 
                kde = True, 
                ax = axes[i,0], bins=200)# Creamos el histograma
    axes[i,0].set_title(f'Distribucion de {col}') # Añadimos el título
    axes[i,0].set_ylabel('Frecuencia') # Añadimos la etiqueta del eje y
    
    sns.boxplot(data = df,
                x = col,  
                ax = axes[i,1])# Creamos el histograma
    axes[i,1].set_title(f'Boxplot de {col}') # Añadimos el título


  for j in range(i+1, len(axes)):
    fig.delaxes(axes[j]) # Eliminamos los ejes que no vamos a usar
    
  plt.tight_layout()
  plt.show()