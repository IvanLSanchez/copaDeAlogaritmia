from modulos import Archivo
from modulos import Pantalla
from modulos import Diccionario
from modulos import Escrutinio

sOpcion = Pantalla.menuEscrutinio()

sRuta = "archivo_votacion.csv"
lVotos = Archivo.leerVotos(sRuta, sOpcion)

dVotosRegiones=Escrutinio.generarVotoRegion(lVotos)
dVotosTotales=Escrutinio.contarVotosRegion(dVotosRegiones)
