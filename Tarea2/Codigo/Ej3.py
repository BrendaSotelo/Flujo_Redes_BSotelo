# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 20:57:14 2019

@author: yanet
"""

import networkx as nx 
import matplotlib.pyplot as plt

G=nx.Graph()  
A=[(0,1),(1,2),(2,3),(3,4)]
G.add_edges_from(A)
labels={1:'R'}
pos=nx.shell_layout(G)

nx.draw_networkx_nodes(G,pos,nodelist=[1],node_shape='s', node_color='g',node_size=500)
nx.draw_networkx_nodes(G,pos,nodelist=[3,4],node_color='b', node_size=80)
nx.draw_networkx_nodes(G,pos,nodelist=[0,2],node_color='b', node_size=80)
nx.draw_networkx_edges(G,pos,width=3,edgelist=[(2,3),(3,4)],alpha=1,style='dashed')
nx.draw_networkx_edges(G,pos,width=3,edgelist=[(0,1),(1,2)],alpha=1,style='dashed')
nx.draw_networkx_labels(G,pos,labels, front_size=12)
nx.draw_networkx_edge_labels(G, pos,font_family='sans-serif',edge_labels={(0,1):'Barragan',(1,2):'Gonzalitos',(2,3):'Ruiz Cortines',(3,4):'Rangel Frias'})

plt.axis('off')
plt.savefig("GNR.eps")
