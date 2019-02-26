# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:08:59 2019

@author: yanet
"""

import networkx as nx 
import matplotlib.pyplot as plt

G=nx.MultiDiGraph()

A=[(1,2),(2,3),(3,4),(4,5)]
G.add_edges_from(A)

pos =nx.spectral_layout(G)

nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4,5],node_color='b', node_size=300)
nx.draw_networkx_edges(G,pos,width=2,edgelist=A,alpha=1, edge_color='c')
nx.draw_networkx_edges(G,pos,width=3,edgelist=[(1,2),(3,4)],alpha=1,edge_color='r')
nx.draw_networkx_edge_labels(G, pos,edge_labels={(1,2):'Ductos 1 y 2',(2,3):'Ducto 3',(3,4):'Ductos 4 y 5',(4,5):'Ducto 6'})

plt.axis('off')
plt.savefig("MDA.eps")