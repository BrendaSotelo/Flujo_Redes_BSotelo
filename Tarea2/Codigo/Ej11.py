# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:27:51 2019

@author: yanet
"""

import networkx as nx 
import matplotlib.pyplot as plt

G=nx.MultiDiGraph()

A=[(1,2),(2,4),(4,3),(3,1),(5,2),(6,5),(7,5)]
G.add_edges_from(A)

pos =nx.shell_layout(G)

nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4,5,6,7],node_color='y', node_size=400,node_shape='^')
nx.draw_networkx_edges(G,pos,width=1,alpha=1,arrowsize=20)
nx.draw_networkx_edges(G,pos,width=3,edgelist=[(5,2)],alpha=1, edge_color='r', arrowsize=20)

plt.axis('off')
plt.savefig("MDC.eps")