# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 08:45:40 2019

@author: yanet
"""

import networkx as nx
from fa2 import ForceAtlas2
import matplotlib.pyplot as plt

G = nx.MultiDiGraph() 
G.add_nodes_from(range(6))
labels={1:'I', 2:'S1',3:'S2',4:'S3',5:'S4'}
forceatlas2 = ForceAtlas2(
                        outboundAttractionDistribution=True,  
                        linLogMode=False,
                        adjustSizes=False,
                        edgeWeightInfluence=1.0,
                        
                        jitterTolerance=1.0,
                        barnesHutOptimize=True,
                        barnesHutTheta=1.2,
                        multiThreaded=False,

                        scalingRatio=2.0,
                        strongGravityMode=False,
                        gravity=1.0,

                        verbose=True)

pos = forceatlas2.forceatlas2_networkx_layout(G, pos=None, iterations=100)




nx.draw_networkx_nodes(G, pos, nodelist=[2,3,4,5],node_size=400, with_labels=True, node_color="m")
nx.draw_networkx_nodes(G, pos, nodelist=[1],node_size=400, with_labels=True, node_color="g")
nx.draw_networkx_edges(G, pos,edgelist=[(1,5)],edge_color="r")
nx.draw_networkx_edges(G, pos,edgelist=[(1,2),(1,3),(1,4)], edge_color="k")
nx.draw_networkx_labels(G,pos,labels, front_size=12, font_color='w')

plt.axis('off')
plt.savefig('MNR.eps')