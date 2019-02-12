# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 18:04:34 2019

@author: yanet
"""
import networkx as nx 
import matplotlib.pyplot as plt

G=nx.MultiGraph()
 
V={0:(0,0),1:(1,1.5),2:(2,1.5),3:(0,-3),4:(3,4), 5:(1,-3.5),6:(3,0)}
A=[(0,1),(1,2),(0,3),(2,4),(3,5),(2,6)]

nx.draw_networkx_nodes(G,V,nodelist=[0,1,2,3,4,5,6],node_color='b')
nx.draw_networkx_edges(G,V,width=1,edgelist=A,alpha=1,edge_color='c')
nx.draw_networkx_edges(G,V,width=3,edgelist=[(0,3)],alpha=1,edge_color='r')
nx.draw_networkx_labels(G,V,front_size=12)

plt.axis('off')
plt.savefig("MNA.eps")