# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 10:45:49 2019

@author: yanet
"""

import networkx as nx 
import matplotlib.pyplot as plt

G=nx.Graph()  

A=[(0,1),(1,2),(2,3),(3,4),(4,5),(0,5),(1,4),(0,6),(6,7)]

G.add_edges_from(A)
labels={2:'1',3:'2',4:'3',5:'4',0:'5',1:'6',6:'7',7:'8'}
pos= nx.fruchterman_reingold_layout(G, iterations=1000)

nx.draw_networkx_nodes(G,pos,nodelist=[0,1,2,3,4,5,6,7],node_color='b', node_size=300)
nx.draw_networkx_edges(G,pos,width=1,edgelist=A,alpha=1)
nx.draw_networkx_labels(G,pos,labels, front_size=12, font_color='w')

plt.axis('off')
plt.savefig("GNC.eps")

