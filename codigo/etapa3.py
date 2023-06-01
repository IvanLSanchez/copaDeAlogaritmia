from modulos import Archivo
from modulos import Pantalla
from modulos import Escrutinio

sOpcion, sCargo = Pantalla.menuEscrutinio()

sRuta = "archivo_votacion.csv"
lVotos = Archivo.leerVotos(sRuta, sOpcion)

dVotosRegiones=Escrutinio.generarVotoRegion(lVotos)
dRegionPartido = Escrutinio.contarVotosPartido(dVotosRegiones)

dRegistroElectoral = Escrutinio.archivar(dRegionPartido, sCargo)

Archivo.guardarEleccion(dRegistroElectoral)

if sOpcion !=  '3':
    dVotosTotales=Escrutinio.contarVotosRegion(dVotosRegiones)
    Pantalla.mostrarEscrutinio(dRegionPartido, dVotosTotales, sCargo)
else:
    dSenadores = Escrutinio.obtenerSenadores(dRegionPartido)
    Pantalla.mostrarSenadores(dSenadores)
