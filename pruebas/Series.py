import math
from . import ChiCuadrado
import itertools
from tabulate import tabulate


#agrupa los datos en vectores de n dimensiones
def agruparDatos(datos,dimensiones):
    return [datos[x:x+dimensiones] for x in range(0, len(datos), dimensiones)]


def pruebaSeries(datos, confianza, dimensiones):
    total_datos = len(datos)
    total_grupos = total_datos/dimensiones
    total_clases = math.ceil(math.sqrt(total_grupos))

    clases_por_dimension = math.ceil(math.pow( math.sqrt(total_grupos),1/dimensiones))
    total_clases_por_dimension =  math.pow(clases_por_dimension,dimensiones)
    datos_agrupados = agruparDatos(datos,dimensiones)
    frecuencias_observadas = frecuenciasObservadas(datos_agrupados,dimensiones,clases_por_dimension) 

    frecuencia_esperada = total_grupos/total_clases_por_dimension
    chiCuadrados = list(map(lambda fo: ChiCuadrado.calcularChiCuadrado(frecuencia_esperada,fo),frecuencias_observadas.values()))
    xcalc = sum(chiCuadrados)
    # xcrit = 22.307
    # xcrit=12.02 #xcrit para grado 7
    xcrit=13.36 #xcrit para grado 8
    return [xcalc,xcrit,frecuencias_observadas,frecuencia_esperada,chiCuadrados]

    
#retorna los posibles combinaciones de clases que puede tener un vector para cada uno de sus numeros
def posiblesCombinaciones(dimensiones,clasesPorDimension):
    clases = list(itertools.product([i for i in range(1,clasesPorDimension+1)],repeat=dimensiones))

    cuenta={}
    for clase in clases:
            cadena=''
            for numero in clase:
                cadena+=str(numero)+'-'

            cuenta[cadena[:-1]]=0
    
    return cuenta


def frecuenciasObservadas(datos,dimensiones,clasesPorDimension):
    intervalos=[i*1/clasesPorDimension for i in range(0,clasesPorDimension+1)]

    combinaciones=[]
    for dato in datos:
        clase=''
        for numero in dato:
            for index,intervalo in enumerate(intervalos):
                if(numero<=intervalo):
                    clase+=f'{str(index)}-'
                    break
        clase=clase[:-1]
        combinaciones.append(clase)
    
    combinaciones.pop()
    posibles_combinaciones = posiblesCombinaciones(dimensiones,clasesPorDimension)

    for combinacion in combinaciones:
        posibles_combinaciones[combinacion]+=1
    
    return posibles_combinaciones


def seriesTabla(datos, confianza,dimensiones):
    res = pruebaSeries(datos,confianza,dimensiones)
    print('entro')
    print(f"X^2 = {res[0]}")
    print(f"X^2crit = {res[1]}")

    if(res[0] <= res[1]):
        print("El generador es bueno en cuanto a independencia pues el valor calculado es menor o igual al critico")
    else:
        print("El generador no es bueno en cuanto a independencia pues el valor calculado es mayor al critico")
  
    cabecera = ["clase", "FO", "FE", "(FE-FO)^2/FE"]
    values= [(clase,res[2][clase],res[3],res[4][index]) for index,clase in enumerate(res[2].keys())]
    print(tabulate(values, cabecera, tablefmt="grid"))
  