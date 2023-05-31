from modulos import Archivo
from modulos import Pantalla
from modulos import Diccionario
from modulos import Escrutinio

lOpcion = Pantalla.menuEscrutinio()

sRuta = "archivo_votacion.csv"
lVotos = Archivo.leerVotos(sRuta, lOpcion[0])

dVotosRegiones=Escrutinio.generarVotoRegion(lVotos)
dVotosTotales=Escrutinio.contarVotosRegion(dVotosRegiones)
dRegionPartido= Escrutinio.contarVotosPartido(dVotosRegiones)

dRegistroElectoral = Escrutinio.archivar(dRegionPartido, lOpcion[1])

##print(dVotosTotales)
##print(dRegistroElectoral)

Archivo.guardarEleccion(dRegistroElectoral)

print("\n"*2)
Pantalla.mostrarEscrutinio(dRegistroElectoral, dVotosTotales, lOpcion[1])