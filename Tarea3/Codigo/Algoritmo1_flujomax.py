# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 09:18:55 2019

@author: yanet
"""
import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np
import time

'''
------------------------------------------------------------------------------
Grafo 10
'''
G=nx.DiGraph()

A=[(1,2,{'peso':15}),(2,3,{'peso':5}),(2,4,{'peso':1}),(3,4,{'peso':3}),(4,5,{'peso':9})]
G.add_edges_from(A)

pos =nx.spectral_layout(G)
Tiempos=[]
for i in range(30):
    T1=0
    for j in range(15000):
        t1=time.time()
valor_flujo, flujo_max =nx.maximum_flow(G,1,5,capacity = 'peso') 
        t2=time.time()
        T=t2-t1
        T1=T1+T
        
    Tiempos.append(T1)               
    print('Tiempo total de repeticiones: ',T1)

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)

flujo=[]
pesos=nx.get_edge_attributes(G,'peso')
pesos1=[pesos[i] for i in pesos]
for i in flujo_max.keys():
    for j in flujo_max[i].keys():
        flujo.append(flujo_max[i][j])
        
Arcos=[i for i in G.edges]
s_flujo={Arcos[i]:(pesos1[i],flujo[i]) for i in range(len(Arcos))}


nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4,5],node_color='b', node_size=400)
nx.draw_networkx_edges(G,pos,width=3,edgelist=A,alpha=1, edge_color='c')
#nx.draw_networkx_edges(G,pos,width=3,edgelist=[(8,7),(7,1)],alpha=1,edge_color='r')
nx.draw_networkx_edge_labels(G, pos,edge_labels=s_flujo)
nx.draw_networkx_labels(G, pos,font_color='w')
plt.axis('off')
plt.savefig("MDA.eps")
plt.show(1)

f = open ('Reporte1.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()

'''
-------------------------------------------------------------------------------
Grafo 2
'''
G=nx.DiGraph()  

A=[(1,2,{'peso':3}),(2,3,{'peso':6}),(3,4,{'peso':4}),(5,4,{'peso':7}),(6,5,{'peso':9}),(1,6,{'peso':5}),(2,5,{'peso':1},),(7,1,{'peso':10}),(8,7,{'peso':15})]

G.add_edges_from(A)
pesos=nx.get_edge_attributes(G,'peso')
pos= nx.circular_layout(G)

Tiempos=[]
for i in range(30):
    T1=0
    for j in range(15000):
        t1=time.time()
        valor_flujo, flujo_max =nx.maximum_flow( G , 8, 4, capacity = 'peso' , flow_func = None) 
        t2=time.time()
        T=t2-t1
        T1=T1+T
    Tiempos.append(T1)  
    print('Tiempo total de repeticiones: ',T1)

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)

flujo=[]
pesos=nx.get_edge_attributes(G,'peso')
pesos1=[pesos[i] for i in pesos]
for i in flujo_max.keys():
    for j in flujo_max[i].keys():
        flujo.append(flujo_max[i][j])
Arcos=[i for i in G.edges]
s_flujo={Arcos[i]:(pesos1[i],flujo[i]) for i in range(len(Arcos))}
        
nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4,5,6,7,8],node_color='yellow', node_size=200, node_shape='s')
nx.draw_networkx_edges(G,pos,width=2,edgelist=[(2,5)],alpha=1,edge_color='b')
nx.draw_networkx_edges(G,pos,width=2,edgelist=[(8,7),(7,1),(1,6),(1,2),(6,5),(5,4),(2,3),(3,4)],alpha=1,edge_color='c')
nx.draw_networkx_labels(G,pos)
nx.draw_networkx_edge_labels(G, pos,edge_labels=s_flujo,font_color='r')

plt.axis('off')
plt.savefig("GNC.eps")
plt.show(2)

f = open ('Reporte1.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()

'''
-------------------------------------------------------------------------------
Grafo 4
'''
G=nx.DiGraph()  
V={0:(-2,0.2),1:(-1,0.2),2:(0,0.2),3:(0,0),4:(1,0.2),5:(1,0),6:(1.5,-0.2),7:(2,0.2),8:(2.5,0),9:(4,0),10:(5,0)}
A=[(0,1,{'peso':20}),(1,2,{'peso':6}),(2,3,{'peso':2}),(3,4,{'peso':8}),(3,5,{'peso':10}),(3,6,{'peso':12}),(4,7,{'peso':1}),(5,8,{'peso':12}),(8,6,{'peso':3}),(7,9,{'peso':7}),(9,10,{'peso':4}),(1,3,{'peso':9})]
G.add_edges_from(A)
pesos=nx.get_edge_attributes(G,'peso')

Tiempos=[]

for i in range(30):
    T1=0
    for j in range(15000):
        t1=time.time()
        valor_flujo, flujo_max =nx.maximum_flow( G , 0, 10, capacity = 'peso' , flow_func = None) 
        t2=time.time()
        T=t2-t1
        T1=T1+T
    Tiempos.append(T1)  
    print('Tiempo total de repeticiones: ',T1)

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)

flujo=[]
pesos=nx.get_edge_attributes(G,'peso')
pesos1=[pesos[i] for i in pesos]
for i in flujo_max.keys():
    for j in flujo_max[i].keys():
        flujo.append(flujo_max[i][j])
Arcos=[i for i in G.edges]
s_flujo={Arcos[i]:(pesos1[i],flujo[i]) for i in range(len(Arcos))}
        
nx.draw_networkx_nodes(G,V,nodelist=[0,1,2,3,4,5,6,7,8,9,10],node_color='m', node_size=200)
nx.draw_networkx_edges(G,V,width=2,edgelist=A,alpha=1,edge_color='b')
nx.draw_networkx_labels(G,V)
nx.draw_networkx_edge_labels(G, V,edge_labels=s_flujo,font_color='c',font_size=7)

plt.axis('off')
plt.savefig("GDA.eps")
plt.show(3)

f = open ('Reporte1.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()

'''
-------------------------------------------------------------------------------
Grafo 5
'''

G=nx.DiGraph()  
A=[(0,1,{'peso':12}),(1,2,{'peso':5}),(2,3,{'peso':7}),(3,4,{'peso':6}),(4,0,{'peso':8}),(0,5,{'peso':12}),(5,6,{'peso':5}),(6,7,{'peso':4}),(7,8,{'peso':10}),(8,0,{'peso':8})]
G.add_edges_from(A)
pesos=nx.get_edge_attributes(G,'peso')

pos=nx.spring_layout(G, iterations=100)

Tiempos=[]

for i in range(1):
    T1=0
    for j in range(15000):
        t1=time.time()
        valor_flujo, flujo_max =nx.maximum_flow( G , 0, 8, capacity = 'peso' , flow_func = None) 
        t2=time.time()
        T=t2-t1
        T1=T1+T
    Tiempos.append(T1)
    print('Tiempo total de repeticiones: ',T1)

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)

flujo=[]
pesos=nx.get_edge_attributes(G,'peso')
pesos1=[pesos[i] for i in pesos]
for i in flujo_max.keys():
    for j in flujo_max[i].keys():
        flujo.append(flujo_max[i][j])
Arcos=[i for i in G.edges]
s_flujo={Arcos[i]:(pesos1[i],flujo[i]) for i in range(len(Arcos))}
        
labels={0:'D',8:'F'}
pos=nx.spring_layout(G, iterations=100)
nx.draw_networkx_nodes(G,pos,nodelist=[0],node_shape='s',node_color='b', node_size=300)
nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4],node_color='pink')
nx.draw_networkx_nodes(G,pos,nodelist=[5,6,7],node_color='c')
nx.draw_networkx_nodes(G,pos,nodelist=[8],node_color='b',node_shape='s',node_size=300)
nx.draw_networkx_edges(G,pos,width=2,edgelist=A,alpha=1,arrowsize=25)
nx.draw_networkx_labels(G,pos,labels,front_size=12,font_color='w')
nx.draw_networkx_edge_labels(G, pos,edge_labels=s_flujo,font_color='r',font_size=8)
plt.axis('off')
plt.savefig("GDC.eps")
plt.show(4)

f = open ('Reporte1.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()

''''
------------------------------------------------------------------------------
Grafo 8
'''

G=nx.DiGraph()

A=[(1,2,{'peso':4}),(3,4,{'peso':8}),(1,3,{'peso':1}),(3,2,{'peso':12}),(2,4,{'peso':6}),(4,1,{'peso':7})]
G.add_edges_from(A)
pesos=nx.get_edge_attributes(G,'peso')

pos = nx.bipartite_layout(G,{1,4}, scale=0.2)

Tiempos=[]

for i in range(30):
    T1=0
    for j in range(15000):
        t1=time.time()
        valor_flujo, flujo_max =nx.maximum_flow( G , 4, 2, capacity = 'peso' , flow_func = None) 
        t2=time.time()
        T=t2-t1
        T1=T1+T
    Tiempos.append(T1)
    print('Tiempo total de repeticiones: ',T1)

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)

flujo=[]
pesos=nx.get_edge_attributes(G,'peso')
pesos1=[pesos[i] for i in pesos]
for i in flujo_max.keys():
    for j in flujo_max[i].keys():
        flujo.append(flujo_max[i][j])
Arcos=[i for i in G.edges]
s_flujo={Arcos[i]:(pesos1[i],flujo[i]) for i in range(len(Arcos))}
        
labels={1:'México', 3: 'Nayarit', 4: 'Cancún' }
labels1={2:'Monterrey'}
nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4],node_color='b',node_shape='p')
nx.draw_networkx_edges(G,pos,width=1,edgelist=A,alpha=1)
nx.draw_networkx_edges(G,pos,width=3,edgelist=[(3,2)],alpha=1,edge_color='r',size=0.1)
nx.draw_networkx_edge_labels(G, pos,edge_labels=s_flujo,font_color='r',font_size=8, label_pos=0.56)
pos1=pos
for i in pos:
    pos1[i][1]=pos1[i][1]+0.04
nx.draw_networkx_labels(G,pos,labels, font_size=12)
for i in pos:
    pos1[i][1]=pos1[i][1]-0.08
nx.draw_networkx_labels(G,pos,labels1, font_size=12)
plt.axis('off')
plt.savefig("MNC.eps")
plt.show(5)

f = open ('Reporte1.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()