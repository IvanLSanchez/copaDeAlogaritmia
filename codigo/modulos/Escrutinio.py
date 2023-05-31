from modulos import Diccionario
from modulos import Archivo
import random
    
def asignarVoto(dPadron, dRegiones):
    sArchBoletas = "boletas.txt"
    lPartidosMemoria = Archivo.leer(sArchBoletas)
    lPadron = list(dPadron.keys())
    lRegiones = list(dRegiones.keys())
    for iDNI in lPadron:
        lVotoDNI = []
        iVota = random.randint(1, 10)
        iMax = len(lPartidosMemoria)-1
        sDNI = str(iDNI)
        sVotoCargo = str(random.randint(1, 4))                
        if iVota > 1:
            iPosicion = random.randint(0, iMax)
            iVotoPartido = lPartidosMemoria[iPosicion][1]
        else:
            iVotoPartido = ""
        lVotoDNI.append(sDNI)
        for clave in dRegiones:
            if sDNI in dRegiones[clave]:
                lVotoDNI.append(clave)
        lVotoDNI.append(sVotoCargo)
        lVotoDNI.append(iVotoPartido)
        #[555, 1, 2, LBD]
        dPadron[iDNI].append(lVotoDNI)
        
def generarRegion(dPadron, lRegionMemoria):
    iMax = len(lRegionMemoria)-1
    dRegiones = {}
    for iDNI in dPadron:
        iPosicion = random.randint(1, iMax)
        iVotoRegion = lRegionMemoria[iPosicion][1]
        
        #{1:[345, 555], 4:[222]}
        #Validación existencia de la región
        if Diccionario.esClave(dRegiones, iVotoRegion):
          dRegiones[iVotoRegion].append(str(iDNI))
        else:
          dRegiones[iVotoRegion] = []
          dRegiones[iVotoRegion].append(str(iDNI))
    return dRegiones

def generarPadron(iRegistros):
    dPadron = {}
    for i in range(iRegistros):
        iVotoDNI = random.randint(1, 99999999)
        #Validación de la existencia del documento
        bEsInvalido = Diccionario.esClave(dPadron, iVotoDNI)
        while bEsInvalido:
          iVotoDNI = random.randint(1, 99999999)
          bEsInvalido = Diccionario.esClave(dPadron, iVotoDNI)
        dPadron[iVotoDNI] = []
    return dPadron