import pruebas.KolmogorovSmirov as KolmogorovSmirov
import util

#implemente un generador lineal congruente con a = 100, m= 165123, c = 1234 y x0 = 32 y genere 10000 números. Trabaje con una confianza del 5 %
def generador():
    a = 100
    m = 165123
    c = 1234
    x0 = 32
    numeros=[]
    for i in range(10000):
        x0 = (a*x0 + c)%m
        numeros.append(x0)
   # print(len(numeros),numeros)
    return numeros

#a
def puntoa():
    datos = generador()
    maximo = util.max(datos)
    KolmogorovSmirov.kolmogorovTabla( list(map(lambda x: x/maximo, datos )) , 0.05)
