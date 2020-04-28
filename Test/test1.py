import numpy as np
import matplotlib.pyplot as plt
from random import *

porcencross = 0.75                     #constantes
porcenmut = 0.05

def f(x):                              #declaracion funcion objetivo
    return (x/((2**30)-1))**2

def sujetoaentero(x):                  #pasar arreglo de bin a entero
    numInt = 0
    for i,val in enumerate(x):
        if val == 1:
            numInt = 2**(len(x)-1-i) + numInt
    return numInt 

def sumatoriadesujetos(y):             #sumatoria de todos los sujetos pasados a binario
    cont = 0
    for i in y:
        cont += f(sujetoaentero(i)) 
    return cont
    
def fitness(x,y):                       #funcion fitness
    return f(x)/sumatoriadesujetos(y)
     
def selec(listFitness):                 #funcion seleccion con ruleta
    ruleta = []
    ran = random()
    cont=0
    for i in range(10):
        cont+=listFitness[i]
        ruleta.append(cont)
    elegido = 0
    maxim = 1
    for j in range(10):
        if ran <= ruleta[j] and ruleta[j] <= maxim:
            elegido = j
            maxim = ruleta[j] 
    return elegido #devuelve indice del sujeto seleccionado por la ruleta

def cross(padresEleg):                      #funcion crossover
    hijos = []                     
    corterandom = randint(0,29)
    hijos.append(padresEleg[0][:corterandom] + padresEleg[1][corterandom:])
    hijos.append(padresEleg[1][:corterandom]+ padresEleg[0][corterandom:])
    return hijos #devuelve dos hijos

def mut(sujeto):                             #funcion mutacion
    genamutar = randint(0,29)
    if sujeto[genamutar] == 0:
        sujeto[genamutar] = 1
    else:
        sujeto[genamutar] = 0
    return sujeto #devuelve sujeto mutado

def promedio(suj):               #promedio de sujetos de un ciclo
    return sum(suj)/len(suj)

def cicl(sujetos,ciclos):                      
    if ciclos >= 0:

        padres = []                            #inicializacion listas
        listFitness = [] 
        hijos = [] 
        hijosEnt = []                        
        
        for i in range(10):                     #asignar fitness
            listFitness.append(fitness(sujetoaentero(sujetos[i]),sujetos))
            
        for i in range(10):                     #seleccionar los padres
            padres.append(sujetos[selec(listFitness)])  
        
        j=1    
        for i in range(0,10,2):                     #aplicar crossover
            if  random() <= porcencross:                       
                hijos.extend(cross([padres[i],padres[j]]))
            else:
                hijos.extend([padres[i],padres[j]])
            j+=2 
    
        if random() <= porcenmut:               #aplicar mutacion
            genran = randint(0,9) 
            sujetos[genran] = mut(sujetos[genran])
        
        for i in hijos:                         #agregar hijos para todos y enteros
            hijosEnt.append(sujetoaentero(i))
            todos.append(sujetoaentero(i))
        
        plotMax.append(max(hijosEnt))
        plotMin.append(min(hijosEnt))
        plotProm.append(promedio(hijosEnt))
        
        ciclos -= 1
        cicl(hijos,ciclos)
    else:
        #mostrar datos    
        print(max(todos))
        plt.style.use('ggplot')
        plt.plot(list(range(len(plotMax))),plotMax,label="Maximos")  
        plt.plot(list(range(len(plotMin))),plotMin,label="Minimos")
        plt.plot(list(range(len(plotProm))),plotProm,label="Promedios")
        plt.legend()
        plt.show()

sujetos = []                                   #carga poblacion inicial          
for q in range(10):
    sujeto = []
    for j in range(30):
        sujeto.append(randint(0,1))
    sujetos.append(sujeto)

    todos = []      
    plotMax = []
    plotMin = []
    plotProm = [] 

    for i in sujetos:                        #carga poblacion inicial en todos
        todos.append(sujetoaentero(i))  
cicl(sujetos,ciclos)                         #recursion para que los sujetos sean los hijos en la siguiente iteracion


    

        




    
    
    
    
