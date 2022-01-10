from . import util
import math
from tabulate import tabulate

def calcularChiCuadrado(frecuencia_esperada, frecuencia_observada):
    return math.pow((frecuencia_esperada - frecuencia_observada),2)/frecuencia_esperada

def pruebaChiCuadrado(datos, confianza):
    numero_datos = len(datos)
    numero_clases = util.numeroClases(numero_datos)
    clases = util.crearClases(int(numero_clases))
    grados_libertad = numero_clases - 1

    frecuencias_esperadas = util.frecuenciasEsperadas(numero_datos, numero_clases)
    frecuencias_observadas = util.frecuenciasObservadas(clases, datos)

    chiCuadrados = list(map(lambda fe,fo: calcularChiCuadrado(fe,fo),frecuencias_esperadas,frecuencias_observadas))
    chiCuadrado = sum(chiCuadrados)

    #http://www.mat.uda.cl/hsalinas/cursos/2010/eyp2/Tabla%20Chi-Cuadrado.pdf
    estadistico = {0.05: 44.985} #para 31 grados de libertad

    pasa = chiCuadrado <= estadistico[confianza]

    res = []
    for fila in zip(clases,frecuencias_observadas, frecuencias_esperadas, chiCuadrados ):
         res.append(fila)
    return  [res, chiCuadrado, estadistico[confianza], pasa]

def chiCuadradoTabla(datos, confianza):
    res = pruebaChiCuadrado(datos, confianza)
    print(f"X^2 = {res[1]}")
    print(f"X^2crit = {res[2]}")

    if(res[3]):
        print("El generador es bueno en cuanto a uniformidad pues dmcalc es menor o igual a dmcritico")
    else:
        print("El generador no es bueno en cuanto a uniformidad dmcalc  no es menor o igual a dmcritico")

    cabecera = ["clase", "FO", "FE", "(FE-FO)^2/FE"]
    print(tabulate(res[0], cabecera, tablefmt="grid"))

