import pandas as pd
import numpy as np

def calcular_solo_col_nul(df, umbral=10):
    """
    Función que calcula el porcentaje de nulos por columna y muestra las columnas con un porcentaje de nulos mayor al umbral.
    """
    columns_with_nulls = df.columns[df.isnull().any()]
    null_columns_info = pd.DataFrame(
      {"Column": columns_with_nulls,
       "Datatype": [df[col].dtype for col in columns_with_nulls],
       "NullCount": [df[col].isnull().sum() for col in columns_with_nulls],
       "Null%": [((df[col].isnull().sum() / df.shape[0]) * 100) for col in columns_with_nulls]}
    )
    
    display(null_columns_info) # Mostrar información de columnas con nulos
    high_null_cols = null_columns_info[null_columns_info["Null%"] > umbral]['Column'].tolist() # Filtrar por umbral con alto porcentaje de nulos
    low_null_cols = null_columns_info[null_columns_info["Null%"] <= umbral]['Column'].tolist() # Filtrar por umbral con bajo porcentaje de nulos
    return high_null_cols, low_null_cols
  
def imputar_iterative(df, lista_columnas):
  """
  Función que rellena los nulos de un dataframe con el método IterativeImputer
  """
  iter_imputer = IterativeImputer(max_iter=50, random_state=42) # Creamos el objeto IterativeImputer
  data_imputed = iter_imputer.fit_transform(df[col_high_umbral]) # Rellenamos los nulos con el objeto IterativeImputer
  new_col = [col + "_iterative" for col in lista_columnas] # Creamos una lista con los nombres de las nuevas columnas
  df[new_col] = data_imputed # Añadimos las nuevas columnas al dataframe
  display(df[new_col].describe().T) # Mostramos el resumen estadístico de las nuevas columnas
  return df, new_col