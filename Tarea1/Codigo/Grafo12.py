# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 00:20:21 2019

@author: yanet
"""

import networkx as nx 
import matplotlib.pyplot as plt

G=nx.MultiDiGraph()

V={0:(0,0),1:(1,1),2:(1,-1),3:(-1.5,-1.5),4:(0,-3)}
A=[(0,1),(0,2),(0,3),(0,4)]
labels={0:'Hospital'}

nx.draw_networkx_nodes(G,V,nodelist=[1,2,3,4],node_color='pink')
nx.draw_networkx_nodes(G,V,nodelist=[0],node_color='r')
nx.draw_networkx_edges(G,V,width=1,edgelist=A,alpha=1)
nx.draw_networkx_edges(G,V,width=3,edgelist=[(0,3)],alpha=1, edge_color='c')
nx.draw_networkx_labels(G,V,labels, front_size=12)

plt.axis('off')
plt.savefig("MDR.eps")