# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 01:24:45 2019

@author: yanet
"""

import networkx as nx 
import matplotlib.pyplot as plt

G=nx.MultiDiGraph()

V={0:(0,3),1:(0,0),2:(1,0.5),3:(2,2),4:(-2,2)}
A=[(0,1),(0,2),(0,3),(0,4)]
labels={0:'I', 1:'S1',2:'S2',3:'S3',4:'S4'}

nx.draw_networkx_nodes(G,V,nodelist=[1,2,3,4],node_color='b')
nx.draw_networkx_nodes(G,V,nodelist=[0],node_color='r')
nx.draw_networkx_edges(G,V,width=1,edgelist=A,alpha=1)
nx.draw_networkx_edges(G,V,width=3,edgelist=[(0,3)],alpha=1)
nx.draw_networkx_labels(G,V,labels, front_size=12)

plt.axis('off')
plt.savefig("MNR.eps")