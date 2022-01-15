import math

from pruebas.util import frecuenciaObservada
from . import ChiCuadrado
from tabulate import tabulate
#agrupa los datos en vectores de cuatro dimensiones
def agruparDatos(datos,dimensiones):
    return [datos[x:x+dimensiones] for x in range(0, len(datos), dimensiones)]


def pruebaSeries(datos, confianza, dimensiones):
    total_datos = len(datos)
    total_grupos = total_datos/dimensiones
    total_clases = math.ceil(math.sqrt(total_grupos))

    clases_por_dimension = math.ceil(math.pow( math.sqrt(total_grupos),1/dimensiones))
    total_clases_por_dimension =  math.pow(clases_por_dimension,dimensiones)
    datos_agrupados = agruparDatos(datos,dimensiones)
    #para el de 3 dimensiones
    # frecuencias_observadas = frecuenciasObservadas(datos_agrupados) 
    #para el de 2 dimensiones
    print(datos_agrupados)
    frecuencias_observadas = frecuenciasObservadasTres(datos_agrupados) 
    frecuencia_esperada = total_grupos/total_clases_por_dimension
    chiCuadrados = list(map(lambda fo: ChiCuadrado.calcularChiCuadrado(frecuencia_esperada,fo),frecuencias_observadas.values()))
    xcalc = sum(chiCuadrados)
    # xcrit = 22.307
    # xcrit=12.02 #xcrit para grado 7
    xcrit=13.36 #xcrit para grado 8
    return [xcalc,xcrit,frecuencias_observadas,frecuencia_esperada,chiCuadrados]

    
#retorna los posibles combinaciones de clases que puede tener un vector para cada uno de sus numeros
def posiblesCombinaciones():
    cuenta={}
    for i in [1,2]:
            
        for j in [1,2]:
                
            for k in [1,2]:
                    
                for l in [1,2]:
                    cuenta[f'{i}-{j}-{k}-{l}']=0
    return cuenta
def posiblesCombinaciones3Dimensiones():
    cuenta={}
    for i in [1,2]:
            
        for j in [1,2]:
                
            for k in [1,2]:
                    
                cuenta[f'{i}-{j}-{k}']=0
    return cuenta
def posiblesCombinaciones2Dimensiones():
    cuenta={}
    for i in [1,2,3]:
            
        for j in [1,2,3]:
                cuenta[f'{i}-{j}']=0
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

    posibles_combinaciones = posiblesCombinaciones3Dimensiones()

    for combinacion in combinaciones:
        posibles_combinaciones[combinacion]+=1
    
    return posibles_combinaciones
# se tienen tres intervalos [0, 0.3),[0.3, 0.6),[0.6, 1]
def frecuenciasObservadasTres(datos):
    combinaciones=[]
    for dato in datos:
        clase=''
        for numero in dato:
            if(numero<0.33333):
                clase+='1-'
            elif(numero<0.66666):
                clase+='2-'
            else: clase+='3-'
        clase=clase[:-1]
        combinaciones.append(clase)
    
    combinaciones.pop()

    posibles_combinaciones = posiblesCombinaciones2Dimensiones()

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
    # print(values)
    print(tabulate(values, cabecera, tablefmt="grid"))
  