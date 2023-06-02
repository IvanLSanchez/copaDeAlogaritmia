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

if sOpcion ==  '3':
    dSenadores = Escrutinio.obtenerSenadores(dRegionPartido)
    Pantalla.mostrarSenadores(dSenadores)
elif sOpcion == '2':
    dVotosTotales=Escrutinio.contarVotosRegion(dVotosRegiones)
    Pantalla.mostrarDiputados(dRegionPartido, dVotosTotales, sCargo)
else:    
    dVotosTotales=Escrutinio.contarVotosRegion(dVotosRegiones)
    Pantalla.mostrarPresidentesGobernadores(dRegionPartido, dVotosTotales, sCargo)
