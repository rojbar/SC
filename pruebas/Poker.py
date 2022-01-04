from . import ChiCuadrado
from tabulate import tabulate

def obtenerDecimales(datos):
    decimales = []
    for dato in datos:
        decimales.append(f'{int(dato * (1000))/(1000):.3f}'[2:])
    return decimales

def obtenerClasesK3():
    return [ 
        "3 IGUALES",
        "2 IGUALES 1 DIFERENTE",
        "3 DIFERENTES"
    ]

def obtenerFrecuenciasEsperadas(total_datos):
    return [0.01 * total_datos, 0.24*total_datos, 0.72*total_datos]

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
    clases = obtenerClasesK3()
    chiCuadrados = list(map(lambda fe, fo: ChiCuadrado.calcularChiCuadrado(fe, fo), frecuencias_esperadas,frecuencias_observadas))
    xCalc =ChiCuadrado.calcularChiCuadrados(chiCuadrados)
    xCrit = 0

    pasa = True
    if(xCalc > xCrit):
        pasa = False
    res = []
    for fila in zip(clases,frecuencias_observadas, frecuencias_esperadas, chiCuadrados):
         res.append(fila)
    return  [res, xCalc, xCrit, pasa]

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


datos = [
    0.3163,	0.4438,	0.5747,	0.1908,	0.2829,	0.6034,	0.2011,	0.6643,	0.9016,	0.2913,
    0.1319,	0.6235,	0.6208,	0.9173,	0.2296,	0.6305,	0.7348,	0.3657,	0.425,	0.52,
    0.7299,	0.3847,	0.685,	0.9083,	0.1024,	0.7366,	0.2248,	0.7218,	0.2277,	0.6495,
    0.9208,	0.7804,	0.592,	0.7126,	0.8892,	0.7757,	0.7795,	0.6775,	0.3438,	0.2234,
    0.2948,	0.6049,	0.7617,	0.5667,	0.0706,	0.4907,	0.0686,	0.4993,	0.7706,	0.591,
    0.7113,	0.5349,	0.8835,	0.0349,	0.3063,	0.237,	0.0985,	0.7607,	0.5853,	0.9042,
    0.0049,	0.962,	0.4767,	0.9255,	0.5806,	0.1856,	0.0508,	0.4864,	0.7624,	0.2841,
    0.8394,	0.3062,	0.1635,	0.6599,	0.4443,	0.0346,	0.026,	0.2889,	0.6681,	0.764,
    0.9723,	0.9096,	0.4579,	0.8236,	0.3435,	0.9882,	0.0777,	0.6874,	0.3303,	0.5752
]

print(len(datos))
#print(obtenerDecimales(datos))
poker3Tabla(datos, 0.05)
