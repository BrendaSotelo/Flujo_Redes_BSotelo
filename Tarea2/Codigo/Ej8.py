# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 14:45:39 2019

@author: yanet
"""


import networkx as nx 
import matplotlib.pyplot as plt

G=nx.MultiGraph()
A=[(1,2),(2,3),(3,4),(3,1),(3,2),(2,4),(1,3)]
G.add_edges_from(A)
labels={1:'México', 3: 'Nayarit', 4: 'Cancún' }
labels1={2:'Monterrey'}
pos = nx.bipartite_layout(G,{1,4}, scale=0.2)

nx.draw_networkx_nodes(G,pos,nodelist=[1,2,3,4],node_color='b',node_shape='p')
nx.draw_networkx_edges(G,pos,width=1,edgelist=A,alpha=1)
nx.draw_networkx_edges(G,pos,width=3,edgelist=[(2,3)],alpha=1,edge_color='r',size=0.1)
pos1=pos
for i in pos:
    pos1[i][1]=pos1[i][1]+0.04
nx.draw_networkx_labels(G,pos,labels, font_size=12)
for i in pos:
    pos1[i][1]=pos1[i][1]-0.08
nx.draw_networkx_labels(G,pos,labels1, font_size=12)
plt.axis('off')
plt.savefig("MNC.eps")
