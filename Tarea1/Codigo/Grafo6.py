# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:28:27 2019

@author: yanet
"""

import networkx as nx 
import matplotlib.pyplot as plt

G=nx.DiGraph() 
 
V={0:(0,0),1:(1,5),2:(5,3),3:(7,0),4:(7,-3)}
A=[(0,1),(0,2),(0,3),(0,4),(3,4)]
labels={0:'P',1:'T1',2:'T2',3:'T3',4:'T4'}

nx.draw_networkx_nodes(G,V,nodelist=[1,2,3,4],node_color='c')
nx.draw_networkx_nodes(G,V,nodelist=[0],node_color='g')
nx.draw_networkx_edges(G,V,width=1,edgelist=A,alpha=1)
nx.draw_networkx_labels(G,V,labels, front_size=12)

plt.axis('off')
plt.savefig("GDR.eps")