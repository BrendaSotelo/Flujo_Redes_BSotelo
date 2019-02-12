# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 02:35:46 2019

@author: yanet
"""

import networkx as nx 
import matplotlib.pyplot as plt

G=nx.MultiDiGraph()

V={0:(0,0),1:(1,0),2:(1.5,-1),3:(2,1),4:(-1,0),5:(-2,-1),6:(0,-1)}
A=[(0,6),(6,5),(5,4),(4,0),(1,0),(3,1),(2,1)]

nx.draw_networkx_nodes(G,V,nodelist=[0,1,2,3,4,5,6],node_color='b')
nx.draw_networkx_edges(G,V,width=1,edgelist=A,alpha=1)
nx.draw_networkx_edges(G,V,width=3,edgelist=[(1,0)],alpha=1)

plt.axis('off')
plt.savefig("MDC.eps")