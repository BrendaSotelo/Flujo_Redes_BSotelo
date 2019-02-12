# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 13:43:22 2019

@author: yanet
"""
import networkx as nx 
import matplotlib.pyplot as plt

G=nx.DiGraph() 
 
V={0:(0,0),1:(1,1),2:(3,2),3:(4,1),4:(2,-1),5:(-1,2),6:(-3,1),7:(-4,-1),8:(-2,-2)}
A=[(0,1),(1,2),(2,3),(3,4),(4,0),(0,5),(5,6),(6,7),(7,8),(8,0)]
labels={0:'Centro'}

nx.draw_networkx_nodes(G,V,nodelist=[0,1,2,3,4],node_color='c')
nx.draw_networkx_nodes(G,V,nodelist=[5,6,7,8],node_color='y')
nx.draw_networkx_edges(G,V,width=1,edgelist=A,alpha=1)
nx.draw_networkx_labels(G,V,labels, front_size=12)

plt.axis('off')
plt.savefig("GDC.eps")