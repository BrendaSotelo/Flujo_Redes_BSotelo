# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:33:05 2019

@author: yanet
"""

import networkx as nx 
import matplotlib.pyplot as plt

G=nx.DiGraph() 
A=[(0,1),(1,2),(2,3),(3,4),(4,0),(0,5),(5,6),(6,7),(7,8),(8,0)]
G.add_edges_from(A)
labels={0:'D'}
pos=nx.spring_layout(G, iterations=100)
nx.draw_networkx_nodes(G,pos,nodelist=[0],node_shape='s',node_color='b', node_size=300)
nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4],node_color='pink')
nx.draw_networkx_nodes(G,pos,nodelist=[5,6,7,8],node_color='c')
nx.draw_networkx_edges(G,pos,width=2,edgelist=A,alpha=1,arrowsize=25)
nx.draw_networkx_labels(G,pos,labels,front_size=12,font_color='w')

plt.axis('off')
plt.savefig("GDC.eps")