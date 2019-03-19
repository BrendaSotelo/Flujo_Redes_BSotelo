# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:31:26 2019

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

G.add_edges_from([(1,2),(2,3),(2,4),(3,4),(4,5)])
pos =nx.spectral_layout(G)

Tiempos=[]
for i in range(30):
    T1=0
    for j in range(200000):
        t1=time.time()
        Tm = nx.dfs_tree(G, source=1)
        t2=time.time()
        T=t2-t1
        T1=T1+T
    Tiempos.append(T1) 
    print('Tiempo total de repeticiones: ',T1)

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)

nx.draw_networkx_nodes(G,pos,nodelist=G.nodes,node_color='r', node_size=400)
nx.draw_networkx_edges(G,pos,nodelist=G.edges)
nx.draw_networkx_labels(G,pos,font_color='w')
nx.draw_networkx_edges(G,pos, edgelist=Tm.edges,edge_color='b',width=2)

plt.axis('off')
plt.savefig("A5G1.eps")
plt.show(1)

f = open ('Reporte5.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()
'''
GRAFO 2
'''
G=nx.Graph() 

G.add_edges_from([(1,2),(2,3),(3,4),(4,5),(5,6),(1,6),(2,5),(1,7),(7,8)])
pos= nx.fruchterman_reingold_layout(G, iterations=1000)

Tiempos=[]
for i in range(30):
    T1=0
    for j in range(200000):
        t1=time.time()
        Tm = nx.dfs_tree(G, source=8)
        t2=time.time()
        T=t2-t1
        T1=T1+T
    Tiempos.append(T1) 
    print('Tiempo total de repeticiones: ',T1)

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)

nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4,5,6,7,8],node_color='yellow', node_size=300)
nx.draw_networkx_edges(G,pos,nodelist=G.edges)
nx.draw_networkx_labels(G,pos,font_color='black')

nx.draw_networkx_edges(G,pos, edgelist=Tm.edges,edge_color='b',width=2)

plt.axis('off')
plt.savefig("A5G2.eps")
plt.show(2)

f = open ('Reporte5.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()
'''
GRAFO 4
'''
G=nx.Graph() 
 
V={0:(-2,0.2),1:(-1,0.2),2:(0,0.2),3:(0,0),4:(1,0.2),5:(1,0),6:(1.5,-0.2),7:(2,0.2),8:(2.5,0),9:(4,0),10:(5,0)}
G.add_edges_from([(0,1),(1,2),(2,3),(3,4),(3,5),(3,6),(4,7),(5,8),(8,6),(7,9),(9,10),(1,3),(8,9)])

Tiempos=[]
for i in range(30):
    T1=0
    for j in range(200000):
        t1=time.time()
        Tm = nx.dfs_tree(G, source=0)
        t2=time.time()
        T=t2-t1
        T1=T1+T
    Tiempos.append(T1) 
    print('Tiempo total de repeticiones: ',T1)

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)

nx.draw_networkx_nodes(G,V,nodelist=G.nodes,node_color='m', node_size=500)
nx.draw_networkx_edges(G,V,nodelist=G.edges,width=1.2,alpha=1,arrowsize=20)
nx.draw_networkx_labels(G,V,font_color='w')

nx.draw_networkx_edges(G,V, edgelist=Tm.edges,edge_color='b',width=2)

plt.axis('off')
plt.savefig("A5G3.eps")
plt.show(3)

f = open ('Reporte5.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()
'''
GRAFO 5
'''
G=nx.DiGraph()  

G.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,0,),(0,5),(5,6),(6,7),(7,8),(8,0),(0,6),(0,2),(5,8)])
pos=nx.spring_layout(G, iterations=100)

Tiempos=[]
for i in range(30):
    T1=0
    for j in range(200000):
        t1=time.time()
        Tm = nx.dfs_tree(G, source=0)
        t2=time.time()
        T=t2-t1
        T1=T1+T
    Tiempos.append(T1) 
    print('Tiempo total de repeticiones: ',T1)

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)

nx.draw_networkx_nodes(G,pos,node_shape='s',node_color='b', node_size=300)
nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4],node_color='r')
nx.draw_networkx_nodes(G,pos,nodelist=[5,6,7,8],node_color='g')
nx.draw_networkx_edges(G,pos,nodelist=G.edges,arrowsize=25)
nx.draw_networkx_labels(G,pos,font_color='black')

nx.draw_networkx_edges(G,pos, edgelist=Tm.edges,edge_color='b',width=2,arrowsize=25)

plt.axis('off')
plt.savefig("A5G4.eps")
plt.show(4)

f = open ('Reporte5.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()

'''
GRAFO 8
'''

G=nx.Graph()

G.add_edges_from([(1,2),(3,4),(1,3),(3,2),(2,4),(4,1)])
pos = nx.bipartite_layout(G,{1,4}, scale=0.2)

Tiempos=[]
for i in range(30):
    T1=0
    for j in range(200000):
        t1=time.time()
        Tm = nx.dfs_tree(G, source=1)
        t2=time.time()
        T=t2-t1
        T1=T1+T
    Tiempos.append(T1) 
    print('Tiempo total de repeticiones: ',T1)

media=np.round(np.mean(Tiempos),4)
desviacion=np.round(np.std(Tiempos),4)

labels={1:'México', 3: 'Nayarit', 4: 'Cancún' }
labels1={2:'Monterrey'}
nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4],node_color='c',node_shape='p')
nx.draw_networkx_edges(G,pos,width=2,edgelist=[(3,2),(2,4),(4,1)],alpha=1)

nx.draw_networkx_edges(G,pos, edgelist=Tm.edges,edge_color='b',width=3,arrowsize=25)

pos1=pos
for i in pos:
    pos1[i][1]=pos1[i][1]+0.04
nx.draw_networkx_labels(G,pos,labels, font_size=12)
for i in pos:
    pos1[i][1]=pos1[i][1]-0.08
nx.draw_networkx_labels(G,pos,labels1, font_size=12)
plt.axis('off')
plt.savefig("A5G5.eps")
plt.show(5)

f = open ('Reporte5.txt','a')
f.write(str(media) + "\t" + str(desviacion) + "\n" )   
f.close()
