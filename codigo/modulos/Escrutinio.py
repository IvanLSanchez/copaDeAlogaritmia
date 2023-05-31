from modulos import Diccionario
from modulos import Archivo
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
    for iDNI in dPadron:
        #Se asigna a la n cantidad de votos del mismo DNI y misma región
        lMatriz=dPadron[iDNI]
        iLongitud=len(lMatriz)
        for lDato in lMatriz:
            bRepetir=True
            iCargo = random.randint(1, iMax)
            sCargo = str(iCargo)
            while bRepetir:
                bExiste=False
                #Posición 2 es donde está el cargo
                for iPos in range(iLongitud):
                    lVotos=lMatriz[iPos]
                    if len(lVotos)==3:
                        if sCargo==lVotos[2]:
                            bExiste=True
                if bExiste:
                    iCargo = random.randint(1, iMax)
                    sCargo = str(iCargo)
                else:
                    bRepetir=False
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
        bRepetir=True
        lVoto = []
        iDNI = random.randint(1, 99999999) 
        while bRepetir:
            if Diccionario.esClave(dPadron, iDNI):
                if len(dPadron[iDNI])<4:
                    bRepetir=False
                    lVoto.append(str(iDNI))
                    dPadron[iDNI].append(lVoto)
                else:
                    bRepetir=True
                    iDNI = random.randint(1, 99999999)
            else:
                bRepetir=False
                dPadron[iDNI] = []
                lVoto.append(str(iDNI))
                dPadron[iDNI].append(lVoto)
    return dPadron

def generarVotoRegion(lLista):
    """Crea un diccionario a partir de una lista
    con clave con iPosClave"""
    iPosClave=1
    dDiccionario = {}
    for lDatos in lLista:
        clave = lDatos[iPosClave]
        if not Diccionario.esClave(dDiccionario, clave):
            dDiccionario[clave] = []
            dDiccionario[clave].append(lDatos)
        else:
            dDiccionario[clave].append(lDatos)
    return dDiccionario

def contarVotosRegion(dVotosRegion):
    dDiccionario = {}
    for clave in dVotosRegion:
        dDiccionario[clave] = []
        iTotalRegion=len(dVotosRegion[clave])
        iVotoBlanco=0
        iVotoPositivo=0
        for lVoto in dVotosRegion[clave]:
            iPosPartido=3
            if lVoto[iPosPartido] == "":
                iVotoBlanco+=1
            else:
                iVotoPositivo+=1
        fPorcentajePositivo=(iVotoPositivo*100)/iTotalRegion
        fPorcentajeBlanco=(iVotoBlanco*100)/iTotalRegion
        fPorcentajeTotal=100
        tTotales=(iVotoPositivo, fPorcentajePositivo, iVotoBlanco, fPorcentajeBlanco, iTotalRegion, fPorcentajeTotal)
        dDiccionario[clave].append(tTotales)
    return dDiccionario

def contarVotosPartido(dVotosRegion):
    dRegionPartido = {}
    for clave in dVotosRegion:
        dVotoPartido = {}
        iTotalRegion = 0
        #lVoto es en formato DNI,REGION,CARGO,PARTIDO
        for lVoto in dVotosRegion[clave]:
            #En posición 3 vienen los partidos políticos
            sClave = lVoto[3]
            iTotalRegion+=1
            if not Diccionario.esClave(dVotoPartido, sClave):
                dVotoPartido[sClave] = []
                #Hay un voto
                dVotoPartido[sClave].append(1)           
            else:
                #Se suma el voto
                dVotoPartido[sClave][0]+=1
        #Agregado del total y el porcentaje    
        for partido in dVotoPartido:
            iVotoPartido = dVotoPartido[partido][0]
            dVotoPartido[partido].append(iTotalRegion)
            iPorcentaje = (iVotoPartido * 100) / iTotalRegion
            dVotoPartido[partido].append(iPorcentaje)
        #Árbol: cada región tiene una rama de partidos
        dVotoPartido = ordenarPorIndex(dVotoPartido)
        dRegionPartido[clave] = dVotoPartido
    return dRegionPartido

def ordenarPorIndex(dDiccionario):
    #Lista de tuplas en formato clave, valor
    lLista = list(dDiccionario.items())
    #Ordena los items de manera descendente
    lLista.sort(key=lambda x:x[1][0], reverse=True)
    #Se transforma en diccionario
    dNuevo = dict(lLista)
    return dNuevo
    
def archivar(dRegionPartido, sCargo):
    sRuta = "boletas.txt"
    lPartidos = Archivo.leer(sRuta)
    dPartidos = Diccionario.generarDiccionario(lPartidos)

    sRuta = "regiones.txt"
    lRegiones = Archivo.leer(sRuta)
    dRegiones = Diccionario.generarDiccionario(lRegiones)
    
    dVotosTotales = {}
    for sCodRegion in dRegionPartido:
        for sPartido in dRegionPartido[sCodRegion]:
            lVotosRegion = []
            lCantVotos = dRegionPartido[sCodRegion][sPartido]
            sNomRegion = dRegiones.get(sCodRegion, [])[0].upper()
            sSinEspacio = sNomRegion.split()
            sNomRegion = "".join(sSinEspacio)
            lPartido = dPartidos.get(sPartido, "")
            if lPartido != "":
                sNumLista = lPartido[1].upper()
            else:
                sNumLista = ""
            
            sTotalObtenido = str(lCantVotos[0])
            sPorcentaje = "{:.2f}%".format(lCantVotos[2])
            sNombreArchivo = sNomRegion+ "_" + sCargo + ".csv"
            lVotosRegion.append(sCodRegion)
            lVotosRegion.append(sNumLista)
            lVotosRegion.append(sTotalObtenido)
            lVotosRegion.append(sPorcentaje)
            if not Diccionario.esClave(dVotosTotales, sNombreArchivo):
                dVotosTotales[sNombreArchivo] = []
                dVotosTotales[sNombreArchivo].append(lVotosRegion)
            else:
                dVotosTotales[sNombreArchivo].append(lVotosRegion)
    return dVotosTotales