#from modulos 
import Diccionario
#from modulos 
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
        fPorcentajeTotal=100.0
        tTotales=(iVotoPositivo, fPorcentajePositivo, iVotoBlanco, fPorcentajeBlanco, iTotalRegion, fPorcentajeTotal)
        dDiccionario[clave].append(tTotales)
    return dDiccionario

def contarVotosPartido(dVotosRegion):
    """Devuelve un árbol donde la clave es la región y el valor es un diccionario con los votos
    obtenidos por cada partido"""
    dRegionPartido = {}
    for clave in dVotosRegion:
        dVotoPartido = {}
        iTotalRegion = 0
        #lVoto es en formato DNI,REGION,CARGO,PARTIDO
        for lVoto in dVotosRegion[clave]:
            #En posición 3 vienen los partidos políticos
            sClave = lVoto[3]
            if sClave!="":
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
        dVotoPartido = Diccionario.ordenarDiccionarioMatriz(dVotoPartido)
        dRegionPartido[clave] = dVotoPartido
    return dRegionPartido

def obtenerPartido():
    """Devuelve un diccionario de los partidos con la abreviatura como clave"""
    sRuta = "boletas.txt"
    lPartidos = Archivo.leer(sRuta)
    dPartidos = Diccionario.generarDiccionario(lPartidos)
    return dPartidos

def obtenerRegion():
    """Devuelve un diccionario de las regones con código de región como clave"""
    sRuta = "regiones.txt"
    lRegiones = Archivo.leer(sRuta)
    dRegiones = Diccionario.generarDiccionario(lRegiones)
    return dRegiones

def archivar(dRegionPartido, sCargo):
    """Devuelve un diccionario con el nombre de la provincia como ruta de archivo
    y su valor contiene una lista con código región, número de lista, votos obtenidos y el porcentaje total"""
    dRegiones = obtenerRegion()
    dPartidos = obtenerPartido()
    
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

def obtenerSenadores(dRegionPartido):
    """Devuelve un diccionario con el escrutinio nacional por cada partido en el cargo senador"""
    iTotalVotos = 0
    dSenadores = {}
    for region in dRegionPartido:
        dVotosPartido = dRegionPartido[region]
        for partido in dVotosPartido:
            iTotalVotos += dVotosPartido[partido][0]
            if Diccionario.esClave(dSenadores, partido):
                #Posición 0 está la cantidad de voto por partido
                dSenadores[partido][0] += dVotosPartido[partido][0]
            else:
                #Se agrega lista con valor 0 en su primera posición
                dSenadores[partido] = [dVotosPartido[partido][0]]
            
    for partido in dSenadores:
        iVotos = dSenadores[partido][0]
        fPorcentaje = (iVotos * 100) / iTotalVotos
        dSenadores[partido].append(iTotalVotos)
        dSenadores[partido].append(fPorcentaje)
    
    dSenadores = Diccionario.ordenarDiccionarioMatriz(dSenadores)
    return dSenadores

def calcularTotalesSenadores(dSenadores):
    """Cálculo de votos totales positivos, en blanco y porcentajes de los senadores a nivel nacional"""
    iVotoPositivo=0
    fPorcentajePositivo=0
    lClaveBlanca=dSenadores.get("")
    if lClaveBlanca!=None:
        iVotoBlanco=lClaveBlanca[0]
        fPorcentajeBlanco=lClaveBlanca[2]
    sClave=list(dSenadores.partidos())[0]
    iTotalNacional=dSenadores[sClave][1]
    fPorcentajeTotal=100.0
    lPartido=[]
    for clave in dSenadores:
        if clave!="":
            iVotoPositivo+=dSenadores[clave][0]
            fPorcentajePositivo+=dSenadores[clave][2]
            lClave=[clave]
            lPartido.append(lClave + dSenadores[clave])
    tTotales=(iVotoPositivo, fPorcentajePositivo, iVotoBlanco, fPorcentajeBlanco, iTotalNacional, fPorcentajeTotal)
    lVotos = lPartido[0:2]
    lVotos.append(tTotales)
    return lVotos

def sistemaDhondt(dPartidos, iCantBancas):
    dBancas = {}
    
    dPartidosCopia=dPartidos.copy()
    lBancasTotales = list(dBancas.values())
    for partido in dPartidosCopia: 
        dBancas[partido]=0

    for partido in dPartidosCopia:
        dPartidosCopia[partido] = dPartidosCopia[partido][0]
    
    for iBanca in range (1,iCantBancas+1,1):
        lPartido = list(dPartidosCopia.keys())
        lVotosPartidos= list(dPartidosCopia.values())
        maxVotos = max(lVotosPartidos)
        sPartido = lPartido[lVotosPartidos.index(maxVotos)]
        
        if sPartido in dBancas:
            dBancas[sPartido]+=1
        else:
            dBancas[sPartido]=1
        
        dPartidosCopia[sPartido]=dPartidos[sPartido][0]/(iBanca+1)
        lBancasTotales = list(dBancas.values())

    return dBancas,dPartidosCopia
dPartido = {'POI': [9, 30, 30.0], 'LBD': [9, 30, 30.0], 'FDT': [5, 30, 16.666666666666668], 'PPP': [4, 30, 13.333333333333334], 'JXC': [3, 30, 10.0]}
dBancas = sistemaDhondt(dPartido, 6)
print(dBancas)