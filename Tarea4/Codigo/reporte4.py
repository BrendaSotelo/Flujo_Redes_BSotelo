# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:51:25 2019

@author: yanet
"""

import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt

Data=pd.read_csv('T4.csv',header= None)
Data.columns=['Generador','Orden','Algoritmo','Parejas','Grafo','Densidad','Tiempo']

sns.boxplot(x='Generador',y='Tiempo',data=Data)
plt.savefig("box1.eps")
plt.show()

sns.boxplot(x='Algoritmo',y='Tiempo',data=Data)
plt.savefig("box2.eps")
plt.show()

sns.boxplot(x='Orden',y='Tiempo',data=Data)
plt.savefig("box3.eps")
plt.show()

sns.boxplot(x='Densidad',y='Tiempo',data=Data)
plt.savefig("box4.eps")
plt.show()

modelo=ols('Tiempo~Generador+Algoritmo+Orden+Densidad+Generador*Algoritmo+Generador*Orden+Generador*Densidad+Algoritmo*Orden+Algoritmo*Densidad+Orden*Densidad',data=Data).fit()


Anova=sm.stats.anova_lm(modelo,typ=2)
print(Anova)
for i in range(len(Anova)):
    print("{:s} {:s}es significativo".format(Anova.index[i], "" if Anova['PR(>F)'][i] < 0.05 else "NO "))

print()