def cambiarALista(dVotoPadron):
  """Ingresa un diccionario y devuelve una lista de votos"""
  lVotos = []
  for clave in dVotoPadron:
      lDatos = dVotoPadron[clave]
      for linea in lDatos:
          lVotos.append(linea)
  return lVotos

def esClave(dDiccionario, clave):
  """Valida la existencia de la llave iDato dentro de dDiccionario"""
  bEsClave = False
  lClaves = dDiccionario.keys()
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
    for elemento in lLista:
        lDatos = elemento.split(";")
        clave = lDatos[iPosClave]
        if not esClave(dDiccionario, clave):
            dDiccionario[clave] = []
            dDiccionario[clave].append(lDatos[iPosValor])
        else:
            dDiccionario[clave].append(lDatos[iPosValor])
    return dDiccionario

lista=["51353174;4;4;LBD",
"63812041;1;2;JXC",
"38418484;1;3;FDT",
"70019298;6;1;LBD",
"46663328;6;3;LBD"]
dDiccionario=generarDiccionario(lista,1,0)