import time
import matplotlib.pyplot as plt
from pruebas import util
import math
from pruebas import ChiCuadrado
from pruebas import Corridas
from pruebas import Series
def normalizar(numb):
    maxNumb=max(numb)
    values=[]
    for num in numb:
        if(num/maxNumb == 1):
            values.append(num/maxNumb - 0.01)
        else: values.append(num/maxNumb)
    return values

def generador(semilla=0,cantidad=100):
    if(semilla==0):
        semilla=time.time()
    a=7**5
    c=0
    m=2**31-1
    x=semilla
    numb=[]
    for i in range(cantidad):
        x=(a*x+c)%m
        numb.append(x)
    return numb

def punto2a():
    numerosAleatorios=normalizar(generador(cantidad=100))
    #x va de -3.4 hasta 3.4
    F=[0.0003,0.0004,0.0006,0.0009,.00135, 0.00187, 0.00256, 0.00347, 0.00466, 0.00621, 0.0082, 0.01072, 0.0139,
     0.01786, 0.02275, 0.02872, 0.03593, 0.04457, 0.0548, 0.06681, 0.08076, 0.0968, 
     0.11507, 0.13567, 0.15866, 0.18406, 0.21186, 0.24196, 0.27425, 0.30854, 0.34458, 
     0.38209, 0.42074, 0.46017,0.5,0.53983,0.57926,0.61791,0.65542,0.69146,0.72575,
     0.75804,0.78814,0.81594,0.86433, 0.98214, 0.88493, 0.9861, 0.9032, 0.98928, 0.91924, 
     0.9918, 0.93319, 0.99379, 0.9452, 0.99534, 0.95543, 0.99653, 0.96407, 0.99744, 0.97128, 
     0.99813,0.9987,0.9990,0.9993,0.9995,0.9997]
    numerosDistNormal=[]
    for r in numerosAleatorios:
        for fxk1 in range(len(F)):
            if(r<=F[fxk1]):
                for fxk in range(F.index(F[fxk1]),-1,-1):
                    if(r>=F[fxk]):
                       
                        xk=-3.4+0.1*fxk
                        xk1=-3.4+0.1*fxk1
                        lamb=(F[fxk1]-r)/(F[fxk1]-F[fxk])
                        a=lamb*(xk) + (1-lamb)*(xk1)
                        numerosDistNormal.append(a)
                        print(F[fxk],xk,F[fxk1],xk1)
                        break
                break
    print(len(numerosDistNormal))
    intervalos= util.crearClases(util.numeroClases(100))
    print(intervalos)
    fo= util.frecuenciasObservadas(intervalos,numerosDistNormal)
    print(fo)
    plt.plot(list(map(lambda a: a[1], intervalos)),fo)
    plt.ylabel('frecuencia observada')
    plt.show()
   
def punto2c():
    numerosAleatorios=normalizar(generador(cantidad=1000))
    lamb=3.5
    numerosPoisson=[]
    for numero in numerosAleatorios:
        p=math.e**(-lamb)
        F=p
        i=0
        while(numero>F):
            p=(lamb*p)/(i+1)
            F=F+p
            i+=1
        X=i
        numerosPoisson.append(i)
    intervalos= util.crearClases(util.numeroClases(1000))
    print(intervalos)
    fo= util.frecuenciasObservadas(intervalos,util.normalizar(numerosPoisson))
    plt.plot(list(map(lambda a: a[1], intervalos)),fo)
    plt.ylabel('frecuencia observada')
    plt.show()
    return numerosPoisson

#punto2c()

def punto3():
    datos=normalizar(generador(cantidad=100))
    Series.seriesTabla(datos,0.1,2)
    # Corridas.mostrarCorridasCrecimiento(datos,0.1)
    # Corridas.mostrarCorridas(datos,0.1)
    # ChiCuadrado.chiCuadradoTabla(datos,0.05)

punto3()
#Pruebas 
# ChiCuadrado.chiCuadradoTabla(util.normalizar(punto2c()),0.05)
# Corridas.mostrarCorridas(util.normalizar(punto2c()),0.05)


