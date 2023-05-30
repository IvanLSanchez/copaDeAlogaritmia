def leer(sDirectorio):
    """Devuelve en una la lista las líneas encontradas en el archivo sDirectorio"""
    lDatos = [] #guarda datos de linea
    lRegistro = [] #guarda listas
    try: 
        oArchivo = open(f"../codigo/baseDeDatos/{sDirectorio}", "rt", encoding="UTF-8")
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
        oArchivo = open(f"codigo/baseDeDatos/{sDirectorio}", "at")
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
        oArchivo = open(f"codigo/baseDeDatos/{sDirectorio}", "rt", encoding="UTF-8")
        
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