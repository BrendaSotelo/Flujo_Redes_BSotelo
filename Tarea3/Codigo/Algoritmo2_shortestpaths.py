# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:20:58 2019

@author: yanet
"""
import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np
import time
'''
GRAFO 10
'''
G=nx.DiGraph()

A=[(1,2,{'peso':15}),(2,3,{'peso':5}),(2,4,{'peso':1}),(3,4,{'peso':3}),(4,5,{'peso':9})]
G.add_edges_from(A)
pesos=nx.get_edge_attributes(G,'peso')
pos =nx.spectral_layout(G)

Tiempos=[]
for i in range(30):
    T1=0
    for j in range(300000):
        t1=time.time()
R = [p for p in nx.all_shortest_paths(G, source=1, target=5,weight='peso')]
        t2=time.time()
        T=t2-t1
        T1=T1+T
    Tiempos.append(T1)  
    print('Tiempo total de repeticiones: ',T1)

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)

Arcos=[(R[0][i],R[0][i+1]) for i in range(len(R[0])-1)]

nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4,5],node_color='b', node_size=300)
nx.draw_networkx_edges(G,pos,width=2,edgelist=[(1,2),(2,3),(4,5),(2,4),(3,4)],alpha=1, edge_color='black')
nx.draw_networkx_edge_labels(G, pos,edge_labels=pesos,font_color='b')
nx.draw_networkx_labels(G, pos,font_color='w')
nx.draw_networkx_edges(G,pos,edgelist=Arcos,edge_color='c',width=3)
plt.axis('off')
plt.savefig("A2G1.eps")
plt.show(1)

f = open ('Reporte2.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()
'''
GRAFO 2
'''
G=nx.Graph()  

A=[(1,2,{'peso':6}),(2,3,{'peso':12}),(3,4,{'peso':4}),(4,5,{'peso':3}),(5,6,{'peso':8}),(1,6,{'peso':10}),(2,5,{'peso':2},),(1,7,{'peso':5}),(7,8,{'peso':6})]

G.add_edges_from(A)
pesos=nx.get_edge_attributes(G,'peso')
pos= nx.fruchterman_reingold_layout(G, iterations=1000)

Tiempos=[]
for i in range(30):
    T1=0
    for j in range(300000):
        t1=time.time()
        R = [p for p in nx.all_shortest_paths(G, source=4, target=8,weight='peso')]
        t2=time.time()
        T=t2-t1
        T1=T1+T
    Tiempos.append(T1)  
    print('Tiempo total de repeticiones: ',T1)   

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)
   
Arcos=[(R[0][i],R[0][i+1]) for i in range(len(R[0])-1)]

nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4,5,6,7,8],node_color='yellow', node_size=300)
nx.draw_networkx_edges(G,pos,width=1,edgelist=A,alpha=1)
nx.draw_networkx_labels(G,pos,font_color='black')
nx.draw_networkx_edge_labels(G, pos,edge_labels=pesos,font_color='b')
nx.draw_networkx_edges(G,pos,edgelist=Arcos,edge_color='c',width=3)

plt.axis('off')
plt.savefig("A2G2.eps")
plt.show(2)

f = open ('Reporte2.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()
'''
GRAFO 4
'''
G=nx.Graph()  

V={0:(-2,0.2),1:(-1,0.2),2:(0,0.2),3:(0,0),4:(1,0.2),5:(1,0),6:(1.5,-0.2),7:(2,0.2),8:(2.5,0),9:(4,0),10:(5,0)}
A=[(0,1,{'peso':20}),(1,2,{'peso':6}),(2,3,{'peso':2}),(3,4,{'peso':8}),(3,5,{'peso':10}),(3,6,{'peso':12}),(4,7,{'peso':1}),(5,8,{'peso':12}),(8,6,{'peso':3}),(7,9,{'peso':7}),(9,10,{'peso':4}),(1,3,{'peso':9}),(8,9,{'peso':9})]
G.add_edges_from(A)
pesos=nx.get_edge_attributes(G,'peso')

Tiempos=[]
for i in range(30):
    T1=0
    for j in range(300000):
        t1=time.time()
        R = [p for p in nx.all_shortest_paths(G, source=0, target=10,weight='peso')]
        t2=time.time()
        T=t2-t1
        T1=T1+T
    Tiempos.append(T1)  
    print('Tiempo total de repeticiones: ',T1) 

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)
        
Arcos=[(R[0][i],R[0][i+1]) for i in range(len(R[0])-1)]

nx.draw_networkx_nodes(G,V,nodelist=[0,1,2,3,4,5,6,7,8,9,10],node_color='m', node_size=300)
nx.draw_networkx_edges(G,V,width=1.2,edgelist=[(1,3),(3,6),(3,5),(5,8),(8,9),(6,8)],alpha=1,arrowsize=20)
nx.draw_networkx_labels(G,V)
nx.draw_networkx_edge_labels(G, V,edge_labels=pesos,font_color='b')
nx.draw_networkx_edges(G,V,edgelist=Arcos,edge_color='c',width=3)
plt.axis('off')
plt.savefig("A2G3.eps")
plt.show(3)

f = open ('Reporte2.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()
'''
GRAFO 5
'''

G=nx.DiGraph()  

A=[(0,1,{'peso':12}),(1,2,{'peso':5}),(2,3,{'peso':7}),(3,4,{'peso':6}),(4,0,{'peso':8}),(0,5,{'peso':12}),(5,6,{'peso':5}),(6,7,{'peso':4}),(7,8,{'peso':10}),(8,0,{'peso':8}),(0,6,{'peso':25}),(0,2,{'peso':2}),(5,8,{'peso':30})]
G.add_edges_from(A)
pesos=nx.get_edge_attributes(G,'peso')
pos=nx.spring_layout(G, iterations=100)

Tiempos=[]
for i in range(30):
    T1=0
    for j in range(300000):
        t1=time.time()
        R = [p for p in nx.all_shortest_paths(G, source=0, target=8,weight='peso')]
        t2=time.time()
        T=t2-t1
        T1=T1+T
    Tiempos.append(T1)  
    print('Tiempo total de repeticiones: ',T1) 

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)
        
Arcos=[(R[0][i],R[0][i+1]) for i in range(len(R[0])-1)]

labels={0:'D'}
nx.draw_networkx_nodes(G,pos,nodelist=[0],node_shape='s',node_color='b', node_size=300)
nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4],node_color='pink')
nx.draw_networkx_nodes(G,pos,nodelist=[5,6,7,8],node_color='g')
nx.draw_networkx_edges(G,pos,width=2,edgelist=[(0,1),(1,2),(2,3),(3,4),(4,0),(8,0),(0,6),(0,2),(5,8)],alpha=1,arrowsize=25)
nx.draw_networkx_labels(G,pos,labels,front_size=12,font_color='w')
nx.draw_networkx_labels(G, pos,font_color='w')
nx.draw_networkx_edge_labels(G, pos,edge_labels=pesos,font_color='r',font_size=8)
nx.draw_networkx_edges(G,pos,edgelist=Arcos,edge_color='c',width=3,arrowsize=25)
plt.axis('off')
plt.savefig("A2G4.eps")
plt.show(4)

f = open ('Reporte2.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()

'''
GRAFO 8
'''

G=nx.Graph()

A=[(1,2,{'peso':5}),(3,4,{'peso':8}),(1,3,{'peso':1}),(3,2,{'peso':12}),(2,4,{'peso':38}),(4,1,{'peso':9})]
G.add_edges_from(A)
pesos=nx.get_edge_attributes(G,'peso')
pos = nx.bipartite_layout(G,{1,4}, scale=0.2)

Tiempos=[]
for i in range(30):
    T1=0
    for j in range(300000):
        t1=time.time()
        R = [p for p in nx.all_shortest_paths(G, source=2, target=4,weight='peso')]
        t2=time.time()
        T=t2-t1
        T1=T1+T
    Tiempos.append(T1)  
    print('Tiempo total de repeticiones: ',T1) 

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)
        
Arcos=[(R[0][i],R[0][i+1]) for i in range(len(R[0])-1)]

labels={1:'México', 3: 'Nayarit', 4: 'Cancún' }
labels1={2:'Monterrey'}
nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4],node_color='b',node_shape='p')
nx.draw_networkx_edges(G,pos,width=1,edgelist=A,alpha=1)
nx.draw_networkx_edges(G,pos,width=3,edgelist=[(3,2)],alpha=1,edge_color='r',size=0.1)
nx.draw_networkx_edge_labels(G, pos,edge_labels=pesos,font_color='r',font_size=8, label_pos=0.56)
nx.draw_networkx_edges(G,pos,edgelist=Arcos,edge_color='c',width=3)

pos1=pos
for i in pos:
    pos1[i][1]=pos1[i][1]+0.04
nx.draw_networkx_labels(G,pos,labels, font_size=12)
for i in pos:
    pos1[i][1]=pos1[i][1]-0.08
nx.draw_networkx_labels(G,pos,labels1, font_size=12)
plt.axis('off')
plt.savefig("A2G5.eps")
plt.show(5)

f = open ('Reporte2.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()