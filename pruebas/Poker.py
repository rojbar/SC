from . import ChiCuadrado
from tabulate import tabulate

#obtiene los 3 decimales de una lista de numeros y los retorna como una lista de cadenas
def obtenerDecimales(datos):
    decimales = []
    for dato in datos:
        decimales.append(f'{int(dato * (1000))/(1000):.3f}'[2:])
    return decimales

def obtenerFrecuenciasEsperadas(total_datos):
    return [0.01 * total_datos, 0.27*total_datos, 0.72*total_datos]

def obtenerFrecuencias(datos):
    iguales = 0
    dos_iguales = 0
    tres_diferentes = 0
    for dato in datos:
        if(dato[0] == dato[1] and dato[1] == dato[2]):
            iguales += 1
        if(dato[0] != dato[1]  and dato[0] != dato[2] and dato[1] != dato[2]):
            tres_diferentes += 1
        if((dato[0] == dato[1] and dato[2] != dato[0]) or (dato[1] == dato[2] and dato[2] != dato[0]) or(dato[2] == dato[0] and dato[1] != dato[2])):
            dos_iguales += 1
    return [iguales, dos_iguales, tres_diferentes]

def pruebaPoker3(datos, confianza):
    datos_decimales = obtenerDecimales(datos)
    frecuencias_observadas = obtenerFrecuencias(datos_decimales)
    frecuencias_esperadas = obtenerFrecuenciasEsperadas(len(datos_decimales))
    clases = [ 
        "3 IGUALES",
        "2 IGUALES 1 DIFERENTE",
        "3 DIFERENTES"
    ]
    chiCuadrados = list(map(lambda fe, fo: ChiCuadrado.calcularChiCuadrado(fe, fo), frecuencias_esperadas,frecuencias_observadas))
    xCalc = sum(chiCuadrados)
    xCrit = {0.05: 5.99, 0.1: 4.605} #valor critico para dos grados de libertad de chicuadrado

    pasa = True
    if(xCalc > xCrit[confianza]):
        pasa = False
    res = []
    for fila in zip(clases,frecuencias_observadas, frecuencias_esperadas, chiCuadrados):
         res.append(fila)
    return  [res, xCalc, xCrit[confianza], pasa]

def poker3Tabla(datos, confianza):
    res = pruebaPoker3(datos, confianza)
    print(f"XCalc = {res[1]}")
    print(f"XCrit = {res[2]}")
    if(res[3]):
        print("El generador es bueno en cuanto a independencia")
    else:
        print("El generador no es bueno en cuaanto a independencia")

    cabecera = ["clase", "FO", "FE", "(FE-FO)^2/FE"]
    print(tabulate(res[0], cabecera, tablefmt="grid"))
