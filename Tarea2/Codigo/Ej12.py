# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 07:27:30 2019

@author: yanet
"""

import networkx as nx
import matplotlib.pyplot as plt

G=nx.DiGraph()
G.add_nodes_from(range(5))

V = nx.nx_pydot.graphviz_layout(G)

labels={0:'Hospital'}

nx.draw_networkx_nodes(G,V,nodelist=[1,2,3,4],node_color='pink')
nx.draw_networkx_nodes(G,V,nodelist=[0],node_color='r')
nx.draw_networkx_edges(G,V,width=1,edgelist=[(0,1),(0,2),(0,3),(0,4)],alpha=1)
nx.draw_networkx_edges(G,V,width=3,edgelist=[(0,3)],alpha=1, edge_color='c')
nx.draw_networkx_labels(G,V,labels, front_size=12)

plt.axis('off')
plt.savefig("MDR.eps")