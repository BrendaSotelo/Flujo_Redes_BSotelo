# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 02:51:59 2019

@author: yanet
"""


import networkx as nx 
import matplotlib.pyplot as plt

G=nx.MultiDiGraph()

V={0:(0,0),1:(1,0),2:(2,0.2),3:(3,0),4:(4,0)}
A=[(0,1),(1,2),(2,3),(3,4)]

nx.draw_networkx_nodes(G,V,nodelist=[0,1,2,3,4],node_color='b')
nx.draw_networkx_edges(G,V,width=1,edgelist=A,alpha=1)
nx.draw_networkx_edges(G,V,width=3,edgelist=[(0,1),(2,3)],alpha=1,edge_color='c')

plt.axis('off')
plt.savefig("MDA.eps")