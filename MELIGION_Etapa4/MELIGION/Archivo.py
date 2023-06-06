import Escrutinio
import Diccionario

def leer(sDirectorio):
    """Devuelve en una la lista las líneas encontradas en el archivo sDirectorio"""
    lDatos = [] #guarda datos de linea
    lRegistro = [] #guarda listas
    try: 
        oArchivo = open(sDirectorio, "rt", encoding="UTF-8")
        sLinea = oArchivo.readline()
        while sLinea:
            sListado = sLinea.rstrip("\n")
            lDatos = sListado.split(";")
            lRegistro.append(lDatos)
            sLinea = oArchivo.readline()
    except OSError as mensaje:
        pass
    finally:
        try:
            oArchivo.close()
        except NameError:
            pass
        finally:
            return lRegistro

def guardar(sDirectorio, lRegistro):
    """Guarda los valores de la lista lRegistro en el archivo sDirectorio"""
    try:
        oArchivo = open(sDirectorio, "wt")
        for datos in lRegistro:
            sLinea = ";".join(datos)
            sLinea = sLinea + "\n"
            oArchivo.write(sLinea)
    except OSError as mensaje:
        print("No se pudo guardar el archivo: ", mensaje)
    finally:
        try:
            oArchivo.close()
        except NameError:
            pass
        
def leerVotos(sDirectorio, sCargo):
    """Devuelve en una la lista de votos encontrados
    de acuerdo a sCargo en el archivo sDirectorio"""
    lVoto = [] #guarda datos de linea
    lVotos = [] #guarda listas
    try: 
        oArchivo = open(sDirectorio, "rt", encoding="UTF-8")
        
        for sLinea in oArchivo:
            sDatos = sLinea.rstrip("\n")
            lVoto = sDatos.split(";")
            if lVoto[2] == sCargo:
                lVotos.append(lVoto)
    except OSError as mensaje:
        pass
    finally:
        try:
            oArchivo.close()
        except NameError:
            pass
        finally:
            return lVotos
       
def guardarEleccion(dRegistroElectoral):
    """Guarda el registro electoral en el archivo que tiene por nombre la clave de dRegistroElectoral"""
    try:
        for sNomArchivo in dRegistroElectoral:
            lRegistro = dRegistroElectoral[sNomArchivo]
            oArchivo = open(sNomArchivo, "wt", encoding="UTF-8")
            
            for lDato in lRegistro:
                sLinea = ";".join(lDato)
                sLinea = sLinea + "\n"
                oArchivo.write(sLinea)
    except OSError as mensaje:
        pass
    finally:
        try:
            oArchivo.close()
        except NameError:
            pass
        
def obtenerPartido():
    """Devuelve un diccionario de los partidos con la abreviatura como clave"""
    sRuta = "boletas.txt"
    lPartidos = leer(sRuta)
    dPartidos = Diccionario.generarDicCodLista(lPartidos)
    return dPartidos

def leerVotosPresidencial(dPartidos):
    """Devuelve un diccionario con los votos totales
    obtenidos por partido a nivel nacional"""
    lArchivos = [
        "SANTAFE_PRESIDENTE.CSV",
        "CATAMARCA_PRESIDENTE.CSV",
        "RÍONEGRO_PRESIDENTE.CSV",
        "SALTA_PRESIDENTE.CSV",
        "JUJUY_PRESIDENTE.CSV",
        "FORMOSA_PRESIDENTE.CSV",
        "CHACO_PRESIDENTE.CSV",
        "CORRIENTES_PRESIDENTE.CSV",
        "MISIONES_PRESIDENTE.CSV",
        "SANTIAGODELESTERO_PRESIDENTE.CSV",
        "LARIOJA_PRESIDENTE.CSV",
        "TUCUMÁN_PRESIDENTE.CSV",
        "SANJUAN_PRESIDENTE.CSV",
        "SANLUIS_PRESIDENTE.CSV",
        "BUENOSAIRES_PRESIDENTE.CSV",
        "CÓRDOBA_PRESIDENTE.CSV",
        "LAPAMPA_PRESIDENTE.CSV",
        "CHUBUT_PRESIDENTE.CSV",
        "SANTACRUZ_PRESIDENTE.CSV",
        "TIERRASDELFUEGO_PRESIDENTE.CSV",
        "ENTRERÍOS_PRESIDENTE.CSV",
        "MENDOZA_PRESIDENTE.CSV",
        "NEUQUÉN_PRESIDENTE.CSV",
              ]
    dVotoNacional = {}
    lVoto = [] #guarda datos de linea
    lVotos = [] #guarda listas
    for sDirectorio in lArchivos:

        try:
                oArchivo = open(sDirectorio, "rt", encoding="UTF-8")
                
                for sLinea in oArchivo:
                    sDatos = sLinea.rstrip("\n")
                    lVoto = sDatos.split(";")
                    sCodLista = lVoto[1]
                    lAbreviatura = dPartidos.get(sCodLista, "")
    #                     Guardado de las abreviaturas de los partidos como clave
                    if lAbreviatura != "":
                        sPartido = lAbreviatura[0]
                    else:
                        sPartido = lAbreviatura
                    if Diccionario.esClave(dVotoNacional, sPartido):
                        iCantVotos = int(lVoto[2])
                        dVotoNacional[sPartido] += iCantVotos
                    else:
                        iCantVotos = int(lVoto[2])
                        dVotoNacional[sPartido] = iCantVotos
                       
        except OSError as mensaje:
            pass
        finally:
            try:
                oArchivo.close()
            except NameError:
                pass
    return dVotoNacional