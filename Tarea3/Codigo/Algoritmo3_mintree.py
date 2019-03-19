# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:43:57 2019

@author: yanet
"""
import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np
import time

'''
GRAFO  10
'''
G=nx.Graph()

G.add_edge(1, 2, weight=5)
G.add_edge(2, 3, weight=10)
G.add_edge(3, 4, weight=20)
G.add_edge(1, 5, weight=30)
G.add_edge(5, 6, weight=15)
G.add_edge(6, 4, weight=15)
G.add_edge(2, 5, weight=20)
G.add_edge(5, 3, weight=10)
G.add_edge(3, 6, weight=5)

pesos=nx.get_edge_attributes(G,'weight')
pos= nx.circular_layout(G)

Tiempos=[]
for i in range(30):
    T1=0
    for j in range(60000):
        t1=time.time()
        Tm = nx.minimum_spanning_tree(G,algorithm='kruskal')
        t2=time.time()
        T=t2-t1
        T1=T1+T
    Tiempos.append(T1)  
    print('Tiempo total de repeticiones: ',T1)

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)

nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4,5,6],node_color='b', node_size=500)
nx.draw_networkx_edges(G,pos,width=2,edgelist=[(3,4),(1,5),(5,6),(2,5),(5,3)],alpha=1, edge_color='black')
nx.draw_networkx_edges(G,pos,width=3,edgelist=Tm.edges,alpha=1, edge_color='m')
nx.draw_networkx_edge_labels(G, pos,edge_labels=pesos,font_color='r')
nx.draw_networkx_labels(G, pos,font_color='w')

plt.axis('off')
plt.savefig("A3G1.eps")
plt.show(1)

f = open ('Reporte3.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()
'''
GRAFO 2
'''
G=nx.Graph()

G.add_edge(1, 2, weight=3)
G.add_edge(2, 3, weight=6)
G.add_edge(3, 4, weight=4)
G.add_edge(5, 4, weight=7)
G.add_edge(6, 5, weight=9)
G.add_edge(1, 6, weight=5)
G.add_edge(2, 5, weight=1)
G.add_edge(7, 1, weight=10)
G.add_edge(8, 7, weight=15)

pesos=nx.get_edge_attributes(G,'weight')
pos= nx.fruchterman_reingold_layout(G, iterations=1000)

Tiempos=[]
for i in range(30):
    T1=0
    for j in range(60000):
        t1=time.time()
        Tm = nx.minimum_spanning_tree(G,algorithm='kruskal')
        t2=time.time()
        T=t2-t1
        T1=T1+T
    Tiempos.append(T1)
    print('Tiempo total de repeticiones: ',T1)

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)

nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4,5,6,7,8],node_color='yellow', node_size=500)
nx.draw_networkx_edges(G,pos,width=3,edgelist=Tm.edges,alpha=1,edge_color='m')
nx.draw_networkx_edges(G,pos,width=1,edgelist=[(5,4),(6,5)],alpha=1)
nx.draw_networkx_labels(G,pos,font_color='black')
nx.draw_networkx_edge_labels(G, pos,edge_labels=pesos,font_color='r')
plt.axis('off')
plt.savefig("A3G2.eps")
plt.show(2)

f = open ('Reporte3.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()

'''
GRAFO 4
'''
G=nx.Graph()  

V={0:(-2,0.2),1:(-1,0.2),2:(0,0.2),3:(0,0),4:(1,0.2),5:(1,0),6:(1.5,-0.2),7:(2,0.2),8:(2.5,0),9:(4,0),10:(5,0)}

G.add_edge(0, 1, weight=20)
G.add_edge(1, 2, weight=6)
G.add_edge(2, 3, weight=2)
G.add_edge(3, 4, weight=8)
G.add_edge(3, 5, weight=10)
G.add_edge(3, 6, weight=12)
G.add_edge(4, 7, weight=1)
G.add_edge(5, 8, weight=12)
G.add_edge(8, 6, weight=3)
G.add_edge(7, 9, weight=7)
G.add_edge(9, 10, weight=4)
G.add_edge(1, 3, weight=9)
G.add_edge(8, 9, weight=9)
pesos=nx.get_edge_attributes(G,'weight')

Tiempos=[]
for i in range(30):
    T1=0
    for j in range(60000):
        t1=time.time()
        Tm = nx.minimum_spanning_tree(G,algorithm='kruskal')
        t2=time.time()
        T=t2-t1
        T1=T1+T
    Tiempos.append(T1)
    print('Tiempo total de repeticiones: ',T1)

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)

nx.draw_networkx_nodes(G,V,nodelist=[0,1,2,3,4,5,6,7,8,9,10],node_color='pink', node_size=300)
nx.draw_networkx_edges(G,V,width=3,edgelist=Tm.edges,alpha=1,edge_color='m')
nx.draw_networkx_edges(G,V,width=1.2,edgelist=[(3,6),(5,8),(1,3)],alpha=1,arrowsize=20)
nx.draw_networkx_labels(G,V)
nx.draw_networkx_edge_labels(G, V,edge_labels=pesos,font_color='r',label_pos=0.56)

plt.axis('off')
plt.savefig("A3G3.eps")
plt.show(3)

f = open ('Reporte3.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()
'''
GRAFO 5
'''

G=nx.Graph() 
 
G.add_edge(0, 1, weight=12)
G.add_edge(1, 2, weight=5)
G.add_edge(2, 3, weight=7)
G.add_edge(3, 4, weight=6)
G.add_edge(4, 0, weight=8)
G.add_edge(0, 5, weight=12)
G.add_edge(6, 7, weight=4)
G.add_edge(7, 8, weight=10)
G.add_edge(8, 0, weight=8)
G.add_edge(0, 6, weight=25)
G.add_edge(0, 2, weight=2)
G.add_edge(5, 8, weight=30)


pesos=nx.get_edge_attributes(G,'weight')
pos=nx.spring_layout(G, iterations=100)

Tiempos=[]
for i in range(30):
    T1=0
    for j in range(60000):
        t1=time.time()
        Tm = nx.minimum_spanning_tree(G,algorithm='kruskal')
        t2=time.time()
        T=t2-t1
        T1=T1+T
    Tiempos.append(T1)
    print('Tiempo total de repeticiones: ',T1)

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)

labels={0:'D'}
nx.draw_networkx_nodes(G,pos,nodelist=[0],node_shape='s',node_color='b', node_size=300)
nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4],node_color='pink')
nx.draw_networkx_nodes(G,pos,nodelist=[5,6,7,8],node_color='g')
nx.draw_networkx_edges(G,pos,width=3,edgelist=Tm.edges,alpha=1,edge_color='m')
nx.draw_networkx_edges(G,pos,width=2,edgelist=[(0,1),(4,0),(0,6),(5,8)],alpha=1,arrowsize=25)
nx.draw_networkx_labels(G,pos,labels,front_size=12,font_color='w')
nx.draw_networkx_labels(G, pos,font_color='w')
nx.draw_networkx_edge_labels(G, pos,edge_labels=pesos,font_color='r',font_size=8)
plt.axis('off')
plt.savefig("A3G4.eps")
plt.show(4)

f = open ('Reporte3.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()
'''
GRAFO 8
'''
G=nx.Graph()

G.add_edge(1, 2, weight=5)
G.add_edge(3, 4, weight=8)
G.add_edge(1, 3, weight=1)
G.add_edge(3, 2, weight=12)
G.add_edge(2, 4, weight=38)
G.add_edge(4, 1, weight=9)

pesos=nx.get_edge_attributes(G,'weight')
pos = nx.bipartite_layout(G,{1,4}, scale=0.2)

Tiempos=[]
for i in range(30):
    T1=0
    for j in range(60000):
        t1=time.time()
        Tm = nx.minimum_spanning_tree(G,algorithm='kruskal')
        t2=time.time()
        T=t2-t1
        T1=T1+T
    Tiempos.append(T1)
    print('Tiempo total de repeticiones: ',T1)

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)

labels={1:'México', 3: 'Nayarit', 4: 'Cancún' }
labels1={2:'Monterrey'}
nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4],node_color='b',node_shape='p')
nx.draw_networkx_edges(G,pos,width=1,edgelist=[(3,2),(2,4),(4,1)],alpha=1)
nx.draw_networkx_edges(G,pos,width=3,edgelist=Tm.edges,alpha=1,edge_color='m')

nx.draw_networkx_edge_labels(G, pos,edge_labels=pesos,font_color='r',font_size=8, label_pos=0.56)


pos1=pos
for i in pos:
    pos1[i][1]=pos1[i][1]+0.04
nx.draw_networkx_labels(G,pos,labels, font_size=12)
for i in pos:
    pos1[i][1]=pos1[i][1]-0.08
nx.draw_networkx_labels(G,pos,labels1, font_size=12)
plt.axis('off')
plt.savefig("A3G5.eps")
plt.show(5)

f = open ('Reporte3.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()