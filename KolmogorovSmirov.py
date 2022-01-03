import math
import util
from tabulate import tabulate


#retorna la frecuencia observado de datos para un intervalo (limInferior, limSuperior]
def frecuenciaObservada(limiteInferior, limiteSuperior, datos):
    frecuencia = 0
    for dato in datos:
        if(dato > limiteInferior and dato <= limiteSuperior):
            frecuencia += 1
    return frecuencia

#retorna una lista de las frecuencias obersavadas para cada intervalo en una lista
def frecuenciasObservadas(intervalos, datos):
    frecuencias = []
    for intervalo in intervalos:
        frecuencias.append(frecuenciaObservada(intervalo[0], intervalo[1], datos))
    return frecuencias

#retorna una lista de intervalos
def intervalos(clases):
    longitud_intervalo = 1/clases
    intervalos_ = []
    for i in range(clases):
        intervalos_.append([longitud_intervalo*i, longitud_intervalo*(i+1)])
    return intervalos_

#retorna una lista de las frecuencias esperadas
def frecuenciasEsperadas(datos, clases):
    frec_esperada = datos/clases
    frecuenciaEperada = []
    for i in range(clases):
        frecuenciaEperada.append(frec_esperada)
    return frecuenciaEperada

#retorna una lista de los datos acumuladas
def acumula(probabilidades):
    probs = []
    for index, probabilidad in enumerate(probabilidades):
        if(index == 0):
            probs.append(probabilidad)
            continue
        probs.append(probabilidad+probs[index-1])
    return probs

#los datos deben de pasarse normalizados
def pruebaKolmogorov_Smirov(datos, confianza):
    numero_datos = len(datos)
    numero_clases = math.ceil(math.sqrt(numero_datos))
    clases = intervalos(int(numero_clases))

    frecuencias_observadas = frecuenciasObservadas(clases,datos)
    frecuencias_esperadas = frecuenciasEsperadas(numero_datos,numero_clases)
    frecuencias_observadas_acumuladas = acumula(frecuencias_observadas)

    probabilidades_observadas = list(map(lambda x: x/numero_datos,frecuencias_observadas))
    probabilidades_observadas_acumuladas = acumula(probabilidades_observadas)
    
    probabilidades_esperadas  = list(map(lambda x: x/numero_datos, frecuencias_esperadas))
    probabilidades_esperadas_acumuladas = acumula(probabilidades_esperadas)

    pea_menos_pao = list(map(lambda poa,pea: abs(pea-poa), probabilidades_observadas_acumuladas, probabilidades_esperadas_acumuladas))
    dm = util.max(pea_menos_pao)
    dm_critico = 0
    
    if(confianza == 0.1):
        dm_critico = 1.22/(math.sqrt(numero_datos))
    if(confianza == 0.05):
        dm_critico = 1.36/(math.sqrt(numero_datos))
    if(confianza == 0.01):
        dm_critico = 1.63/(math.sqrt(numero_datos))
    
    pasa = False

    if(dm <= dm_critico):
        pasa = True

    res = []
    for fila in zip(clases,frecuencias_observadas, frecuencias_observadas_acumuladas, probabilidades_observadas_acumuladas, probabilidades_esperadas_acumuladas, pea_menos_pao):
         res.append(fila)
    return  [res, dm, dm_critico, pasa]

#funcion que genera una tabla para la prueba
def kolmogorovTabla(datos, confianza):
    res = pruebaKolmogorov_Smirov(datos, confianza)
    print(f"DMcalc = {res[1]}")
    print(f"DMcritico = {res[2]}")

    if(res[3]):
        print("El generador es bueno en cuanto a uniformidad pues dmcalc es menor o igual a dmcritico")
    else:
        print("El generador no es bueno en cuanto a uniformidad dmcalc  no es menor o igual a dmcritico")

    cabecera = ["clase", "FO", "FOA", "POA", "PEA", "|PEA-POA|"]
    print(tabulate(res[0], cabecera, tablefmt="grid"))

