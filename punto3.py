from pruebas import KolmogorovSmirov
from pruebas import Corridas
from pruebas import Series

datos = [
    0.3163,	0.4438,	0.5747,	0.1908,	0.2829,	0.6034,	0.2011,	0.6643,	0.9016,	0.2913,
    0.1319,	0.6235,	0.6208,	0.9173,	0.2296,	0.6305,	0.7348,	0.3657,	0.425,	0.52,
    0.7299,	0.3847,	0.685,	0.9083,	0.1024,	0.7366,	0.2248,	0.7218,	0.2277,	0.6495,
    0.9208,	0.7804,	0.592,	0.7126,	0.8892,	0.7757,	0.7795,	0.6775,	0.3438,	0.2234,
    0.2948,	0.6049,	0.7617,	0.5667,	0.0706,	0.4907,	0.0686,	0.4993,	0.7706,	0.591,
    0.7113,	0.5349,	0.8835,	0.0349,	0.3063,	0.237,	0.0985,	0.7607,	0.5853,	0.9042,
    0.0049,	0.962,	0.4767,	0.9255,	0.5806,	0.1856,	0.0508,	0.4864,	0.7624,	0.2841,
    0.8394,	0.3062,	0.1635,	0.6599,	0.4443,	0.0346,	0.026,	0.2889,	0.6681,	0.764,
    0.9723,	0.9096,	0.4579,	0.8236,	0.3435,	0.9882,	0.0777,	0.6874,	0.3303,	0.5752
]

#Las siguientes pruebas de bondad usarlas con un valor de confianza de 0.1
CONFIANZA = 0.1

#a Realice una prueba deKolmogorov-Smirnov
def puntoa():
    KolmogorovSmirov.kolmogorovTabla(datos,CONFIANZA)

#b. Realice una prueba de corridas por encima y debajo de la media
def puntob():
    Corridas.mostrarCorridas(datos,CONFIANZA)

#c. Realice una prueba de series con k=4.
def puntoc():
    Series.pruebaSeries(datos, CONFIANZA, 4)
    