# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 07:22:24 2019

@author: yanet
"""

import networkx as nx 
import matplotlib.pyplot as plt

G=nx.MultiGraph()
G.add_nodes_from([0,1,2,3,4,5,6])

pos = nx.nx_pydot.pydot_layout(G)

A=[(0,1),(1,2),(0,3),(2,4),(3,5),(2,6)]

nx.draw_networkx_nodes(G,pos,nodelist=[0,1,2,3,4,5,6],node_color='b')
nx.draw_networkx_edges(G,pos,width=1,edgelist=A,alpha=1,edge_color='c')
nx.draw_networkx_edges(G,pos,width=3,edgelist=[(0,3)],alpha=1,edge_color='r')
nx.draw_networkx_labels(G,pos,front_size=12)

plt.axis('off')
plt.savefig("MNA.eps")
plt.show()