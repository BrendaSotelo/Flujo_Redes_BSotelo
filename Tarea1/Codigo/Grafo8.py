# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 23:28:00 2019

@author: yanet
"""

import networkx as nx 
import matplotlib.pyplot as plt

G=nx.MultiGraph()
 
V={0:(-3,0),1:(1,0),2:(1,3),3:(-1,3)}
A=[(0,1),(0,2),(2,1),(3,1),(3,2)]

nx.draw_networkx_nodes(G,V,nodelist=[0,1,2,3],node_color='b')
nx.draw_networkx_edges(G,V,width=1,edgelist=A,alpha=1)
nx.draw_networkx_edges(G,V,width=3,edgelist=[(2,1)],alpha=1,edge_color='r')
nx.draw_networkx_labels(G,V,front_size=12)

plt.axis('off')
plt.savefig("MNC.eps")