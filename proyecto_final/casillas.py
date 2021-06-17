# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 12:58:02 2021

@author: joana
"""

import numpy as np
import pandas as pd  
import math
from sklearn.linear_model import LinearRegression
import glob

path = r'C:\Users\joana\Desktop\INE' # use la ruta pertinente
all_files = glob.glob(path + "/*.csv")

li = []
count = 0

for filename in all_files: #leer todos los archivos 
    df = pd.read_csv(filename, index_col=None, thousands=',')
    
    #se hacen dos ciclos for porque sólo se necesitaban leer las primeras dos
    #columnas en el primer archivo
    
    for column in df: #leer todas las columnas y eliminar aquellas diferentes
        if column == 'ENTIDAD':
            pass
        elif column == 'MUNICIPIO':
            pass
        elif column == 'SECCION':
            pass
        elif column == 'LISTA':
            pass
        elif column == 'TOTAL_LISTA':
            pass
        else:
            df= df.drop([column], axis=1) #con esta función se eliminan
        
    df = df[df.ENTIDAD == 11] #eliminar todas las filas que no son de GTO
    
    if count != 0: #leer todas las columnas y eliminar aquellas diferentes
        for column in df: 
            if column == 'LISTA':
                pass
            elif column == 'TOTAL_LISTA':
                pass
            else:
                df= df.drop([column], axis=1) #con esta funcion se eliminan
    count = 1
    df= df.drop(df.index[3142:])
    df.reset_index(drop=True, inplace=True)
    li.append(df)

df = pd.concat(li, axis=1) #concatenamos los 16 archivos en li y guardamos en df
df = df.drop(df.index[0]) #eliminamos la primera fila de extranjeros

data = np.array(df)
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
regresion_lineal = LinearRegression()
predicciones = []
for i in range (len(data)):

    y = data[i, 3:].reshape(-1,1)  # values converts it into a numpy array
    regresion_lineal.fit(x.reshape(-1,1), y) 
    nuevo_x = np.array([17]) 
    predicciones.append(math.ceil(float(regresion_lineal.predict(nuevo_x.reshape(-1,1)))))
    
casillas = []

for prediccion in predicciones:
    casillas.append(math.ceil(prediccion/750))

print(sum(casillas))
