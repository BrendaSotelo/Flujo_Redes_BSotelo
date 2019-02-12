# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 00:54:20 2019

@author: yanet
"""

import networkx as nx 
import matplotlib.pyplot as plt

G=nx.Graph()  
V={0:(0,0),1:(0,1),2:(1,0),3:(1,1),4:(0.5,0), 5:(0.5,1),6:(-0.5,1),7:(-0.5,2)}
A=[(0,1),(2,3),(4,5),(0,2),(1,5),(5,3),(1,6),(6,7)]
labels={2:'1',3:'2',4:'3',5:'4',0:'5',1:'6',6:'7',7:'8'}

nx.draw_networkx_nodes(G,V,nodelist=[0,1,2,3,4,5,6,7],node_color='b')
nx.draw_networkx_edges(G,V,width=1,edgelist=A,alpha=1)
nx.draw_networkx_labels(G,V,labels, front_size=12)

plt.axis('off')
plt.savefig("GNC.eps")