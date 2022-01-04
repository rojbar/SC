import re
import pruebas.Corridas as Corridas
import pruebas.ChiCuadrado as ChiCuadrado
import util
#https://docs.python.org/3/howto/regex.html#regex-howto

# a) 
# Descargar 100 años de soledad en pdf o en texto y realizar un seudo generador usando python, escoger las palabras que
# están después de cada signo gramatical y tomar el tamaño de las mismas, y generar una lista de 1000 números.
#
# caso1 [^.,;:_\-?¿...!¡"'()«»\s]+ //estas son las palabras que estan inmediatamente despues de un signo
# caso2 \s[^.,;:_\-?¿...!¡"'()«»\s]+ //estas son las palabras que estan despues de un espacio de un signo
#[.,;:_\-?¿...!¡"'()«»](caso1|caso2)
def puntoa():

    signos = ['.',',',';',':','_','\-','?','¿','...','!','¡','"',"'",'(',')','«','»']
    cadenaSignos = r"".join(signos)
    patron = rf"[{cadenaSignos}]([^{cadenaSignos}\s]+|\s[^{cadenaSignos}\s]+)"
    
    libro = open("cien.txt")
    cadena = libro.read()
    libro.close()
    
    cadena = cadena.replace( '\n', '')
    p = re.compile(patron)
    res = p.findall(cadena)
    
    numeros = []
    for index,palabra in enumerate(res):
        if(index == 1000):
            break
        numeros.append(len(palabra.split()[0]))
        
    #print(numeros)
    return numeros
# b)
# Usando el mismo texto contar el número de caracteres que hay entre cada signo gramatical y generar 1000 números.
def puntob():

    signos = ['.',',',';',':','_','\-','?','¿','...','!','¡','"',"'",'(',')','«','»']
    cadenaSignos = r"".join(signos)
    patron = rf"([^{cadenaSignos}]*)[{cadenaSignos}]"
    
    libro = open("cien.txt")
    cadena = libro.read()
    libro.close()
    
    cadena = cadena.replace( '\n', '')
    
    p = re.compile(patron)
    res = p.findall(cadena)
    
    numeros = []

    for index,palabra in enumerate(res):
        if(index == 1000):
            break
        numeros.append(len(palabra))
        
    #print(numeros)
    return numeros
        

#c

#d
def puntod():
    datos_puntoa = puntoa()
    datos_puntob = puntob()
    CONFIANZA = 0.05
    Corridas.mostrarCorridas(list(map(lambda x: x/util.max(datos_puntoa), datos_puntoa)), CONFIANZA)
    Corridas.mostrarCorridas(list(map(lambda x: x/util.max(datos_puntob), datos_puntob)), CONFIANZA)

#e aplicar a ambos puntos pruebas de chi cuadrado. Con una confianza del 5%
def puntoe():
    datos_puntoa = puntoa()
    datos_puntob = puntob()
    CONFIANZA = 0.05
    ChiCuadrado.chiCuadradoTabla(list(map(lambda x: x/util.max(datos_puntoa), datos_puntoa)), 0.05)
    ChiCuadrado.chiCuadradoTabla(list(map(lambda x: x/util.max(datos_puntob), datos_puntob)), 0.05)
