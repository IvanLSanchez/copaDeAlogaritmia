from modulos import Archivo
from modulos import Pantalla
from modulos import Escrutinio

sRuta = "archivo_votacion.csv"
lVotos = Archivo.leerVotos(sRuta, "1")

sCargo = "PRESIDENTE"

dVotosRegiones=Escrutinio.generarVotoRegion(lVotos)
dRegionPartido = Escrutinio.contarVotosPartido(dVotosRegiones)

dRegistroElectoral = Escrutinio.archivar(dRegionPartido, sCargo)

Archivo.guardarEleccion(dRegistroElectoral)

dVotosTotales=Escrutinio.contarVotosRegion(dVotosRegiones)

print(dVotosTotales)
Pantalla.mostrarPresidentesBalotaje(dRegionPartido, dVotosTotales, sCargo)

## Mostrar Ganador y porcentaje total pais
dTotales = Escrutinio.obtenerSenadores(dRegionPartido)
Pantalla.mostrarResultadosBalotaje(sCargo, dRegionPartido, dTotales)