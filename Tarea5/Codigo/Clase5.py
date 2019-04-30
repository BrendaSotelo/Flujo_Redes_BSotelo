import networkx as nx 
import matplotlib.pyplot as plt
import random
import time
import seaborn as sns
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols

class grafo:
   
    def __init__(self,x1,x2,x3):
        self.dim_x=x1
        self.dim_y=x2
        self.num=x3

    def crear(self):
        self.G= nx.grid_graph(dim=[self.dim_x,self.dim_y])
        self.pos=nx.kamada_kawai_layout(self.G)

    def graficar(self):
        nx.draw_networkx(self.G,self.pos)
        plt.axis('off')
        plot_margin = 0.05
        x0, x1, y0, y1 = plt.axis()
        plt.axis((x0 - plot_margin,x1 + plot_margin,y0 - plot_margin,y1 + plot_margin))
        plt.tight_layout()
        imagen1="I1_"+str(self.num)+".eps"
        plt.savefig(imagen1)
        plt.show()
     
    def Asignarpesos(self, media, desviacion):
        self.media=media
        self.desviacion=desviacion
        K=[i for i in self.G.edges()]
        Pesos=[round (max(0.1,random.gauss(self.media,self.desviacion)),2) for i in range(len(K))]
        e=[]
        for i in range(len(self.G.edges())):
            a=(K[i][0],K[i][1],Pesos[i])  
            e.append(a)
        self.G.add_weighted_edges_from(e)

    def solucion(self):
        #Seleccionar nodo fuente y nodo destino 
        buscar=True
        while buscar:
           
           origen1=random.randint(0, self.dim_x-1)
           origen2=random.randint(0, self.dim_y-1)
           destino1=random.randint(0, self.dim_x-1)
           destino2=random.randint(0, self.dim_y-1)
           
           if origen1==destino1 and origen2==destino2:
              buscar=True
           else:
              buscar=False
        
        self.inicio=(origen1,origen2)
        self.final=(destino1,destino2)
        
        flow_value, flow_dict = nx.maximum_flow(self.G,self.inicio,self.final,capacity='weight')
        self.objetivo=flow_value
        print(self.objetivo)
        #Aqui indica el flujo que pasa por cada arista
        flujo=[]
        pesos=nx.get_edge_attributes(self.G,'weight')
        pesos1=[pesos[i] for i in pesos]
        
        for i in flow_dict.keys():
            for j in flow_dict[i].keys():
                if flow_dict[i][j]>0:
                    flujo.append(flow_dict[i][j]) 
        
        self.grosor_capacidad=[i*0.75 for i in pesos1]
        self.grosor_flujo=[i*0.4 for i in flujo]
        
        nx.draw_networkx_nodes(self.G,self.pos,node_color='purple')
        nx.draw_networkx_nodes(self.G,self.pos,nodelist=[(origen1,origen2)],node_color='b', node_shape='s',node_size=500)
        nx.draw_networkx_nodes(self.G,self.pos,nodelist=[(destino1,destino2)],node_color='r', node_shape='s',node_size=500)
        nx.draw_networkx_edges(self.G,self.pos,edge_color='lightgray',width=self.grosor_capacidad)
        plt.axis('off')
        plot_margin = 0.05
        x0, x1, y0, y1 = plt.axis()
        plt.axis((x0 - plot_margin,x1 + plot_margin,y0 - plot_margin,y1 + plot_margin))
        plt.tight_layout()
        imagen2="I2_"+str(self.num)+".eps"
        plt.savefig(imagen2)
        plt.show()
        
        nx.draw_networkx_nodes(self.G,self.pos,node_color='purple')
        nx.draw_networkx_nodes(self.G,self.pos,nodelist=[(origen1,origen2)],node_color='b', node_shape='s',node_size=500)
        nx.draw_networkx_nodes(self.G,self.pos,nodelist=[(destino1,destino2)],node_color='r', node_shape='s',node_size=500)
        nx.draw_networkx_edges(self.G,self.pos,edge_color='lightgray',width=self.grosor_capacidad)
        nx.draw_networkx_edges(self.G,self.pos,edge_color='dodgerblue',width=self.grosor_flujo, style='--')
        
        plt.axis('off')
        plot_margin = 0.05
        x0, x1, y0, y1 = plt.axis()
        plt.axis((x0 - plot_margin,x1 + plot_margin,y0 - plot_margin,y1 + plot_margin))
        plt.tight_layout()
        imagen3="I3_"+str(self.num)+".eps"
        plt.savefig(imagen3)
        plt.show()
        
    
    def CrearTabla(self):
        A1 = nx.degree_centrality(self.G) 
        A2 = nx.closeness_centrality(self.G)
        A3 = nx.clustering(self.G)
        A4 = nx.load_centrality(self.G)
        A5 = nx.eccentricity(self.G)
        A6 = nx.pagerank(self.G)
        
        '''
        print('{}\t{:>8}{:>8}{:>8}{:>8}\n'.format('N','A1','A2','A3','A4'))
        for i in self.G.nodes():
            print('{}\t{:>8.3f}{:>8.3f}{:>10.6f}{:>8.3f}\n'.format(i,A1[i],A2[i],A3[i],A4[i]))
        '''
   
        sum1=0
        sum2=0
        #sum3=0
        sum4=0
        sum5=0
        sum6=0
        
        for i in self.G.nodes():
            sum1=sum1+A1[i]
            sum2=sum2+A2[i]
            #sum3=sum3+A3[i]
            sum4=sum4+A4[i]
            sum5=sum5+A5[i]
            sum6=sum6+A6[i]
            
        A1=[A1[i]/sum1 for i in self.G.nodes()]
        A2=[A2[i]/sum2 for i in self.G.nodes()]
        #A3=[A3[i]/sum3 for i in self.G.nodes()]
        A4=[A4[i]/sum4 for i in self.G.nodes()]
        A5=[A5[i]/sum5 for i in self.G.nodes()]
        A6=[A6[i]/sum6 for i in self.G.nodes()]
        
        self.A7=[]
        #print('{}\t{:>8}{:>8}{:>8}\n'.format('N','A1','A2','A4'))
        for i in range(len(self.G.nodes())):
            #print( '{}\t{:>8.3f}{:>8.3f}{:>8.3f}\n'.format(i,A1[i],A2[i],A4[i])    )
            self.A7.append(2000*A1[i]+A2[i]+A4[i]+A5[i]+A6[i])
            
    def variacion_d(self,repeticiones,replicas): #Varia el final
        #aux=self.
        self.tabla_d=[]
        self.best_d=[]
        for fila in range(self.dim_x):
            for columna in range(self.dim_y):
                if (fila,columna)!=self.inicio:
                    final=(fila,columna)
                    for i in range(repeticiones):
                        t_inicial=time.time()
                        for i in range(replicas):
                            flow_value, flow_dict = nx.maximum_flow(self.G,self.inicio,final,capacity='weight')
                        t_final=time.time()
                        self.tabla_d.append([self.inicio,final,round(t_final-t_inicial,2),round(flow_value,2)])
                        #print('{}  {}  {:10.3f}{:10.3f}'.format(self.inicio,final,t_final-t_inicial,flow_value))
                    if flow_value-self.objetivo>0.05:
                        self.best_d.append(final)
                
        self.tabla_d=pd.DataFrame(self.tabla_d,columns=['I', 'F', 'TE','FO'])               
                    
    def variacion_f(self,repeticiones,replicas): #Varia el destino
        self.tabla_f=[]
        self.best_f=[]
        for fila in range(self.dim_x):
            for columna in range(self.dim_y):
                if (fila,columna)!=self.final :
                    inicio=(fila,columna)
                    for i in range(repeticiones):
                        t_inicial=time.time()
                        for i in range(replicas):
                            flow_value, flow_dict = nx.maximum_flow(self.G,inicio,self.final,capacity='weight')
                        t_final=time.time()
                        self.tabla_f.append([inicio,self.final,round(t_final-t_inicial,2),round(flow_value,2)])

                        #print('-----------')
                        #print('{}  {}  {:10.3f}{:10.3f}'.format(inicio,self.final,t_final-t_inicial,flow_value))
                    if flow_value-self.objetivo>0.05:
                        self.best_f.append(inicio)
                
        self.tabla_f=pd.DataFrame(self.tabla_f,columns=['I', 'F', 'TE','FO'])
         
         
    def solucion2(self):
        
        nodos1=[]
        nodos2=[]
        nodos3=[]
        nodos4=[]
      
        color1=[]
        color2=[]
        color3=[]
        color4=[]
      
        tamaño1=[]
        tamaño2=[]
        tamaño3=[]
        tamaño4=[]
        
        I=0
        F=0
        
      #st fd
        j=0
        for i in self.G.nodes():
           if i!=self.inicio and i!=self.final:
              if i in self.best_f and i not in self.best_d:
                 nodos1.append(i)
                 color1.append('limegreen')
                 tamaño1.append(self.A7[j])
              if i in self.best_d and i not in self.best_f:
                 nodos2.append(i)
                 color2.append('yellow')
                 tamaño2.append(self.A7[j])
              if i in self.best_d and i in self.best_f:
                 nodos3.append(i)
                 color3.append('darkgreen')
                 tamaño3.append(self.A7[j])
              if i not in self.best_d and i not in self.best_f:
                 nodos4.append(i)
                 color4.append('purple')
                 tamaño4.append(self.A7[j])
           elif i == self.inicio:
              I=j
           elif i == self.inicio:
              F=j
           j=j+1
      
        n1=[]
        c1=[]
        j=0
        for i in self.G.nodes():
           if i != self.inicio and i!=self.final:
              n1.append(i)
              c1.append(self.A7[j])
           j=j+1
           
        nx.draw_networkx_nodes(self.G,self.pos,nodelist=n1,node_color='purple',node_size=c1)
        nx.draw_networkx_nodes(self.G,self.pos,nodelist=[self.inicio],node_color='b', node_shape='s',node_size=self.A7[I])
        nx.draw_networkx_nodes(self.G,self.pos,nodelist=[self.final],node_color='r', node_shape='s',node_size=self.A7[F])
        nx.draw_networkx_edges(self.G,self.pos,edge_color='lightgray',width=self.grosor_capacidad)
        nx.draw_networkx_edges(self.G,self.pos,edge_color='dodgerblue',width=self.grosor_flujo, style='--')
        
          
        plt.axis('off')
        plot_margin = 0.05
        x0, x1, y0, y1 = plt.axis()
        plt.axis((x0 - plot_margin,x1 + plot_margin,y0 - plot_margin,y1 + plot_margin))
        plt.tight_layout()
        imagen4="I4_"+str(self.num)+".eps"
        plt.savefig(imagen4)
        plt.show()
        
        
        #mejores fuente pero no destino      
        nx.draw_networkx_nodes(self.G,self.pos,nodelist=nodos1,node_color=color1,node_size=tamaño1,node_shape='o')
        nx.draw_networkx_nodes(self.G,self.pos,nodelist=nodos1,node_color='b',node_size=[i*.5 for i in tamaño1],node_shape='o')
        #mejores destino pero no fuente
        nx.draw_networkx_nodes(self.G,self.pos,nodelist=nodos2,node_color=color2,node_size=tamaño2,node_shape='o')
        nx.draw_networkx_nodes(self.G,self.pos,nodelist=nodos2,node_color='r',node_size=[i*.5 for i in tamaño2],node_shape='o')
        #mejores fuente y destino
        nx.draw_networkx_nodes(self.G,self.pos,nodelist=nodos3,node_color=color3,node_size=tamaño3,node_shape='o')
        #sin mejora
        nx.draw_networkx_nodes(self.G,self.pos,nodelist=nodos4,node_color=color4,node_size=tamaño4,node_shape='o')
        #inicio
        nx.draw_networkx_nodes(self.G,self.pos,nodelist=[self.inicio],node_color='b', node_shape='s',node_size=self.A7[I])
        #final
        nx.draw_networkx_nodes(self.G,self.pos,nodelist=[self.final],node_color='r', node_shape='s',node_size=self.A7[F])  
        
        nx.draw_networkx_edges(self.G,self.pos,edge_color='lightgray',width=self.grosor_capacidad)
        nx.draw_networkx_edges(self.G,self.pos,edge_color='dodgerblue',width=self.grosor_flujo, style='--')
        
        plt.axis('off')
        plot_margin = 0.05
        x0, x1, y0, y1 = plt.axis()
        plt.axis((x0 - plot_margin,x1 + plot_margin,y0 - plot_margin,y1 + plot_margin))
        plt.tight_layout()
        imagen5="I5_"+str(self.num)+".eps"
        plt.savefig(imagen5)
        plt.show()
        
        '''      
        nx.draw_networkx_nodes(self.G,self.pos,node_size=self.A7, node_color='purple')
        nx.draw_networkx_nodes(self.G,self.pos,nodelist=[self.inicio],node_color='b', node_shape='s',node_size=500)
        nx.draw_networkx_nodes(self.G,self.pos,nodelist=[self.final],node_color='r', node_shape='s',node_size=500)
        #nx.draw_networkx_edge_labels(self.G,self.pos,edge_labels=s_flujo, label_pos=0.7)  
        nx.draw_networkx_edges(self.G,self.pos,edge_color='lightgray',width=self.grosor_capacidad)
        nx.draw_networkx_edges(self.G,self.pos,edge_color='dodgerblue',width=self.grosor_flujo, style='--')
        #nx.draw_networkx_labels(self.G,self.pos,font_color='w')
        nx.draw_networkx_nodes(self.G,self.pos,nodelist=self.best_d,node_color='orange')
        nx.draw_networkx_nodes(self.G,self.pos,nodelist=self.best_f,node_color='yellow')
        '''
        

        '''
        print('aqui esta la tabla D, donde varia el final')
        print(self.tabla_d)
        '''
        
        
        #PARA LA TABLA DONDE VARIA EL NODO DESTINO (F:FINAL)
        if self.dim_x <5: #Si la malla es menor de 5x5 (1x1 , 2x2 , 3x3 y 4x4) => grafica
           
           plot=sns.boxplot(y='TE', x='F', data=self.tabla_d, width=0.4,palette="colorblind")      
           plot=sns.swarmplot(y='TE', x='F',data=self.tabla_d, color='black',alpha=0.0)
           #plot.axes.set_title("Tiempo de ejecución variando\n el vértice sumidero partiendo del vértice "+str(self.inicio),fontsize=13)
           j=0
        
           for c_nodo in self.G.nodes():
               if c_nodo!=self.inicio:
                   aux1 = self.tabla_d.loc[self.tabla_d.F == c_nodo]
                 
                   aux2= np.asarray(aux1['TE'])
                  
                   if max(np.asarray(aux1['FO'])) - self.objetivo >0.01:
                      plt.text(j-0.3,max(aux2)+0.0007 , max(np.asarray(aux1['FO'])),color='r',size=7.2)
                   else:
                      plt.text(j-0.3,max(aux2)+0.0007 , max(np.asarray(aux1['FO'])),color='b',size=7.2)
                   j=j+1
               
           plot.set_xlabel("Vértice sumidero", fontsize=11)
           plot.set_ylabel("Tiempo(segs.)",fontsize=11)
           plot.tick_params(labelsize=8)
           box1="B1_"+str(self.num)+".eps"
           plt.savefig(box1)
           plt.show()
           
        else: # Sino ANOVA
           modelo_int = ols('TE ~  F', data = self.tabla_d).fit() 
           
           ANOVA = sm.stats.anova_lm(modelo_int, typ = 2)
           print(ANOVA)
            
           for i in range(len(ANOVA)):
              print("{:s} {:s}es significativo".format(ANOVA.index[i], "" if ANOVA['PR(>F)'][i] < 0.05 else "NO "))
                
                       
         #PARA LA TABLA DONDE VARIA EL NODO INICIO O FUENTE(I:INICIAL)
        if self.dim_x <5: #Si la malla es menor de 5x5 (1x1 , 2x2 , 3x3 y 4x4) => grafica
           
           plot=sns.boxplot(y='TE', x='I', data=self.tabla_f, width=0.4,palette="colorblind")      
           plot=sns.swarmplot(y='TE', x='I',data=self.tabla_f, color='black',alpha=0.0)
           #plot.axes.set_title("Tiempo de ejecución variando\n el vértice fuente con destino al vértice "+str(self.final),fontsize=13)
           j=0
         
           for c_nodo in self.G.nodes():
               if c_nodo!=self.final:
                   Aux1 = self.tabla_f.loc[self.tabla_f.I == c_nodo]
                 
                   Aux2= np.asarray(Aux1['TE'])
                  
                   if max(np.asarray(Aux1['FO'])) - self.objetivo >0.01:
                      plt.text(j-0.3,max(Aux2)+0.0007 , max(np.asarray(Aux1['FO'])),color='r',size=7.2)
                   else:
                      plt.text(j-0.3,max(Aux2)+0.0007 , max(np.asarray(Aux1['FO'])),color='b',size=7.2)
                   j=j+1
               
           plot.set_xlabel("Vértice fuente", fontsize=11)
           plot.set_ylabel("Tiempo(segs)",fontsize=11)
           plot.tick_params(labelsize=8)
           box2="B2_"+str(self.num)+".eps"
           plt.savefig(box2)
           plt.show()
           
        else: # Sino ANOVA
           modelo_int = ols('TE ~  I', data = self.tabla_f).fit() 
           
           ANOVA = sm.stats.anova_lm(modelo_int, typ = 2)
           print(ANOVA)
            
           for i in range(len(ANOVA)):
              print("{:s} {:s}es significativo".format(ANOVA.index[i], "" if ANOVA['PR(>F)'][i] < 0.05 else "NO "))
      
def caracteristicas(instancias):
    Alg1=[nx.degree_centrality(instancias[0].G),nx.clustering(instancias[0].G),nx.closeness_centrality(instancias[0].G),nx.load_centrality(instancias[0].G),nx.eccentricity(instancias[0].G),nx.pagerank(instancias[0].G)]
    i=1
    Datos1=[]
    for alg in Alg1: 
        valores=[j for j in alg.values()]
        if i==5:
            suma=np.sum(valores)
            valores=[j/suma for j in valores]
            for j in valores:
               Datos1.append([i,j])
        else:
           for j in valores:
              Datos1.append([i,j])
        i=i+1   
    
    Alg2=[nx.degree_centrality(instancias[1].G),nx.clustering(instancias[1].G),nx.closeness_centrality(instancias[1].G),nx.load_centrality(instancias[1].G),nx.eccentricity(instancias[1].G),nx.pagerank(instancias[1].G)]
    i=1
    Datos2=[]
    for alg in Alg2: 
        valores=[j for j in alg.values()]
        if i==5:
            suma=np.sum(valores)
            valores=[j/suma for j in valores]
            for j in valores:
               Datos2.append([i,j])
        else:
           for j in valores:
              Datos2.append([i,j])
        i=i+1 
    
    Alg3=[nx.degree_centrality(instancias[2].G),nx.clustering(instancias[2].G),nx.closeness_centrality(instancias[2].G),nx.load_centrality(instancias[2].G),nx.eccentricity(instancias[2].G),nx.pagerank(instancias[2].G)]
    i=1
    Datos3=[]
    for alg in Alg3:
        valores=[j for j in alg.values()]
        if i==5:
            suma=np.sum(valores)
            valores=[j/suma for j in valores]
            for j in valores:
               Datos3.append([i,j])
        else:
           for j in valores:
              Datos3.append([i,j])
        i=i+1    
    
    Alg4=[nx.degree_centrality(instancias[3].G),nx.clustering(instancias[3].G),nx.closeness_centrality(instancias[3].G),nx.load_centrality(instancias[3].G),nx.eccentricity(instancias[3].G),nx.pagerank(instancias[3].G)]
    i=1
    Datos4=[]
    for alg in Alg4:
        valores=[j for j in alg.values()]
        if i==5:
            suma=np.sum(valores)
            valores=[j/suma for j in valores]
            for j in valores:
               Datos4.append([i,j])
        else:
           for j in valores:
              Datos4.append([i,j])
        i=i+1 
    
    Alg5=[nx.degree_centrality(instancias[4].G),nx.clustering(instancias[4].G),nx.closeness_centrality(instancias[4].G),nx.load_centrality(instancias[4].G),nx.eccentricity(instancias[4].G),nx.pagerank(instancias[4].G)]
    i=1
    Datos5=[]
    for alg in Alg5: 
        valores=[j for j in alg.values()]
        if i==5:
            suma=np.sum(valores)
            valores=[j/suma for j in valores]
            for j in valores:
               Datos5.append([i,j])
        else:
           for j in valores:
              Datos5.append([i,j])
        i=i+1 

    Datos1=pd.DataFrame(Datos1,columns=['A', 'V']) 
    Datos2=pd.DataFrame(Datos2,columns=['A', 'V']) 
    Datos3=pd.DataFrame(Datos3,columns=['A', 'V']) 
    Datos4=pd.DataFrame(Datos4,columns=['A', 'V']) 
    Datos5=pd.DataFrame(Datos5,columns=['A', 'V']) 
    
    bplot=sns.boxplot(y='V', x='A', data=Datos1, width=0.4,palette="colorblind")      
    #bplot.axes.set_title("Comparación por algoritmo de la instancia 1",fontsize=13)
    bplot.set_xlabel("Algoritmo", fontsize=11)
    bplot.set_ylabel("Valor",fontsize=11)
    bplot.tick_params(labelsize=9)
    plt.savefig("Grafo_1.eps")
    plt.show()
         
    bplot=sns.boxplot(y='V', x='A', data=Datos2, width=0.4,palette="colorblind")      
    #bplot.axes.set_title("Comparación por algoritmo del instancia 2",fontsize=13)
    bplot.set_xlabel("Algoritmo", fontsize=11)
    bplot.set_ylabel("Valor",fontsize=11)
    bplot.tick_params(labelsize=9)
    plt.savefig("Grafo_2.eps")
    plt.show()
        
    bplot=sns.boxplot(y='V', x='A', data=Datos3, width=0.4,palette="colorblind")      
    #bplot.axes.set_title("Comparación por algoritmo del instancia 3",fontsize=13)
    bplot.set_xlabel("Algoritmo", fontsize=11)
    bplot.set_ylabel("Valor",fontsize=11)
    bplot.tick_params(labelsize=9)
    plt.savefig("Grafo_3.eps")
    plt.show()
         
    bplot=sns.boxplot(y='V', x='A', data=Datos4, width=0.4,palette="colorblind")      
    #bplot.axes.set_title("Comparación por algoritmo del instancia 4",fontsize=13)
    bplot.set_xlabel("Algoritmo", fontsize=11)
    bplot.set_ylabel("Valor",fontsize=11)
    bplot.tick_params(labelsize=9)
    plt.savefig("Grafo_4.eps")
    plt.show()
     
    bplot=sns.boxplot(y='V', x='A', data=Datos5, width=0.4,palette="colorblind")      
    #bplot.axes.set_title("Comparación por algoritmo del instancia 5",fontsize=13)
    bplot.set_xlabel("Algoritmo", fontsize=11)
    bplot.set_ylabel("Valor",fontsize=11)
    bplot.tick_params(labelsize=9)
    plt.savefig("Grafo_5.eps")
    plt.show()
    







            
            
