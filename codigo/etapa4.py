from modulos import Archivo
from modulos import Escrutinio
from modulos import Diccionario
from modulos import Pantalla

dPartidos=Archivo.obtenerPartido()
dVotoNacional = Archivo.leerVotosPresidencial(dPartidos)

if dVotoNacional != {}:
    dVotoNacional=Diccionario.ordenarDiccionario(dVotoNacional)
    iVotosTotales = Escrutinio.calcularVotosTotales(dVotoNacional)
    lMayoresFuerzas=Escrutinio.calcularMayoresFuerzas(dVotoNacional)

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
    
    Escrutinio.asignarVoto(dPadron, lMayoresFuerzas)
    
    lVotos = Diccionario.cambiarALista(dPadron)
    
    #Guardado de los votos del padrón
    Archivo.guardar(sRuta, lVotos)
