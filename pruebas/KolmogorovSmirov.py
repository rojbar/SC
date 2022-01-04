from . import util
import math
from tabulate import tabulate

#los datos deben de pasarse normalizados
def pruebaKolmogorov_Smirov(datos, confianza):
    numero_datos = len(datos)
    numero_clases = util.numeroClases(numero_datos)
    clases = util.crearClases(int(numero_clases))

    frecuencias_observadas = util.frecuenciasObservadas(clases,datos)
    frecuencias_esperadas = util.frecuenciasEsperadas(numero_datos,numero_clases)
    
    frecuencias_observadas_acumuladas = util.acumula(frecuencias_observadas)

    probabilidades_observadas = list(map(lambda x: x/numero_datos,frecuencias_observadas))
    probabilidades_observadas_acumuladas = util.acumula(probabilidades_observadas)
    
    probabilidades_esperadas  = list(map(lambda x: x/numero_datos, frecuencias_esperadas))
    probabilidades_esperadas_acumuladas = util.acumula(probabilidades_esperadas)

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

