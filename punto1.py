import re
from pruebas import util
from pruebas import Corridas
from pruebas import ChiCuadrado
from pruebas import Poker


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

#c Para los dos generadores aplicar Implemente una prueba depóker, con k=3, recuerde generar los números con al menos 3,
# su aplicación debe tener como salida la tabla en la que se evalúan los número.  Usando confianza del 5%
def puntoc():
    datos_puntoa = util.normalizar(puntoa())
    datos_puntob = util.normalizar(puntob())
    CONFIANZA = 0.05
    Poker.poker3Tabla(datos_puntoa, CONFIANZA)
    Poker.poker3Tabla(datos_puntob, CONFIANZA)

#d  Hacer pruebas de corridas para ambos puntos, usando la media como punto de comparación.
def puntod():
    datos_puntoa = util.normalizar(puntoa())
    datos_puntob = util.normalizar(puntob())
    CONFIANZA = 0.05
    Corridas.mostrarCorridas(datos_puntoa, CONFIANZA)
    Corridas.mostrarCorridas(datos_puntob, CONFIANZA)

#e aplicar a ambos puntos pruebas de chi cuadrado. Con una confianza del 5%
def puntoe():
    datos_puntoa = util.normalizar(puntoa())
    datos_puntob = util.normalizar(puntob())
    CONFIANZA = 0.05
    ChiCuadrado.chiCuadradoTabla(datos_puntoa, CONFIANZA)
    ChiCuadrado.chiCuadradoTabla(datos_puntob, CONFIANZA)
