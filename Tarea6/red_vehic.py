import matplotlib.pyplot as plt
import networkx as nx

#-------------------------------------
#Cardinalidades
numpersonas = 1000
numvehiculos =80
numcalles = 20

#Capacidades
personasxvehiculo=3
vehiculosxcalle=4
#-------------------------------------

#Definicion de conjuntos
conjpersonas = [i for i in range(numpersonas)] # 0,1,2,...,numpersonas-1
conjvehiculos = [i+len(conjpersonas) for i in range(numvehiculos)] # numpersonas,numpersonas+1,...,numpersonas+numvehiculos-1
conjcalles = [i+len(conjpersonas)+len(conjvehiculos) for i in range(numcalles)]


#REPRESENTACION
R1=[[i,j] for i in conjpersonas for j in conjvehiculos]
R2=[[j,k] for j in conjvehiculos for k in conjcalles]

Rn = nx.Graph()
Rn.add_edges_from(R1)
posn = nx.bipartite_layout(Rn,conjpersonas)

Rx = nx.Graph()
Rx.add_edges_from(R2)
posx = nx.bipartite_layout(Rx,conjvehiculos)

#plt.subplot(1,2,1)
nx.draw(Rn,posn)
plt.axis('off')
#plt.savefig("Red_1.eps")
plt.show()

#plt.subplot(1,2,2)
nx.draw(Rx,posx)
plt.axis('off')
#plt.savefig("Red_2.eps")
plt.show()

#RED DEL MODELO DE SOLUCION AL PROBLEMA
aux1 = numpersonas + numvehiculos + numcalles
aux2 = numpersonas + numvehiculos + numcalles + 1
aux3 = numpersonas + numvehiculos + numcalles + 2
aux4 = numpersonas + numvehiculos + numcalles + 3
aux5 = numpersonas + numvehiculos + numcalles + 4
aux6 = numpersonas + numvehiculos + numcalles + 5

U1=[[aux1,i] for i in conjpersonas]
U2=[[i,aux2] for i in conjpersonas]
U3=[[aux2,j] for j in conjvehiculos]
U4=[[j,aux3] for j in conjvehiculos]

U5=[[aux4,i] for i in conjvehiculos]
U6=[[i,aux5] for i in conjvehiculos]
U7=[[aux5,j] for j in conjcalles]
U8=[[j,aux6] for j in conjcalles]



Red1 = U1 + U2
Red2 = U2 + U3
Red3 = U3 + U4
Red4 = U4 + U5

Red5 = U5 + U6
Red6 = U6 + U7
Red7 = U7 + U8

plt.figure(figsize=(10,6))
plt.subplots_adjust(wspace = 0.0)

plt.subplot(1,4,1)
G1=nx.Graph()
G1.add_edges_from(U1)
pos1=nx.bipartite_layout(G1,{aux1})
nx.draw(G1,pos1,with_labels=True)
plt.axis('off')

plt.subplot(1,4,2)
G2=nx.Graph()
G2.add_edges_from(U2)
pos2=nx.bipartite_layout(G2,conjpersonas)
nx.draw_networkx_nodes(G2,pos2,node_size=0)
nx.draw_networkx_edges(G2,pos2)
plt.axis('off')

plt.subplot(1,4,3)
G3=nx.Graph()
G3.add_edges_from(U3)
pos3=nx.bipartite_layout(G3,{aux2})
nx.draw_networkx_nodes(G3,pos3)
nx.draw_networkx_edges(G3,pos3)
nx.draw_networkx_labels(G3,pos3)
plt.axis('off')

plt.subplot(1,4,4)
G4=nx.Graph()
G4.add_edges_from(U4)
pos4=nx.bipartite_layout(G4,conjvehiculos)
Nodos = [i for i in G4.nodes()]
numero = [0 if n!= aux3 else 250 for n in Nodos]
etiqueta=[14 if n==aux3 else 0 for n in Nodos]
nx.draw_networkx_nodes(G4,pos4,node_size=numero)
nx.draw_networkx_edges(G4,pos4)
nx.draw_networkx_labels(G4,pos4,labels={aux3:aux3})
plt.axis('off')
#plt.savefig("Red_sol1.eps")
plt.show()
#---------------------------
plt.figure(figsize=(10,6))
plt.subplots_adjust(wspace = 0.0)

plt.subplot(1,4,1)
G5=nx.Graph()
G5.add_edges_from(U5)
pos5=nx.bipartite_layout(G5,{aux4})
nx.draw(G5,pos5,with_labels=True)
plt.axis('off')

plt.subplot(1,4,2)
G6=nx.Graph()
G6.add_edges_from(U6)
pos6=nx.bipartite_layout(G6,conjvehiculos)
nx.draw_networkx_nodes(G6,pos6,node_size=0)
nx.draw_networkx_edges(G6,pos6)
plt.axis('off')

plt.subplot(1,4,3)
G7=nx.Graph()
G7.add_edges_from(U7)
pos7=nx.bipartite_layout(G7,{aux5})
nx.draw_networkx_nodes(G7,pos7)
nx.draw_networkx_edges(G7,pos7)
nx.draw_networkx_labels(G7,pos7)
plt.axis('off')

plt.subplot(1,4,4)
G8=nx.Graph()
G8.add_edges_from(U8)
pos8=nx.bipartite_layout(G8,conjcalles)
Nodos = [i for i in G8.nodes()]
numero = [0 if n!= aux6 else 250 for n in Nodos]
etiqueta=[14 if n==aux6 else 0 for n in Nodos]
nx.draw_networkx_nodes(G8,pos8,node_size=numero)
nx.draw_networkx_edges(G8,pos8)
nx.draw_networkx_labels(G8,pos8,labels={aux6:aux6})
plt.axis('off')
#plt.savefig("Red_sol2.eps")
plt.show()

A1 = [ (u,v,{'cap':1})  if u>v else (v,u,{'cap':1}) for (u,v) in G1.edges] #Con menor porque el S es el siguiente
A2 = [ (u,v,{'cap':1})  if u<v else (v,u,{'cap':1}) for (u,v) in G2.edges] #Con mayor porque 
A3 = [ (u,v,{'cap':personasxvehiculo})  if u<v else (v,u,{'cap':personasxvehiculo}) for (u,v) in G3.edges]
A4 = [ (u,v,{'cap':personasxvehiculo})  if u<v else (v,u,{'cap':personasxvehiculo}) for (u,v) in G4.edges] #Con mayor porque 

A5 = [ (u,v,{'cap':1})  if u>v else (v,u,{'cap':1}) for (u,v) in G5.edges] #Con menor porque el S es el siguiente
A6 = [ (u,v,{'cap':1})  if u<v else (v,u,{'cap':1}) for (u,v) in G6.edges] #Con mayor porque 
A7 = [ (u,v,{'cap':vehiculosxcalle})  if u<v else (v,u,{'cap':vehiculosxcalle}) for (u,v) in G7.edges]
A8 = [ (u,v,{'cap':vehiculosxcalle})  if u<v else (v,u,{'cap':vehiculosxcalle}) for (u,v) in G8.edges] #Con mayor porque 

Gfinal1 = nx.Graph()
Gfinal1.add_edges_from(A1+A2+A3+A4)

Gfinal2 = nx.Graph()
Gfinal2.add_edges_from(A5+A6+A7+A8)

valor1,flujo_arcos1 = nx.maximum_flow(Gfinal1,aux1,aux3,'cap')
valor2,flujo_arcos2 = nx.maximum_flow(Gfinal2,aux4,aux6,'cap')
print(valor1)
#print('',flujo_arcos1,'')
print(valor2)
#print('',flujo_arcos2,'')

'''

#A = [i for i in zip(conjpersonas,conjvehiculos)]
#print(A)

#plt.figure(figsize=(10,6))

plt.figure(figsize=(10,6))
#sharey=True

plt.subplot(2,3,1)
G1 = nx.Graph()
G1.add_edges_from(U1)
pos1 = nx.bipartite_layout(G1,{aux1})
nx.draw_networkx_nodes(G1,pos1,node_size=10)
nx.draw_networkx_edges(G1,pos1)
plt.axis('off')

plt.subplot(2,3,2)
G2 = nx.Graph()
G2.add_edges_from(U2)
pos2 = nx.bipartite_layout(G2,conjpersonas)
nx.draw_networkx_nodes(G2,pos2,node_size=10)
nx.draw_networkx_edges(G2,pos2)
plt.axis('off')

plt.subplot(2,3,3)
G3 = nx.Graph()
G3.add_edges_from(U3)
pos3 = nx.bipartite_layout(G3,conjvehiculos)
nx.draw_networkx_nodes(G3,pos3,node_size=10)
nx.draw_networkx_edges(G3,pos3)
plt.axis('off')

plt.subplot(2,3,4)
G4 = nx.Graph()
G4.add_edges_from(U4)
pos4 = nx.bipartite_layout(G4,{aux2})
nx.draw_networkx_nodes(G4,pos4,node_size=10)
nx.draw_networkx_edges(G4,pos4)
plt.axis('off')

plt.subplot(2,3,5)
G5 = nx.Graph()
G5.add_edges_from(U5)
pos5 = nx.bipartite_layout(G5,conjvehiculos)
nx.draw_networkx_nodes(G5,pos5,node_size=10)
nx.draw_networkx_edges(G5,pos5)
plt.axis('off')

plt.subplot(2,3,6)
G6 = nx.Graph()
G6.add_edges_from(U6)
pos6 = nx.bipartite_layout(G6,conjcalles)
nx.draw_networkx_nodes(G6,pos6,node_size=10)
nx.draw_networkx_edges(G6,pos6)
plt.axis('off')

plt.show()

A1 = [ (u,v,{'cap':1})  if u>v else (v,u,{'cap':1}) for (u,v) in G1.edges] #Con menor porque el S es el siguiente
A2 = [ (u,v,{'cap':1})  if u<v else (v,u,{'cap':1}) for (u,v) in G2.edges] #Con mayor porque 
A3 = [ (u,v,{'cap':personasxvehiculo})  if u<v else (v,u,{'cap':personasxvehiculo}) for (u,v) in G3.edges]
A4 = [ (u,v,{'cap':1})  if u>v else (v,u,{'cap':1}) for (u,v) in G4.edges]
A5 = [ (u,v,{'cap':1})  if u<v else (v,u,{'cap':1}) for (u,v) in G5.edges]
A6 = [ (u,v,{'cap':vehiculosxcalle})  if u<v else (v,u,{'cap':vehiculosxcalle}) for (u,v) in G6.edges]

Gfinal1 = nx.Graph()
Gfinal1.add_edges_from(A1+A2+A3)

Gfinal2 = nx.Graph()
Gfinal2.add_edges_from(A4+A5+A6)

valor1,flujo_arcos1 = nx.maximum_flow(Gfinal1,aux1,aux2,'cap')
valor2,flujo_arcos2 = nx.maximum_flow(Gfinal2,aux2,aux3,'cap')
print(valor1,valor2)
print('',flujo_arcos1,'',flujo_arcos2)


'''