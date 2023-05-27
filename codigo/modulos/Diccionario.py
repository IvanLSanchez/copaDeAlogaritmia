def cambiarALista(dDiccionario):
  """Ingresa un diccionario y devuelve una lista de votos"""
  lVotos = []
  for clave in dDiccionario:
      lDatos = dDiccionario[clave]
      for linea in lDatos:
          lVotos.append(linea)
  return lVotos

def esClave(dDiccionario, clave):
  """Valida la existencia de la llave iDato dentro de dDiccionario"""
  bEsClave = False
  lClaves = list(dDiccionario.keys())
  if clave in lClaves:
    bEsClave = True
  return bEsClave

def validarValor(dDiccionario, valorClave, valor):
    bExiste = False
    #Por cada clave del diccionario
    for clave in dDiccionario:
        #Por cada elemento de la clave
        for elemento in dDiccionario[clave]:
            #Verificar si existe el valor en otra clave 
            if clave != valorClave and elemento == valor:
                bExiste = True
    return bExiste

def generarDiccionario(lLista, iPosClave=0, iPosValor=1):
    """Crea un diccionario a partir de una lista
    con clave con iPosClave y valor por defecto en iPosValor"""
    dDiccionario = {}
    for lDatos in lLista:
        clave = lDatos[iPosClave]
        if not esClave(dDiccionario, clave):
            dDiccionario[clave] = []
            dDiccionario[clave].append(lDatos[iPosValor])
        else:
            dDiccionario[clave].append(lDatos[iPosValor])
    return dDiccionario