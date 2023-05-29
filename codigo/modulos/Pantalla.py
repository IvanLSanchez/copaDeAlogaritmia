ICANTIDADCARACTERES=70

def imprimirPartidos(lArchivo, sListadoSeparador):
    """Muestra en pantalla los partidos políticos de la lista lArchivo"""
    sListadoTitulo = "PARTIDOS POLITICOS".center(ICANTIDADCARACTERES)
    print(f"{sListadoTitulo}")
    print(f"{sListadoSeparador}\n")
    print("{:^30} {:^15} {:^15}".format('NOMBRE','ABREVIATURA','LISTA'))
    print(f"{sListadoSeparador}\n")
    for lLinea in lArchivo:
        print("{:^30} {:^15} {:^15}".format(lLinea[0].capitalize(),lLinea[1].upper(),lLinea[2].capitalize()))
        print(f"{sListadoSeparador}\n")
        
def imprimirRegiones(lArchivo, sListadoSeparador):
    """Muestra en pantalla las regiones de la lista lArchivo"""
    sListadoTitulo = "REGIONES GEOGRAFICAS".center(ICANTIDADCARACTERES)
    print(f"{sListadoTitulo}")
    print(f"{sListadoSeparador}\n")
    print("{:^30} {:^30}".format('NOMBRE','CODIGO O ABREVIATURA'))
    print(f"{sListadoSeparador}\n")
    for lLinea in lArchivo:
        print("{:^30} {:^30}".format(lLinea[0].capitalize(),lLinea[1].capitalize()))
        print(f"{sListadoSeparador}\n")
            
def visualizar(sRuta, lArchivo):
    """De acuerdo a sRuta, define la impresión de la lista
    lArchivo para Partidos Políticos o Regiones"""
    sNombre = sRuta.split(".")[0]
    sListadoSeparador = "_".center(ICANTIDADCARACTERES,'_')
    print(f"{sListadoSeparador}\n")
    if sNombre == "boletas":
        imprimirPartidos(lArchivo, sListadoSeparador)
    else:
        imprimirRegiones(lArchivo, sListadoSeparador)  
# 1) genera base del listado
# 2) abre el archivo
# 3) segun el archivo genera los campos de la tabla
# 4) devuelve listados por pantalla
# https://parzibyte.me/blog/2020/11/09/leer-archivo-csv-python/
# https://www.delftstack.com/es/howto/python/data-in-table-format-python/
# https://www.w3schools.com/python/ref_string_format.asp

def mostrarVotos(lRegiones, dArchivo):
    """Visualización del recuento de voto en relación a los electores por provincia"""
    sListadoSeparador = "_".center(ICANTIDADCARACTERES,'_')
    print(f"{sListadoSeparador}\n")
    sListadoTitulo = f"RESULTADOS".center(ICANTIDADCARACTERES)
    print(f"{sListadoTitulo}")
    print(f"{sListadoSeparador}\n")
    print("{:^30} {:^15} {:^15}".format('REGION','% DE VOTOS','CANTIDAD'))
    print(f"{sListadoSeparador}\n")

    iCantVotosTotales = 0
    for clave in dArchivo:
        iCantVotosTotales += len(dArchivo[clave])
    
    lVotoRegion = list(dArchivo.keys())
    lVotoRegion.sort()
    
    for sVotoRegion in lVotoRegion:
        for lDatos in lRegiones:
            if lDatos[1] == sVotoRegion:
                sRegion = lDatos[0]
        iVotosPartido = len(dArchivo[sVotoRegion])
        fPorcentaje = ((iVotosPartido*100)/iCantVotosTotales)
        print("{:^30} %{:^15.2f} {:^15}".format(sRegion.upper(), fPorcentaje, iVotosPartido))
        print(f"{sListadoSeparador}\n")
