import math
import time
import matplotlib.pyplot as plt
from pruebas import util
from pruebas import ChiCuadrado
from pruebas import Corridas
from pruebas import Series
from pruebas import Poker


def distribucion_exponencial(datos,alpha):
    ais = []
    for dato in datos:
        if(dato == 1):
            dato = 1-0.001
        ais.append(-1*math.log(1-dato)/alpha)
    return ais


def distribucion_bernoulli(datos, p, n):
    ais = []
    acum = 0
    for index,dato in enumerate(datos):
        if(dato < p):
            acum += 1
        if(index % n == 0):
            ais.append(acum)
            acum = 0
    return ais


#punto 1.1
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


#punto 1.2.a
def punto1_2_a():
    datos = generador(122,100000)
    numerosAleatorios = util.normalizar(datos)
    #x va de -3 hasta 3
    F=[0.00135, 0.00187, 0.00256, 0.00347, 0.00466, 0.00621, 0.00820, 0.01072, 0.0139,
       0.01786, 0.02275, 0.02872, 0.03593, 0.04457, 0.05480, 0.06681, 0.08076, 0.0968, 
       0.11507, 0.13567, 0.15866, 0.18406, 0.21186, 0.24196, 0.27425, 0.30854, 0.34458, 
       0.38209, 0.42074, 0.46017, 0.5,     0.53983, 0.57926, 0.61791, 0.65542, 0.69146,
       0.72575, 0.75804, 0.78814, 0.81594, 0.84134, 0.86433, 0.88493, 0.90320, 0.91924,
       0.93319, 0.94520, 0.95543, 0.96407, 0.97128, 0.97725, 0.98214, 0.98610, 0.98928,
       0.99180, 0.99379, 0.99534, 0.99653, 0.99744, 0.99813, 0.99865
       ]
    numerosDistNormal=[]
    for r in numerosAleatorios:
        for fxk1 in range(len(F)):
            if(r<=F[fxk1]):
                for fxk in range(F.index(F[fxk1]),-1,-1):
                    if(r>=F[fxk]):
                       
                        xk=-3+0.1*fxk
                        xk1=-3+0.1*fxk1
                        lamb=(F[fxk1]-r)/(F[fxk1]-F[fxk])
                        a=lamb*(xk) + (1-lamb)*(xk1)
                        numerosDistNormal.append(a)
                        print(xk,F[fxk], '-',xk1,F[fxk1], r)
                        break
                break
    print(len(numerosDistNormal))
    intervalos= util.crearClases(util.numeroClases(100000))
    fo= util.frecuenciasObservadas(intervalos,numerosDistNormal)
    print(fo)
    plt.plot(list(map(lambda a: a[1], intervalos)),fo)
    plt.ylabel('frecuencia observada')
    plt.show()


#punto1.2.b
def punto1_2_b():
    datos = generador(30,100)
    datos = util.normalizar(datos)
    datos_exponencial = distribucion_exponencial(datos, 2.1)

    intervalos = util.crearClases(util.numeroClases(100))
    fo = util.frecuenciasObservadas(intervalos, datos_exponencial)


    plt.plot(list(map( lambda a: a[1], intervalos)),fo)
    plt.ylabel('frecuencia observada')
    plt.show()


#punto1.2.c
def punto1_2_c():
    numerosAleatorios=util.normalizar(generador(cantidad=1000))
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


# d ) Binomial (n = 100, p = 0.3)
def punto1_2_d():
    datos = generador(30,1000000)
    datos = util.normalizar(datos)
    datos_bernoulli =  distribucion_bernoulli(datos, 0.3, 100)

    intervalos = util.crearClases(util.numeroClases(len(datos_bernoulli)))
    fo = util.frecuenciasObservadas(intervalos, util.normalizar(datos_bernoulli))

    plt.plot(list(map( lambda a: a[1], intervalos)),fo)
    plt.ylabel('frecuencia observada')
    plt.show()


def punto2():
    datos=util.normalizar(generador(cantidad=100))
    Series.seriesTabla(datos,0.1,2)
    Corridas.mostrarCorridasCrecimiento(datos,0.1)
    Corridas.mostrarCorridas(datos,0.1)
    ChiCuadrado.chiCuadradoTabla(datos,0.1)
    Poker.poker3Tabla(util.normalizar(datos), 0.1)



punto1_2_d()