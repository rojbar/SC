import math

#calcula la media de una secuencia de numeros
def calcularMedia(datos):
    totalDatos = 0
    for dato in datos:
        totalDatos += dato
    return totalDatos/len(datos)

def calcularMediaCorridas(n1, n2):
    return ((2*n1*n2)/(n1+n2)) + 1

def caclularVarianzaCorridas(n1,n2):
    return 2*n1*n2*(2*n1*n2-n1-n2)/(math.pow(n1+n2, 2)*(n1+n2-1))

def calcularEstadistico(media_esperada_corridas, desviacion_estandar, total_corridas ):
    return (total_corridas - media_esperada_corridas)/desviacion_estandar

#retorna el total de corridas y la cantidad de - y +
def contarCorridas(datos):
    positivo = 0
    negativo = 0
    anterior = 0
    corridas = 0
    for index,dato in enumerate(datos):
        if(dato == '+'):
            positivo += 1
        else:
            negativo += 1

        if(index == 0):
            anterior = dato
            continue
        if(dato != anterior):
            corridas += 1

        anterior = dato
    return [positivo, negativo, corridas]

#formatea los datos si estan arriba o debajo de la media
def formatearDatos(datos, media):
    datos_formateado = []
    for dato in datos:
        if(dato <= media):
            datos_formateado.append('-')
        else:
            datos_formateado.append('+')
    return datos_formateado

#donde los datos es una lista de numeros
def corridasArribaAbajoMedia(datos,confianza):
    media = calcularMedia(datos)
    datos_formateado = formatearDatos(datos, media)
    total_positivos, total_negativos, total_corridas = contarCorridas(datos_formateado)
    media_esperada_corridas = calcularMediaCorridas(total_positivos, total_negativos)
    desviacion_estandar = math.sqrt(caclularVarianzaCorridas(total_positivos, total_negativos))
    estadistico = calcularEstadistico(media_esperada_corridas,desviacion_estandar, total_corridas)

    estadistico_normal = {
        0.05: 1.96,
        0.06: 1.88,
        0.07: 1.81,
        0.08: 1.75,
        0.09: 1.69,
        0.1: 1.65,
        0.2: 1.28,
        0.377: 1,
        0.5: 0.67
    }
    es_random = abs(estadistico) < estadistico_normal[confianza]

    return [
        media,total_positivos, 
        total_negativos, 
        total_corridas, 
        media_esperada_corridas, 
        desviacion_estandar,
        estadistico, 
        estadistico_normal[confianza], 
        es_random]
    
def mostrarCorridas(datos, confianza):
    res = corridasArribaAbajoMedia(datos,confianza)
    media = res[0]
    total_positivos = res[1]
    total_negativos = res[2]
    total_corridas = res[3]
    media_esperada_corridas = res[4]
    desviacion_estandar = res[5]
    estadistico = res[6]
    estadistico_normal = res[7] 
    es_random = res[8]

    print(f"Media de los datos: {media}")
    print(f"Total positivos: {total_positivos}") 
    print(f"Total negativos: {total_negativos}") 
    print(f"Total corridas: {total_corridas}")
    print(f"Media esperada corridas: {media_esperada_corridas}") 
    print(f"Desviacion estandar: {desviacion_estandar}")
    print(f"Estadistico calculado: {estadistico}")
    print(f"Estadistico normal: {estadistico_normal}") 
    print(f"Es el generador aleatorio? : {es_random}")
     