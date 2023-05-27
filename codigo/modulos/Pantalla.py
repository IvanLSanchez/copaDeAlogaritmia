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

def visualizarSimulacion(lRegiones, dArchivo):
    sListadoSeparador = "_".center(ICANTIDADCARACTERES,'_')
    print(f"{sListadoSeparador}\n")
    sListadoTitulo = f"RESULTADOS".center(ICANTIDADCARACTERES)
    print(f"{sListadoTitulo}")
    print(f"{sListadoSeparador}\n")
    print("{:^30} {:^15} {:^15}".format('REGION','% DE VOTOS','CANTIDAD'))
    print(f"{sListadoSeparador}\n")

    iCantVotosTotales = 0
    for i in dArchivo:
        iCantVotosTotales += len(dArchivo[i])
    
    lRegionesQueVotaron = list(dArchivo.keys()).sort()

    for region in lRegionesQueVotaron:
        iPos = lRegiones.index(region)
        sRegion = lRegiones[iPos][0]
        iVotosPartido = len(dArchivo[region])
        print("{:^30} %{:^15} {:^15}".format(sRegion.upper(),((iVotosPartido*100)/iCantVotosTotales),iVotosPartido))
        print(f"{sListadoSeparador}\n")


    """for i in range (int(lRegiones[-1][-1])):
        for j in range (1,5,1):
            dVotosEmitidos = {}
            iCantVotosTotales = 0

            for k in lArchivo:
                if int(k[1]) == int(lRegiones[i][-1]) and int(k[2]) == j and k[3]!="":
                    if dVotosEmitidos.get(k[3]):
                        dVotosEmitidos[k[3]] += 1
                    else:
                        dVotosEmitidos[k[3]] = 1
                    iCantVotosTotales += 1

            if len(dVotosEmitidos) > 0:
                sListadoSeparador = "_".center(ICANTIDADCARACTERES,'_')
                print(f"{sListadoSeparador}\n")

                if j == 1:
                    sCargoVotado = "PRESIDENTE Y VICEPRESIDENTE"
                elif j == 2:
                    sCargoVotado = "DIPUTADOS"
                elif j == 3:
                    sCargoVotado = "SENADOR"
                else:
                    sCargoVotado = "GOBERNADOR Y VICEGOBERNADOR"
                
                sListadoTitulo = f"RESULTADOS ({lRegiones[i][0].upper()}) - {sCargoVotado}".center(ICANTIDADCARACTERES)
                print(f"{sListadoTitulo}")
                print(f"{sListadoSeparador}\n")
                print("{:^35} {:^35}".format('PARTIDO','% DE VOTOS'))
                print(f"{sListadoSeparador}\n")

                for clave in dVotosEmitidos:
                    iVotosPartido = dVotosEmitidos.get(clave)
                    print("{:^35} %{:^35}".format(clave.upper(),((iVotosPartido*100)/iCantVotosTotales)))
                    print(f"{sListadoSeparador}\n")"""