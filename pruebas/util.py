#retorna el numero mas grande de una lista de numeros
def max(datos):
    max = datos[0]
    for num in datos:
        if(num >= max):
            max = num
    return max

#normalizacion de numero al rango [0,1]
def normalizar(datos):
    datos_normalizados = []
    maximo = max(datos)
    for dato in datos:
        datos_normalizados.append(dato/maximo)
    return datos_normalizados