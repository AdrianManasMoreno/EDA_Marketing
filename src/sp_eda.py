import pandas as pd
import numpy as np

def calcular_nulos(df):
    """
    Función que calcula el número y porcentaje de valores nulos en un DataFrame
    :param df: DataFrame
    """
    numero_nulos = df.isnull().sum()
    porcentaje_nulos = round((df.isnull().sum() / df.shape[0]) * 100, 2)
    return numero_nulos, porcentaje_nulos

def analisis_general_categoricas(df):
    """
    Función que realiza un análisis general de las columnas categóricas de un DataFrame
    """
    col_cat = df.select_dtypes(include="O").columns
    
    if len(col_cat) == 0:
        print("No hay columnas categóricas en el DataFrame")
    else:
        for col in col_cat:
            print(f"La distribucion de la columna {col.upper()}")
            print(f"Esta columna tiene {len(df[col].unique())} valores únicos")
            display (df[col].value_counts(normalize=True))
            print("____________\n Describe")
            display(df[col].describe())
            print("---------------------------------")