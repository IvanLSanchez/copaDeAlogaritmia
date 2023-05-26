import random
from modulos import Archivo

def generarNumeroAleatorio(iMin, iMax):
  """Devuelve un número entero al azar dentro de un intervalo entre iMin y iMax"""
  return random.randint(iMin, iMax)


def validarExistenciaClave(dDiccionario, iDato):
  bExiste = False
  lClaves = dDiccionario.keys() # line 35: validarExistenciaClave(dVotosRegion, iVotoRegion) -> dict_keys([])
  if iDato in lClaves:
    bExiste = True
  return bExiste


def generarVoto(iRegistros, dVotosRegion, lPartidos, lRegiones):
  dVotoPadron = {}
  for i in range(iRegistros):
    lVotoDNI = []
    iVotoDNI = generarNumeroAleatorio(1, 99999999)
    #Validación de la existencia del documento
    bEsInvalido = validarExistenciaClave(dVotoPadron, iVotoDNI)
    while bEsInvalido:
      iVotoDNI = generarNumeroAleatorio(1, 99999999)
      bEsInvalido = validarExistenciaClave(dVotoPadron, iVotoDNI)
    dVotoPadron[iVotoDNI] = []
    iPosicion = generarNumeroAleatorio(1, len(lRegiones))
    iVotoRegion = lRegiones[iPosicion]

    #{1:[345, 555], 4:[222]}
    #Validación existencia de la región
    if validarExistenciaClave(dVotosRegion, iVotoRegion):
      dVotosRegion[iVotoRegion].append(iVotoDNI)
    else:
      dVotosRegion[iVotoRegion] = []
      dVotosRegion[iVotoRegion].append(iVotoDNI)

    for j in range(4):
      iVota = generarNumeroAleatorio(0, 10)
      if iVota > 1:
        sVotoCargo = str(j)
        iPosicion = generarNumeroAleatorio(0, len(lPartidos))
        iVotoPartido = lPartidos[iPosicion]
      else:
        sVotoCargo = ""
        iVotoPartido = ""
      lVotoDNI.append(str(iVotoDNI))
      lVotoDNI.append(str(iVotoRegion))
      lVotoDNI.append(sVotoCargo)
      lVotoDNI.append(iVotoPartido)
      #[555, 1, 2, LBD]
      dVotoPadron[iVotoDNI].append(lVotoDNI)


# Guarda nombre de los archivos y genera listas
sArchBoletas = "boletas.txt"
sArchRegiones = "regiones.txt"

lPartidosMemoria = Archivo.leer(sArchBoletas)
lRegionMemoria = Archivo.leer(sArchRegiones)

dVotoRegion = {}
iRegistros = int(input("Ingrese cantidad de registros: ")) ## agregue int()
generarVoto(iRegistros, dVotoRegion, lPartidosMemoria, lRegionMemoria)