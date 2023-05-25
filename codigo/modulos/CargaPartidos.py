def sacarTilde(sCadena):
  """Reemplaza las vocales con tilde en sCadena por sus equivalentes sin tilde"""
  sContilde = "áéíóúÁÉÍÓÚ"
  sSintilde = "aeiouAEIOU"
  sNueva = ""
  for sCaracter in sCadena:
    if sCaracter in sContilde:
      iPosicion = sContilde.index(sCaracter)
      sNueva = sNueva + sSintilde[iPosicion]
    else:
      sNueva = sNueva + sCaracter
  return sNueva

def buscarRepetidosPartidos(iPosicion, sValor, lPartidosMemoria, lPartidosGuardados):
  """busca en las listas actuales concidencias de datos string"""
  bExiste = False
  for i in range(len(lPartidosMemoria)):
    if lPartidosMemoria[i][iPosicion].upper() == sValor:
      bExiste = True
  for i in range(len(lPartidosGuardados)):
    if lPartidosGuardados[i][iPosicion].upper() == sValor:
      bExiste = True
  return bExiste

def buscarListasRepetidosPartidos(iPosicion, sValor, lPartidosMemoria, lPartidosGuardados):
  """busca en las listas actuales concidencias de datos numericos"""
  bExiste = False
  for i in range(len(lPartidosMemoria)):
    if lPartidosMemoria[i][iPosicion] == sValor:
      bExiste = True
  for i in range(len(lPartidosGuardados)):
    if lPartidosGuardados[i][iPosicion] == sValor:
      bExiste = True
  return bExiste


def validarnombrePartido(lPartidosMemoria, lPartidosGuardados):
  """Ingresa y valida nombres de partidos"""
  sNombrePartido = input("Ingrese nombre del partido: ")
  sNombrePartido = sacarTilde(sNombrePartido)
  while (sNombrePartido.upper() != "FIN") and (sNombrePartido == "" or buscarRepetidosPartidos(0, sNombrePartido.upper(), lPartidosMemoria, lPartidosGuardados)):
    print("\nNombre inválido o repetido, ingrese otro.")
    sNombrePartido = input("Ingrese nombre del partido: ")
    sNombrePartido = sacarTilde(sNombrePartido)
  return sNombrePartido


def validarListaPartido(lPartidosMemoria, lPartidosGuardados):
  sLista = input("\nIngrese número de lista del partido: ")
  bEsValido = sLista.isdigit(
  )  #si es 1223 viene True, "" viene False , si es letra o alphanumber es False
  while not (bEsValido) or sLista == '0' or buscarListasRepetidosPartidos(
      2, sLista, lPartidosMemoria, lPartidosGuardados):
    print("\nNúmero de lista inválido o repetido, ingrese otro.")
    sLista = input("\nIngrese número de lista del partido: ")
    bEsValido = sLista.isdigit()
  return sLista


def validarAbreviaturaPartido(lPartidosMemoria, lPartidosGuardados):
  """Ingresa y valida abreviaturas"""
  sAbreviatura = input("\nIngrese abreviatura del partido: ")
  sAbreviatura = sacarTilde(sAbreviatura)
  while (sAbreviatura == "" or buscarRepetidosPartidos(
      1, sAbreviatura.upper(), lPartidosMemoria, lPartidosGuardados)):
    print("\nAbreviatura invalida o repetida, ingrese otra.")
    sAbreviatura = input("\nIngrese abreviatura del partido: ")
    sAbreviatura = sacarTilde(sAbreviatura)
  return sAbreviatura


def cargarPartidos(lPartidosMemoria, lPartidosGuardados):
  """carga los datos a la listas"""
  sNombrePartido = validarnombrePartido(lPartidosMemoria, lPartidosGuardados)

  while sNombrePartido.upper() != "FIN":
    lDatos = []
    lDatos.append(sNombrePartido)

    sAbreviaturaPartido = validarAbreviaturaPartido(lPartidosMemoria,
                                                    lPartidosGuardados)
    lDatos.append(sAbreviaturaPartido)
    sNListaPartido = validarListaPartido(lPartidosMemoria, lPartidosGuardados)
    lDatos.append(str(sNListaPartido))

    lPartidosMemoria.append(lDatos)

    print("\n\n")
    sNombrePartido = validarnombrePartido(lPartidosMemoria, lPartidosGuardados)
