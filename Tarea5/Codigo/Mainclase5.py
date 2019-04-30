from Clase5 import grafo,caracteristicas
import warnings
import matplotlib.pyplot as plt
warnings.simplefilter("ignore")

def main():

    #-------------------Intancia 1----------------------------------  
    g1=grafo(3,3,1)
    g1.crear()
    g1.graficar()
    g1.Asignarpesos(10,3)
    g1.solucion()
    g1.CrearTabla()  
    g1.variacion_d(30,70)
    g1.variacion_f(30,70)
    #print(g1.best_d)
    #print(g1.best_f)
    g1.solucion2()
   
    #-------------------Intancia 2----------------------------------    
    g2=grafo(3,3,2)
    g2.crear()
    g2.graficar()
    g2.Asignarpesos(10,3)
    g2.solucion()
    g2.CrearTabla()  
    g2.variacion_d(30,70)
    g2.variacion_f(30,70)
    #print(g1.best_d)
    #print(g1.best_f)
    g2.solucion2()
    
    #-------------------Intancia 3----------------------------------    
    g3=grafo(4,4,3)
    g3.crear()
    g3.graficar()
    g3.Asignarpesos(10,3)
    g3.solucion()
    g3.CrearTabla()  
    g3.variacion_d(30,70)
    g3.variacion_f(30,70)
    #print(g1.best_d)
    #print(g1.best_f)
    g3.solucion2()
    
    #-------------------Intancia 4----------------------------------
    g4=grafo(4,4,4)
    g4.crear()
    g4.graficar()
    g4.Asignarpesos(10,3)
    g4.solucion()
    g4.CrearTabla()  
    g4.variacion_d(30,70)
    g4.variacion_f(30,70)
    #print(g1.best_d)
    #print(g1.best_f)
    g4.solucion2()
    
    #-------------------Intancia 5-----------------------------------
    g5=grafo(4,4,5) 
    g5.crear()
    g5.graficar()
    g5.Asignarpesos(10,3)
    g5.solucion()
    g5.CrearTabla()  
    g5.variacion_d(30,70)
    g5.variacion_f(30,70)
    #print(g1.best_d)
    #print(g1.best_f)
    g5.solucion2()
    
    caracteristicas([g1,g2,g3,g4,g5])  # recibe objetos tipo grafo
    
main()