def sacarEspacio(sCadena):
  """Divide sCadena en una lista de cadenas y devuelve un string con los elementos de la lista de cadenas separados"""
  lPalabras = sCadena.split()
  return "".join(lPalabras)


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


def compararRegion(lRegion, sCadena):
  """Compara si sCadena ya existe en la lista lRegion"""
  bExiste = False
  for lLinea in lRegion:
    sRegionArchivo = sacarEspacio(lLinea[0])
    sRegionArchivo = sacarTilde(sRegionArchivo)
    if sRegionArchivo.upper() == sCadena.upper():
      bExiste = True
  return bExiste


def ingresarRegion(lRegionMemoria):
  """El usuario ingresa regiones y las agrega a una nueva lista lNuevasRegiones"""
  bExiste = False
  bPedirDato = True
  lNuevasRegiones = []

  while bPedirDato:
    lDatos = []
    sRegion = input(
      "Ingrese una región geográfica ('FIN' para finalizar carga de datos): ")
    sNueva = sacarEspacio(sRegion)
    bEsCadena = sNueva.isalpha()
    sNueva = sacarTilde(sNueva)
    bExiste = compararRegion(lRegionMemoria, sNueva)
    if not bExiste:
      bExiste = compararRegion(lNuevasRegiones, sNueva)

    while (not bEsCadena or bExiste) and sNueva.upper() != "FIN":
      if not bEsCadena:
        print("Región geográfica INVALIDA.")
        sRegion = input(
          "Ingrese nuevamente una región geográfica ('FIN' para finalizar): ")
      elif bExiste:
        print("La región geográfica ingresada YA EXISTE EN EL REGISTRO.")
        sRegion = input(
          "Ingrese nuevamente una región geográfica ('FIN' para finalizar): ")
      sNueva = sacarEspacio(sRegion)
      bEsCadena = sNueva.isalpha()
      sNueva = sacarTilde(sNueva)
      bExiste = compararRegion(lRegionMemoria, sNueva)
      if not bExiste:
        bExiste = compararRegion(lNuevasRegiones, sNueva)

    if sNueva.upper() != "FIN":
      lDatos.append(sRegion)
      lNuevasRegiones.append(lDatos)
    else:
      bPedirDato = False

  if len(lNuevasRegiones) > 0:
    asignarCodigoNumerico(lRegionMemoria, lNuevasRegiones)
  return lNuevasRegiones


def asignarCodigoNumerico(lRegionMemoria, lNuevasRegiones):
  """Asigna un código númerico a la lista lNuevasRegiones"""
  iInicio = 0
  for lMemoria in lRegionMemoria:
    iInicio += 1
  iInicio += 1
  for lActual in lNuevasRegiones:
    lActual.append(str(iInicio))
    iInicio += 1
  return lNuevasRegiones

