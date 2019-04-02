# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:06:38 2019

@author: yanet
"""

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
import time
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols


orden=[8,16,32,64]
grafos=10
media=10
desviacion=3
parejas=5
repeticiones=1500


f=open('Reporte.txt','w')
f.write('Generador' + '\t' + 'Orden' + '\t' + 'Solucion' + '\t' + 'Pareja' +'\t' + 'Grafo' + '\n')
f.close()

for x1 in orden:
   
   for x2 in range(grafos):
      
      for x3 in range(parejas):
         
         
         T11=[]
         T12=[]
         T13=[]
         T21=[]
         T22=[]
         T23=[]
         T31=[]
         T32=[]
         T33=[]
         T41=[]
         T42=[]
         T43=[]
         
         for x4 in range(repeticiones):
              
            
            t1i=time.time()
            G = nx.grid_graph(dim=[x1, x1])
            t1f=time.time()
            
            K=[i for i in G.edges()]
            
            
            Pesos=[max(0.1,random.gauss(media,desviacion)) for i in range(len(K))]
        
            e=[]
            for i in range(len(G.edges())):
               
               a=(K[i][0],K[i][1],Pesos[i])  
               e.append(a)
            
            G.add_weighted_edges_from(e)
            
            
            #Seleccionar nodo fuente y nodo destino 
            buscar=True
            while buscar:
               
               origen1=random.randint(0, x1-1)
               origen2=random.randint(0, x1-1)
               destino1=random.randint(0, x1-1)
               destino2=random.randint(0, x1-1)
               
               if origen1==destino1 and origen2==destino2:
                  buscar=True
               else:
                  buscar=False
            
            
            
            
            t11i=time.time()
            min_cut=nx.minimum_cut(G,(origen1,origen2),(destino1,destino2),capacity='weight')
            t11f=time.time()
            
            
            t12i=time.time()
            cut_value = nx.minimum_cut_value(G, (origen1,origen2),(destino1,destino2),capacity='weight')            
            t12f=time.time()
            
            t13i=time.time()
            flow_value = nx.maximum_flow_value(G, (origen1,origen2),(destino1,destino2),capacity='weight')
            t13f=time.time()
            
            tcreacion1 = t1f-t1i
            
            ta1a1=t11f-t11i
            ta1a2=t12f-t12i
            ta1a3=t13f-t13i
            
            T11.append(tcreacion1 + ta1a1)
            T12.append(tcreacion1 + ta1a2)
            T13.append(tcreacion1 + ta1a3)
            
      
            
            
            t2i=time.time()
            H = nx.complete_graph(x1)
            t2f=time.time()
            
            K=[_ for _ in H.edges()]
            
            Pesos=[max(0.1,random.gauss(media,desviacion)) for _ in range(len(K))]
            
            e=[]
            for i in range(len(H.edges())):
               
               a=(K[i][0],K[i][1],Pesos[i])  
               e.append(a)
            
            H.add_weighted_edges_from(e)
            
            
            buscar=True
            while buscar:
               
               origen2=random.randint(0, x1-1)
               destino2=random.randint(0, x1-1)
               
               if origen2==destino2:
                  buscar=True
               else:
                  buscar=False
                  
            
          
            t21i=time.time()
            min_cut=nx.minimum_cut(H, origen2,destino2,capacity='weight')
            t21f=time.time()
            
            t22i=time.time()
            cut_value = nx.minimum_cut_value(H, origen2,destino2,capacity='weight')            
            t22f=time.time()
            
            t23i=time.time()
            flow_value = nx.maximum_flow_value(H,origen2,destino2,capacity='weight')
            t23f=time.time()
            
            tcreacion2 = t2f-t2i
            
            ta2a1=t21f-t21i
            ta2a2=t22f-t22i
            ta2a3=t23f-t23i
            
            T21.append(tcreacion2 + ta2a1)
            T22.append(tcreacion2 + ta2a2)
            T23.append(tcreacion2 + ta2a3)
            
       
            
            
           
            t3i=time.time()
            W= nx.wheel_graph(x1)
            t3f=time.time()
            
            K=[_ for _ in W.edges()]
            
           
            Pesos=[max(0.1,random.gauss(media,desviacion)) for _ in range(len(K))]
            
           
            e=[]
            for i in range(len(W.edges())):
               
               a=(K[i][0],K[i][1],Pesos[i])  
               e.append(a)
            
            W.add_weighted_edges_from(e)
            
            
            buscar=True
            while buscar:
               
               origen2=random.randint(0, x1-1)
               destino2=random.randint(0, x1-1)
               
               if origen2==destino2:
                  buscar=True
               else:
                  buscar=False
                  
            
            
            
           
            t31i=time.time()
            min_cut=nx.minimum_cut(W, origen2,destino2,capacity='weight')
            t31f=time.time()
            
            
            t32i=time.time()
            cut_value = nx.minimum_cut_value(W, origen2,destino2,capacity='weight')            
            t32f=time.time()
            
            
            t33i=time.time()
            flow_value = nx.maximum_flow_value(W,origen2,destino2,capacity='weight')
            t33f=time.time()
            
            tcreacion3 = t3f-t3i
            
            ta3a1=t31f-t31i
            ta3a2=t32f-t32i
            ta3a3=t33f-t33i
            
            T31.append(tcreacion3 + ta3a1)
            T32.append(tcreacion3 + ta3a2)
            T33.append(tcreacion3 + ta3a3)
            
            
            
            t4i=time.time()
            H = nx.circular_ladder_graph(x1)
            t4f=time.time()
            
            K=[_ for _ in H.edges()]
            
            Pesos=[max(0.1,random.gauss(media,desviacion)) for _ in range(len(K))]
            
            e=[]
            for i in range(len(H.edges())):
               
               a=(K[i][0],K[i][1],Pesos[i])  
               e.append(a)
            
            H.add_weighted_edges_from(e)
            
            
            buscar=True
            while buscar:
               
               origen2=random.randint(0, x1-1)
               destino2=random.randint(0, x1-1)
               
               if origen2==destino2:
                  buscar=True
               else:
                  buscar=False
                  
            
          
            t41i=time.time()
            min_cut=nx.minimum_cut(H, origen2,destino2,capacity='weight')
            t41f=time.time()
            
            t42i=time.time()
            cut_value = nx.minimum_cut_value(H, origen2,destino2,capacity='weight')            
            t42f=time.time()
            
            t43i=time.time()
            flow_value = nx.maximum_flow_value(H,origen2,destino2,capacity='weight')
            t43f=time.time()
            
            tcreacion2 = t4f-t4i
            
            ta4a1=t41f-t41i
            ta4a2=t42f-t42i
            ta4a3=t43f-t43i
            
            T41.append(tcreacion2 + ta4a1)
            T42.append(tcreacion2 + ta4a2)
            T43.append(tcreacion2 + ta4a3)
            
            
         
         media11=np.sum(T11)
         media12=np.sum(T12)
         media13=np.sum(T13)
         
         media21=np.sum(T21)
         media22=np.sum(T22)
         media23=np.sum(T23)
         
         media31=np.sum(T31)
         media32=np.sum(T32)
         media33=np.sum(T33)
         
         media41=np.sum(T41)
         media42=np.sum(T42)
         media43=np.sum(T43)
         
         
         f=open('Reporte.txt','a')
         f.write(str(1) + '\t' + str(x1) + '\t' + str(1) + '\t' + str(x3) + '\t' + str(x2) +'\t' + str(media11) +'\n')
         f.write(str(1) + '\t' + str(x1) + '\t' + str(2) + '\t' + str(x3) + '\t' + str(x2) +'\t' + str(media12)+ '\n')
         f.write(str(1) + '\t' + str(x1) + '\t' + str(3) + '\t' + str(x3) + '\t' + str(x2) +'\t' + str(media13)+ '\n')
         f.write(str(2) + '\t' + str(x1) + '\t' + str(1) + '\t' + str(x3) + '\t' + str(x2) +'\t' + str(media21)+ '\n')
         f.write(str(2) + '\t' + str(x1) + '\t' + str(2) + '\t' + str(x3) + '\t' + str(x2) +'\t' + str(media22)+ '\n')
         f.write(str(2) + '\t' + str(x1) + '\t' + str(3) + '\t' + str(x3) + '\t' + str(x2) +'\t' + str(media23)+ '\n')
         f.write(str(3) + '\t' + str(x1) + '\t' + str(1) + '\t' + str(x3) + '\t' + str(x2) +'\t' + str(media31)+ '\n')
         f.write(str(3) + '\t' + str(x1) + '\t' + str(2) + '\t' + str(x3) + '\t' + str(x2) +'\t' + str(media32)+ '\n')
         f.write(str(3) + '\t' + str(x1) + '\t' + str(3) + '\t' + str(x3) + '\t' + str(x2) +'\t' + str(media33)+ '\n')
         f.close()   

'''
-------------------------------------------------------------------------------
BOXPLOT Y ANOVA
-------------------------------------------------------------------------------
'''


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
#for i in range(len(Anova)):
#    print("{:s} {:s}es significativo".format(Anova.index[i], "" if Anova['PR(>F)'][i] < 0.05 else "NO "))
