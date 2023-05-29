from modulos import Archivo
from modulos import Escrutinio
from modulos import Diccionario
from modulos import Pantalla

sEspeciales=" ¡!\"#$%‰&'()*+,-./0-9:;<<=>>?@A-Z[]^_`{}\\"

try:
    sN = input("Ingrese cantidad de registros: ")
    while sN=="" or sN.isalpha() or not sN.isdigit() or int(sN)<=0:
        print("Valor NO válido\n")
        sN = input("Ingrese cantidad de registros: ")
except ValueError:
        print("Valor NO válido\n")
        sN = input("Ingrese cantidad de registros: ")

iRegistros = int(sN)

sRuta = "archivo_votacion.csv"
sRegiones = "regiones.txt"

lRegionMemoria = Archivo.leer(sRegiones)

dPadron = Escrutinio.generarPadron(iRegistros, lRegionMemoria)

dRegiones = Escrutinio.generarRegion(dPadron, lRegionMemoria)

Escrutinio.asignarCargo(dPadron)

Escrutinio.asignarVoto(dPadron)

lVotos = Diccionario.cambiarALista(dPadron)

#Guardado de los votos del padrón
Archivo.guardar(sRuta, lVotos)

#Visualización de los votos
Pantalla.mostrarVotos(lRegionMemoria, dRegiones)