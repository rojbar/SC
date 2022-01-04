import math
from . import ChiCuadrado
#agrupa los datos en vectores de cuatro dimensiones
def agruparDatos(datos):
    return [datos[x:x+4] for x in range(0, len(datos), 4)]


def pruebaSeries(datos, confianza, dimensiones):
    total_datos = len(datos)
    total_grupos = total_datos/dimensiones
    total_clases = math.ceil(math.sqrt(total_grupos))

    clases_por_dimension = math.ceil(math.pow( math.sqrt(total_grupos),1/dimensiones))
    total_clases_por_dimension =  math.pow(clases_por_dimension,dimensiones)

    datos_agrupados = agruparDatos(datos)
    frecuencias_observadas = frecuenciasObservadas(datos_agrupados) 
    frecuencia_esperada = total_grupos/total_clases_por_dimension
    chiCuadrados = list(map(lambda fo: ChiCuadrado.calcularChiCuadrado(frecuencia_esperada,fo),frecuencias_observadas.values()))
    xcalc = ChiCuadrado.calcularChiCuadrados(chiCuadrados)
    xcrit = 0
    
#retorna los posibles combinaciones de clases que puede tener un vector para cada uno de sus numeros
def posiblesCombinaciones():
    cuenta={}
    for i in [1,2]:
            
        for j in [1,2]:
                
            for k in [1,2]:
                    
                for l in [1,2]:
                    cuenta[f'{i}-{j}-{k}-{l}']=0
    return cuenta

# se tienen dos intervalos [0, 0.5),[0.5, 1]
def frecuenciasObservadas(datos):
    combinaciones=[]
    for dato in datos:
        clase=''
        for numero in dato:
            if(numero<0.5):
                clase+='1-'
            else:
                clase+='2-'
        clase=clase[:-1]
        combinaciones.append(clase)
    combinaciones.pop()

    posibles_combinaciones = posiblesCombinaciones()

    for combinacion in combinaciones:
        posibles_combinaciones[combinacion]+=1
    
    return posibles_combinaciones