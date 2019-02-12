# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 09:43:16 2019

@author: yanet
"""

import networkx as nx 
import matplotlib.pyplot as plt

G=nx.Graph()  
V={0:(0,0),1:(1,0),2:(0.5,1),3:(0,1),4:(0,2)}
A=[(0,1),(1,2),(2,3),(3,4)]
labels={1:'L'}

nx.draw_networkx_nodes(G,V,nodelist=[1])
nx.draw_networkx_nodes(G,V,nodelist=[0,2,3,4],node_color='b')
nx.draw_networkx_edges(G,V,width=1,edgelist=A,alpha=1)
nx.draw_networkx_labels(G,V,labels, front_size=12)

plt.axis('off')
plt.savefig("GNR.eps")