# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 12:07:38 2019

@author: yanet
"""

import networkx as nx 
import matplotlib.pyplot as plt

G=nx.DiGraph()  
V={0:(-2,0.2),1:(-1,0.2),2:(0,0.2),3:(0,0),4:(1,0.2),5:(1,0),6:(1.5,-0.2),7:(2,0.2),8:(2.5,0),9:(4,0),10:(5,0)}
A=[(0,1),(1,2),(2,3),(3,4),(3,5),(3,6),(4,7),(5,8),(8,6),(7,9),(9,10),(6,9),(1,3)]
labels={0:'1',1:'2',2:'3',3:'4',4:'5',5:'6',6:'9',7:'7',8:'8',9:'10',10:'11'}

nx.draw_networkx_nodes(G,V,nodelist=[0,1,2,3,4,5,6,7,8,9,10],node_color='b')
nx.draw_networkx_edges(G,V,width=1,edgelist=A,alpha=1)
nx.draw_networkx_labels(G,V,labels, front_size=12)

plt.axis('off')
plt.savefig("GDA.eps")