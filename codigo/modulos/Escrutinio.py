from modulos import Diccionario
from modulos import Archivo
import random
    
def asignarVoto(dPadron, dRegiones):
    """Asigna un voto al azar para cada el padrón electoral"""
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
    """Genera una región al azar de acuerdo a las obtenidas en lRegionMemoria"""
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
    """Genera el padrón electoral de acuerdo a la cantidad deseada"""
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
        lVoto = []
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
    #Ordena los items de manera ascendente
    lLista.sort(key=lambda x:x[1][0], reverse=True)
    #Ordena los items de manera descendente
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

