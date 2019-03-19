import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

Datos = np.genfromtxt('Reporte1.txt')
Medias=[Datos[i][0] for i in range(0,5)]
Alg=['Grafo 1','Grafo 2','Grafo 3','Grafo 4','Grafo 5']
h=np.arange(len(Alg))

plt.bar(h,Medias,color='green', align='center', width=0.9)

plt.xticks(h,Alg)
plt.xlabel('Tipo de grafo',size=14)
plt.ylabel('Tiempo (segundos)',size=14)
#plt.title('Algoritmo flujo máximo',size=18, color='green')
plt.savefig('Histograma1.eps', format='eps', dpi=1000)
'''
-----------------------------------------------------------------------------
'''
Datos = np.genfromtxt('Reporte2.txt')
Medias=[Datos[i][0] for i in range(0,5)]
Alg=['Grafo 1','Grafo 2','Grafo 3','Grafo 4','Grafo 5']
h=np.arange(len(Alg))

plt.bar(h,Medias,color='orange', align='center', width=0.9)

plt.xticks(h,Alg)
plt.xlabel('Tipo de grafo',size=14)
plt.ylabel('Tiempo (segundos)',size=14)
plt.savefig('Histograma2.eps', format='eps', dpi=1000)

'''
-----------------------------------------------------------------------------
'''
Datos = np.genfromtxt('Reporte3.txt')
Medias=[Datos[i][0] for i in range(0,5)]
Alg=['Grafo 1','Grafo 2','Grafo 3','Grafo 4','Grafo 5']
h=np.arange(len(Alg))

plt.bar(h,Medias,color='c', align='center', width=0.9)

plt.xticks(h,Alg)
plt.xlabel('Tipo de grafo',size=14)
plt.ylabel('Tiempo (segundos)',size=14)
plt.savefig('Histograma3.eps', format='eps', dpi=1000)

'''
-----------------------------------------------------------------------------
'''
Datos = np.genfromtxt('Reporte4.txt')
Medias=[Datos[i][0] for i in range(0,5)]
Alg=['Grafo 1','Grafo 2','Grafo 3','Grafo 4','Grafo 5']
h=np.arange(len(Alg))

plt.bar(h,Medias,color='m', align='center', width=0.9)

plt.xticks(h,Alg)
plt.xlabel('Tipo de grafo',size=14)
plt.ylabel('Tiempo (segundos)',size=14)
plt.savefig('Histograma4.eps', format='eps', dpi=1000)

'''
-----------------------------------------------------------------------------
'''
Datos = np.genfromtxt('Reporte5.txt')
Medias=[Datos[i][0] for i in range(0,5)]
Alg=['Grafo 1','Grafo 2','Grafo 3','Grafo 4','Grafo 5']
h=np.arange(len(Alg))

plt.bar(h,Medias,color='y', align='center', width=0.9)

plt.xticks(h,Alg)
plt.xlabel('Tipo de grafo',size=14)
plt.ylabel('Tiempo (segundos)',size=14)
plt.savefig('Histograma5.eps', format='eps', dpi=1000)
