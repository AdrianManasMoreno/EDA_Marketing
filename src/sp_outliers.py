import pandas as pd
import numpy as np

def count_outliers(data, columns):
  """
  Función que cuenta los outliers de un conjunto de datos.
  """
  outliers_count = {}
  outliers_percent = {}
  for col in columns:
    Q1 = data[col].quantile(0.25) # Primer cuartil
    Q3 = data[col].quantile(0.75) # Tercer cuartil
    IQR = Q3 - Q1 # Rango intercuartílico
    lower_bound = Q1 - 1.5 * IQR # Límite inferior
    upper_bound = Q3 + 1.5 * IQR # Límite superior
    outliers = data[(data[col] < lower_bound) | (data[col] > upper_bound)] # Filtrar outliers
    outliers_count[col] = outliers.shape[0] # Contar outliers
    outliers_percent[col] = round(outliers.shape[0] / data.shape[0], 3) # Porcentaje de outliers
  return outliers_count, outliers_percent

def filter_no_outliers(data, lista_columnas):
  data_filtered = data.copy()
  for col in lista_columnas:
    Q1 = data[col].quantile(0.25) # Primer cuartil
    Q3 = data[col].quantile(0.75) # Tercer cuartil
    IQR = Q3 - Q1 # Rango intercuartílico
    lower_bound = Q1 - 1.5 * IQR # Límite inferior
    upper_bound = Q3 + 1.5 * IQR # Límite superior
    data_filtered = data_filtered[(data_filtered[col] >= lower_bound) & (data_filtered[col] <= upper_bound)]
  return data_filtered