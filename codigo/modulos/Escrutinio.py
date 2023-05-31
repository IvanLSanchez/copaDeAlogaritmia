import Diccionario
import Archivo
import random

def asignarVoto(dPadron):
    """Asigna un voto al azar para cada votante"""
    sArchBoletas = "boletas.txt"
    lPartidosMemoria = Archivo.leer(sArchBoletas)
    for iDNI in dPadron:
        lVotoDNI = []
        iMax = len(lPartidosMemoria)-1
        for lDato in dPadron[iDNI]:
            iVota = random.randint(1, 10)
            if iVota > 1:
                iPosicion = random.randint(0, iMax)
                sVotoPartido = lPartidosMemoria[iPosicion][1]
            else:
                sVotoPartido = ""
            lDato.append(sVotoPartido)

def asignarCargo(dPadron):
    """Se asigna un voto de cargo público al elector"""
    iMax = 4
    dRegiones = {}
    for iDNI in dPadron:
        iCargo = random.randint(1, iMax)
        sCargo = str(iCargo)
        #Se asigna a la n cantidad de votos del mismo DNI
        #la misma región 
        for lDato in dPadron[iDNI]:
            while sCargo in lDato:
                iCargo = random.randint(1, iMax)
                sCargo = str(iCargo)
            lDato.append(sCargo)

def generarRegion(dPadron, lRegionMemoria):
    """Genera una región al azar de acuerdo a las obtenidas en lRegionMemoria"""
    iMax = len(lRegionMemoria)-1
    dRegiones = {}
    for iDNI in dPadron:
        iPosicion = random.randint(1, iMax)
        iRegion = lRegionMemoria[iPosicion][1]
        sRegion = str(iRegion)
        #Se asigna a la n cantidad de votos del mismo DNI
        #la misma región 
        for lDato in dPadron[iDNI]:
            lDato.append(sRegion)

        #Validación existencia de la región
        if Diccionario.esClave(dRegiones, iRegion):
          dRegiones[iRegion].append(str(iDNI))
        else:
          dRegiones[iRegion] = []
          dRegiones[iRegion].append(str(iDNI))
    return dRegiones

def generarPadron(iRegistros, lRegionMemoria):
    """Genera el padrón electoral de acuerdo a la cantidad deseada"""
    dPadron = {}
    for i in range(iRegistros):
        lVoto = []
        iDNI = random.randint(1, 99999999)
        if Diccionario.esClave(dPadron, iDNI):
            lVoto.append(str(iDNI))
            dPadron[iDNI].append(lVoto)
        else:
            dPadron[iDNI] = []
            lVoto.append(str(iDNI))
            dPadron[iDNI].append(lVoto)
    return dPadron