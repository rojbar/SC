#retorna el numero mas grande de una lista de numeros
def max(datos):
    max = datos[0]
    for num in datos:
        if(num >= max):
            max = num
    return max