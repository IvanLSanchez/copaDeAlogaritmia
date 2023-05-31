from modulos import Archivo
from modulos import Pantalla
from modulos import Escrutinio

sOpcion, sCargo = Pantalla.menuEscrutinio()

sRuta = "archivo_votacion.csv"
lVotos = Archivo.leerVotos(sRuta, sOpcion)

dVotosRegiones=Escrutinio.generarVotoRegion(lVotos)
dVotosTotales=Escrutinio.contarVotosRegion(dVotosRegiones)
dRegionPartido = Escrutinio.contarVotosPartido(dVotosRegiones)

dRegistroElectoral = Escrutinio.archivar(dRegionPartido, sCargo)

Archivo.guardarEleccion(dRegistroElectoral)

Pantalla.mostrarEscrutinio(dRegionPartido, dVotosTotales, sCargo)