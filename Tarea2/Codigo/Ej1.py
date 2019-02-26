# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 18:43:49 2019

@author: yanet
"""

import networkx as nx 
import matplotlib.pyplot as plt

G=nx.Graph()  

A=[(1,2),(2,3),(3,4),(4,5),(2,6),(2,7),(3,8),(3,9),(4,10),(4,11)]
G.add_edges_from(A)

pos = nx.kamada_kawai_layout(G)

nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4,5,6,7,8,9,10,11],node_color='gray', node_size=500)
nx.draw_networkx_edges(G,pos,width=3,edgelist=A, )

plt.axis('off')
plt.savefig("GNA.eps")

