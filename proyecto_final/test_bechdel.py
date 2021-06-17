# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 11:37:56 2021

@author: joana
"""

import pandas as pd
import numpy as np
from typing import Set, Any 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("movies.csv") #leer el archivo

    
def remove_others(df: pd, columns: Set[Any]): #funcion para remover columnas
    cols_total: Set[Any] = set(df.columns)
    diff: Set[Any] = cols_total - columns
    df.drop(diff, axis=1, inplace=True)
    
remove_others(df, {"year", "clean_test", "binary"}) #remover todas menos

df = df[df.clean_test != "dubious"] #remover la opcion dubious

n = (pd.unique(df['year'])) #establecer el rango de los años
n = n[0:-10] #de 1980 a 2013


dfs = [] #lista para los dataframes ya editados
for i in n: #ciclo para leer todos los años
    df1 = df[df['year'] == i]
    dfs.append(df1) #guardar los dataframes en la lista

ratios = [] #
count = 0
count_nt = 0
count_ok = 0
count_nw = 0
count_men = 0

for df in dfs:
    for i in (df['binary']):
        if i ==  'PASS':
            count += 1
        
    ratio = count/len(df['binary'])
    ratios.append(ratio)
    count = 0
    for j in (df['clean_test']):
        if j == 'notalk':
            count_nt += 1
    
        if j == 'ok':
            count_ok += 1
    
        if j == 'nowomen':
            count_nw += 1
            
        if j == 'men':
            count_men += 1
    

labels = 'ok', 'notalk',  'nowomen', 'men'
sizes = [count_ok, count_nt, count_nw, count_men]
colors = ['#F16A70','#B1D877','#8CDCDA','#4D4D4D']
explode = (0.1, 0, 0, 0)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, colors=colors, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
ax1.axis('equal')  

plt.savefig("reglas_pastel.png")
plt.show()

ratios = np.array(ratios)
n = np.array(n)

model = LinearRegression().fit(n.reshape(-1,1), ratios)
pred_2015 = np.array([2015]) 
prediccion = model.predict(pred_2015.reshape(-1,1))
Y_pred = model.predict(n.reshape(-1,1))

plt.scatter(n, ratios)
plt.plot(n, Y_pred, color='red')
plt.xlabel('Años', fontsize=14)
plt.ylabel('Ratios', fontsize=14)

plt.savefig("prediccion.png")
plt.show()

print("La prediccion para el 2015 es:", round(float(prediccion*100), 1),"%")
