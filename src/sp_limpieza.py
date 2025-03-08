import pandas as pd
import numpy as np

def eda_preliminar(df):
    """
    Esta función realiza un análisis exploratorio de datos preliminar
    """
    display (df.sample(5))
    print('-------------------')
    print('INFO')
    display(df.info())
    print('-------------------')
    print('NULOS')
    display(round(df.isnull().sum()/df.shape[0]*100,2))
    print('-------------------')
    print('DUPLICADOS')
    print(df.duplicated().sum())
    print('-------------------')
    print('VALUE COUNTS')
    for col in df.columns:
        print(df[col].value_counts())
        print('-------------------')
        
def valores_minusculas(df):
    """
    Esta función convierte a minúsculas los valores de las columnas de tipo object de un DataFrame
    """
    for col in df.select_dtypes(include='object').columns: # Selecciona las columnas de tipo object
      df[col] = df[col].str.lower() # Convierte a minúsculas

def dolares (df, lista_col):
    """
    Esta función elimina el signo $ y las comas de los valores de las columnas de un DataFrame
    """
    for col in lista_col:
        df[col] = df[col].str.replace('$','').str.replace(',','')
        
def comas (df, lista_col):
    """
    Esta función reemplaza las comas por puntos en los valores de las columnas de un DataFrame
    """
    for col in lista_col:
        df[col] = df[col].str.replace(',','.')

def convertir_columnas (df,formato_fecha):
    """
    Esta función convierte las columnas de un DataFrame a los tipos de datos correspondientes
    """
    for col in df.columns:
        for dtype in [float,int]:
            try:
                df[col] = df[col].astype(dtype)
            except:
                pass
        try:
            df[col] = pd.to_datetime(df[col], format=formato_fecha)
        except:
            pass

def quitar_espacios (df):
    """
    Esta función reemplaza los espacios en blanco por guiones bajos en los nombres de las columnas de un DataFrame
    """
    for col in df.columns:
        try:
            df[col] = df[col].str.replace(' ', '_')
        except:
            pass