import random
from modulos import Archivo

def validarExistenciaClave(dDiccionario, iDato):
  """Valida la existencia de la llave iDato dentro de dDiccionario"""
  bExiste = False
  lClaves = dDiccionario.keys()
  if iDato in lClaves:
    bExiste = True
  return bExiste


def generarVoto(iRegistros, dVotosRegion, lPartidos, lRegiones):
  """Genera votos aleatorios para el padrón electoral"""
  dVotoPadron = {}
  for i in range(iRegistros):
    iVotoDNI = random.randint(1, 99999999)
    #Validación de la existencia del documento
    bEsInvalido = validarExistenciaClave(dVotoPadron, iVotoDNI)
    while bEsInvalido:
      iVotoDNI = random.randint(1, 99999999)
      bEsInvalido = validarExistenciaClave(dVotoPadron, iVotoDNI)
    dVotoPadron[iVotoDNI] = []
    iPosicion = random.randint(0, len(lRegiones)-1)
    iVotoRegion = lRegiones[iPosicion][1]

  #{1:[345, 555], 4:[222]}
  #Validación existencia de la región
    if validarExistenciaClave(dVotosRegion, iVotoRegion):
      dVotosRegion[iVotoRegion].append(iVotoDNI)
    else:
      dVotosRegion[iVotoRegion] = []
      dVotosRegion[iVotoRegion].append(iVotoDNI)

    for j in range(4):
      lVotoDNI = []
      iVota = random.randint(0, 10)
      sVotoCargo = str(j+1)
      if iVota > 1:
        iPosicion = random.randint(0, len(lPartidos)-1)
        iVotoPartido = lPartidos[iPosicion][1]
      else:
        iVotoPartido = ""
      lVotoDNI.append(str(iVotoDNI))
      lVotoDNI.append(str(iVotoRegion))
      lVotoDNI.append(sVotoCargo)
      lVotoDNI.append(iVotoPartido)
      #[555, 1, 2, LBD]
      dVotoPadron[iVotoDNI].append(lVotoDNI)
  return dVotoPadron

def formatearVotos(dVotoPadron):
  """Devuelve una lista de votos"""
  lVotos = []
  for clave in dVotoPadron:
      lDatos = dVotoPadron[clave]
      for linea in lDatos:
          lVotos.append(linea)
  return lVotos        
    

# Guarda nombre de los archivos y genera listas
sArchBoletas = "boletas.txt"
sArchRegiones = "regiones.txt"

lPartidosMemoria = Archivo.leer(sArchBoletas)
lRegionMemoria = Archivo.leer(sArchRegiones)

dVotoRegion = {}
iRegistros = int(input("Ingrese cantidad de registros: "))

#Obtención de votos por padrón
dVotoPadron = generarVoto(iRegistros, dVotoRegion, lPartidosMemoria, lRegionMemoria)
lVotos = formatearVotos(dVotoPadron)

#Guardado de los votos del padrón
sRuta = "archivo_votacion.csv"
Archivo.guardar(sRuta, lVotos)