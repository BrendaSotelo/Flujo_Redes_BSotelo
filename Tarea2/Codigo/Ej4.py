# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:42:30 2019

@author: yanet
"""

import networkx as nx 
import matplotlib.pyplot as plt

G=nx.DiGraph()  

A=[(0,1),(1,2),(2,3),(3,4),(3,5),(3,6),(4,7),(5,8),(8,6),(7,9),(9,10),(6,9),(1,3)]
labels={0:'1',1:'2',2:'3',3:'4',4:'5',5:'6',6:'9',7:'7',8:'8',9:'10',10:'11'}
G.add_edges_from(A)

pos =  nx.circular_layout(G)

nx.draw_networkx_nodes(G,pos,nodelist=[0,1,2,3,4,5,6,7,8,9,10],node_color='m', node_size=450, alpha=0.8)
nx.draw_networkx_edges(G,pos,width=1.2,edgelist=A,alpha=1,arrowsize=20)
nx.draw_networkx_labels(G,pos,labels, front_size=12)

plt.axis('off')
plt.savefig("GDA.eps")