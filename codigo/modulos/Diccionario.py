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
    """Verificación de la existencia del valor en dDiccionario"""
    bExiste = False
    #Por cada clave del diccionario
    for clave in dDiccionario:
        #Por cada elemento de la clave
        for elemento in dDiccionario[clave]:
            #Verificar si existe el valor en otra clave 
            if clave != valorClave and elemento == valor:
                bExiste = True
    return bExiste

def generarDiccionario(lLista):
    """Crea un diccionario a partir de una lista
    con clave con iPosClave y valor por defecto en iPosValor"""
    dDiccionario = {}
    iPosClave = 1
    iPosValor1 = 0
    iPosValor2 = 2
    
    for lDatos in lLista:
        iLongitud = len(lDatos)
        clave = lDatos[iPosClave]
        dDiccionario[clave] = []
        dDiccionario[clave].append(lDatos[iPosValor1])
        if iLongitud > 2:
            dDiccionario[clave].append(lDatos[iPosValor2])
    return dDiccionario

def generarDicCodLista(lLista):
    """Crea un diccionario a partir de una lista
    con clave con iPosClave y valor por defecto en iPosValor"""
    dDiccionario = {}
    iPosClave = 2
    iPosValor1 = 1
    
    for lDatos in lLista:
        iLongitud = len(lDatos)
        clave = lDatos[iPosClave]
        dDiccionario[clave] = []
        dDiccionario[clave].append(lDatos[iPosValor1])
    return dDiccionario

def ordenarDiccionario(dDiccionario):
    """Ordena diccionarios con matrices internas,
    tomando la posición 1 de las filas y su contenido de posición 0 como referencia de ordenamiento"""
    #Lista de tuplas en formato clave, valor
    #[(<clave1>, [<v1.1>, <v1.2>, etc]), (<clave2>, [<v2.1>, <v2.2>, etc])]
    lLista = list(dDiccionario.items())
    #Ordena los items de manera descendente
    lLista.sort(key=lambda x:x[1], reverse=True)
    #Se transforma en diccionario
    dNuevo = dict(lLista)
    return dNuevo


def ordenarDiccionarioMatriz(dDiccionario):
    """Ordena diccionarios con matrices internas,
    tomando la posición 1 de las filas y su contenido de posición 0 como referencia de ordenamiento"""
    #Lista de tuplas en formato clave, valor
    #[(<clave1>, [<v1.1>, <v1.2>, etc]), (<clave2>, [<v2.1>, <v2.2>, etc])]
    lLista = list(dDiccionario.items())
    #Ordena los items de manera descendente
    lLista.sort(key=lambda x:x[1][0], reverse=True)
    #Se transforma en diccionario
    dNuevo = dict(lLista)
    return dNuevo
