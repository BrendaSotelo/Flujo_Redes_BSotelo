# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 18:29:28 2019

@author: yanet
"""
 
import networkx as nx 
import matplotlib.pyplot as plt

G=nx.Graph()  
V={0:(0,0),1:(0.4,0),2:(0,1),3:(0.4,1),4:(0,2),5:(0.4,2),6:(0.2,5.0),7:(0.2,-3.0),8:(0.2,0),9:(0.2,1),
   10:(0.2,2)}
A=[(0,1),(2,3),(4,5),(6,7),(8,9)]

nx.draw_networkx_nodes(G,V,nodelist=[0,1,2,3,4,5,6,7,8,9,10],node_color='black')
nx.draw_networkx_edges(G,V,width=1,edgelist=A)

plt.axis('off')
plt.savefig("GNA.eps")
