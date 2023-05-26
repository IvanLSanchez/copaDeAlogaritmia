import random
from modulos import Archivo
from modulos import Escrutinio
from modulos import Diccionario


iRegistros = int(input("Ingrese cantidad de registros: "))
sRuta = "archivo_votacion.csv"

lPadronElectoral = Archivo.leer(sRuta)

dRecuentoRegion = Diccionario.generarDiccionario(lPadronElectoral, 1, 0)

dPadron = Escrutinio.generarPadron(iRegistros)

dRegiones = Escrutinio.generarRegion(dPadron)

Escrutinio.asignarVoto(dPadron)

lVotos = Diccionario.cambiarALista(dPadron)

#Guardado de los votos del padrón
Archivo.guardar(sRuta, lVotos)