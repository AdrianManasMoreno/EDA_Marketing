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
  
def analyze_ctr_without_outliers(data, no_outliers = False):
    """
    Función que analiza el CTR sin los outliers
    """
    if no_outliers == True:
      #Analisis del CTR por campaña y canal
      ctr_by_campaign = data.groupby('campaign_type')['CTR'].mean().sort_values(ascending=False) # CTR por campaña
      ctr_by_channel = data.groupby('channel_used')['CTR'].mean().sort_values(ascending=False) # CTR por canal
    else:
      ctr_by_campaign = data.groupby('campaign_type')['CTR'].median().sort_values(ascending=False) # CTR por campaña
      ctr_by_channel = data.groupby('channel_used')['CTR'].median().sort_values(ascending=False) # CTR por canal
      
    print("CTR promedio por campaña:")
    print(ctr_by_campaign, "\n")
    print("CTR promedio por canal:")
    print(ctr_by_channel, "\n")
    
    #Crear el subplot
    fig, axs = plt.subplots(1, 2, figsize=(16, 6))
    
    #Primer grafico CTR por tipo de campaña
    sns.barplot(x=ctr_by_campaign.index, y=ctr_by_campaign.values, palette='coolwarm', hue=ctr_by_campaign.index, ax=axs[0])
    axs[0].set_title('CTR promedio por campaña')
    axs[0].set_xticklabels(ctr_by_campaign.index, rotation=45)
    axs[0].tick_params(axis='x', labelsize=10)
    axs[0].tick_params(axis='y', labelsize=10)
    
    #Segundo grafico CTR por canal
    sns.barplot(x=ctr_by_channel.index, y=ctr_by_channel.values, palette='viridis', hue=ctr_by_channel.index, ax=axs[1])
    axs[1].set_title('CTR promedio por canal')
    axs[1].set_xticklabels(ctr_by_channel.index, rotation=45)
    axs[1].tick_params(axis='x', labelsize=10)
    axs[1].tick_params(axis='y', labelsize=10)
    
    #Ajustar el layout para que los titulos y etiquetas no se solapen
    plt.tight_layout()

def analyze_conversion_metrics(data, no_outliers = False):
  metrics = ['conversion_cost', 'conversion_value']
  if no_outliers == True:
    for metric in metrics:
    #Analisis del CTR por campaña y canal
      metric_by_channel = data.groupby('channel_used')[metric].mean().sort_values(ascending=False)
      metric_by_segment = data.groupby('customer_segment')[metric].mean().sort_values(ascending=False)
    
      print(f"{metric.capitalize()} promedio por canal utilizado")
      print(metric_by_channel, "\n")
      print(f"{metric.capitalize()} promedio por segmento de cliente")
      print(metric_by_segment, "\n")
  else:
    for metric in metrics:
    #Analisis del CTR por campaña y canal
      metric_by_channel = data.groupby('channel_used')[metric].median().sort_values(ascending=False)
      metric_by_segment = data.groupby('customer_segment')[metric].median().sort_values(ascending=False)
    
      print(f"{metric.capitalize()} promedio por canal utilizado")
      print(metric_by_channel, "\n")
      print(f"{metric.capitalize()} promedio por segmento de cliente")
      print(metric_by_segment, "\n")
      
  #Crear el subplot de Visualizacion
  fig, axs = plt.subplots(1, 2, figsize=(16, 6))
    
  #Primer grafico, metrica promedio por canal
  sns.barplot(x=metric_by_channel.index, y=metric_by_channel.values, palette='muted', ax=axs[0])
  axs[0].set_title(f"{metric.capitalize()} promedio por canal utilizado")
  axs[0].set_xticklabels(metric_by_channel.index, rotation=45)
  axs[0].tick_params(axis='x', labelsize=10)
  axs[0].tick_params(axis='y', labelsize=10)
    
  #Segundo grafico, metrica promedio por segmento de cliente
  sns.barplot(x=metric_by_segment.index, y=metric_by_segment.values, palette='cubehelix', ax=axs[1])
  axs[1].set_title(f"{metric.capitalize()} promedio por cliente")
  axs[1].set_xticklabels(metric_by_channel.index, rotation=45)
  axs[1].tick_params(axis='x', labelsize=10)
  axs[1].tick_params(axis='y', labelsize=10)
    
  #Ajustar el layout para que los titulos y etiquetas no se solapen
  plt.tight_layout()