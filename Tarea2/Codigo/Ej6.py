# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 09:35:33 2019

@author: yanet
"""

import networkx as nx 
import matplotlib.pyplot as plt

G=nx.DiGraph() 
A=[(0,1),(0,2),(0,3),(0,4),(3,4)]
labels={0:'P',1:'T1',2:'T2',3:'T3',4:'T4'}
G.add_edges_from(A)
pos=nx.random_layout(G)

nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4],node_color='c',node_size=500)
nx.draw_networkx_nodes(G,pos,nodelist=[0],node_color='g', node_size=1000,node_shape='s')
nx.draw_networkx_edges(G,pos,width=1,edgelist=A,alpha=1,arrowsize=20)
nx.draw_networkx_labels(G,pos,labels, front_size=12,font_color='w')

plt.axis('off')
plt.savefig("GDR.eps")