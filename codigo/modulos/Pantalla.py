from modulos import Escrutinio

ICANTIDADCARACTERES=70
ICANTIDADCARACTERESENTER = 100

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

def menuEscrutinio():
    #MENÚ
    #VISUALIZAR:
    #1-Consulta de resultados Presidente y vicepresidente
    #2-Consulta de resultados Gobernador y Vicegobernador
    #3-Consulta de resultados Senadores
    #4-Consulta de resultados Diputados
    sTitulo = "ARGENTINA VOTA - 40 AÑOS DE DEMOCRACIA".center(77,' ')
            
    sListadoSeparador = "_".center(77,'_')
    print(f"{sListadoSeparador}\n")
    print(f"{sTitulo}")
    print(f"{sListadoSeparador}\n")

    sBienvenida = "Bienvenido al Portal de Resultados de las Elecciones Generales 2023".center(77, ' ')
    print(f"{sBienvenida}")
    print(f"{sListadoSeparador}\n")

    print("A continuación se presentan las opciones para visualización del escrutinio: ")

    print(f"{sListadoSeparador}\n")
    print("1-Consulta de resultados Presidente y vicepresidente")
    print("2-Consulta de resultados Gobernador y Vicegobernador")
    print("3-Consulta de resultados Senadores")
    print("4-Consulta de resultados Diputados")
    print(f"{sListadoSeparador}\n")

    sIngreso = "Ingrese el número de la opción elegida y luego presione 'Enter': "
    print(f"{sListadoSeparador}\n")

    try:
        sOpcion=input(sIngreso)
        while sOpcion=="" or sOpcion.isalpha() or not sOpcion.isdigit() or int(sOpcion) > 4:
            print("Valor NO válido\n")
            sOpcion=input(sIngreso)
    except ValueError:
            print("Valor NO válido\n")
            sOpcion=input(sIngreso)
    print()
    #VOTOS POSIBLES:
    #1-Presidente y vicepresidente
    #2-Diputados
    #3-Senadores
    #4-Consulta de resultados Gobernador y Vicegobernador
    if sOpcion == "1":
        sCargo = "PRESIDENTE"
    elif sOpcion == "2":
        #Esta opcion es la opción 4 de votos posibles
        sOpcion = "4"
        sCargo = "GOBERNADOR"
    elif sOpcion == "3":
        sCargo = "SENADORES"
    elif sOpcion == "4":
        #Esta opcion es la opción 2 de votos posibles
        sOpcion = "2"
        sCargo = "DIPUTADOS"

    lOpcion = [sOpcion, sCargo]
    
    return lOpcion

# archivo para el modelado del cuadro de salida de la etapa 3. No presenta relevancia en la funcionalidad del codigo principal
ICANTIDADCARACTERES = 90
ICANTIDADCARACTERESENTER = 100

def mostrarSenadores(dSenadores, dVotosTotales):
    
    dRegiones, dPartidos = Escrutinio.obtenerRegionesPartidos()

    sNomRegion="nacional".upper()
    iVotoPositivo="XXX"
    fPorcentajePositivo="XXX"
    iVotoBlanco="XXX"
    fPorcentajeBlanco="XXX"
    iTotalRegion="XXX"
    fPorcentajeTotal="XXX"
    # iVotoPositivo=dVotosTotales[clave][0][0]
    # fPorcentajePositivo=dVotosTotales[clave][0][1]
    # iVotoBlanco=dVotosTotales[clave][0][2]
    # fPorcentajeBlanco=dVotosTotales[clave][0][3]
    # iTotalRegion=dVotosTotales[clave][0][4]
    # fPorcentajeTotal=dVotosTotales[clave][0][5]

    sColor1 = "\33[1;37;41m"
    sColor2 = "\33[1;30;47m"
    sColor3 = "\33[0;30;47m"
    sColor4 = "\33[1m"
    sColor5 = "\33[4m"
    sColor6 = "\33[0m"

    sEnter = sColor3 + " ".center(ICANTIDADCARACTERES," ") + sColor6
    sSeparador = sColor3 + "_".center(ICANTIDADCARACTERES,"_") + sColor6

    print(sColor1 + sNomRegion.center(ICANTIDADCARACTERES) + sColor6)

    print(sColor2 + "ELECCIONES GENERALES 2023".center(ICANTIDADCARACTERES) + sColor6)
    print(sColor2 + ("Categoria: Senadores").center(ICANTIDADCARACTERES) + sColor6)

    print(sEnter)

    print(sColor2 + ("Electores habilitados: {}".format(iTotalRegion)).center(ICANTIDADCARACTERES) + sColor6)
    print(sColor2 + ("Porcentaje de votantes: {}".format(fPorcentajeTotal)).center(ICANTIDADCARACTERES) + sColor6)

    print(sSeparador)
    print(sEnter)

    print(sColor2 + "{:^20} {:^27} {:^20} {:^20}".format("Nº LISTA", "PARTIDO POLÍTICO", "VOTO", "%") + sColor6)
    print(sSeparador)

    for partido in dSenadores:
        if partido!="":
            sNomPartido = partido + ":"
            sNroLista = dPartidos[partido][1]
            iTotalPartido=dSenadores[partido][0]
            fPorcentajePartido=dSenadores[partido][2]
            print(sEnter)
            print(sColor2 + "{:^20} {:^27} {:^20} {:^20.2f}".format(sNroLista, sNomPartido, iTotalPartido, fPorcentajePartido) + sColor6)
            if sNroLista!="":
                print(sColor2 + "{:^20} {:^27} {:^20} {:^20}".format("", "<CANDIDATOS>", "", "") + sColor6)                
            print(sSeparador)
    
    print(sColor3 + "{:>48} {}|{:^21}|{:^21}|".format(sColor4 + "VOTOS POSITIVOS:", sColor5, iVotoPositivo, fPorcentajePositivo) + sColor6)
    print(sColor3 + "{:>48} {}|{:^21}|{:^21}|".format(sColor4 + "VOTOS EN BLANCO:", sColor5, iVotoBlanco, fPorcentajeBlanco) + sColor6)
    print(sColor3 + "{:>48} {}|{:^21}|{:^21}|".format(sColor4 + "TOTAL:", sColor5, iTotalRegion, fPorcentajeTotal) + sColor6)
    print()

def mostrarEscrutinio(dRegionPartido, dVotosTotales, sCargo):
    
    dRegiones, dPartidos = Escrutinio.obtenerRegionesPartidos()
    
    for clave in dRegionPartido:
        sNomRegion=dRegiones[clave][0].upper()
        iVotoPositivo=dVotosTotales[clave][0][0]
        fPorcentajePositivo=dVotosTotales[clave][0][1]
        iVotoBlanco=dVotosTotales[clave][0][2]
        fPorcentajeBlanco=dVotosTotales[clave][0][3]
        iTotalRegion=dVotosTotales[clave][0][4]
        fPorcentajeTotal=dVotosTotales[clave][0][5]
        sColor1 = "\33[1;37;41m"
        sColor2 = "\33[1;30;47m"
        sColor3 = "\33[0;30;47m"
        sColor4 = "\33[1m"
        sColor5 = "\33[4m"
        sColor6 = "\33[0m"

        sEnter = sColor3 + " ".center(ICANTIDADCARACTERES," ") + sColor6
        sSeparador = sColor3 + "_".center(ICANTIDADCARACTERES,"_") + sColor6
    
        print(sColor1 + sNomRegion.center(ICANTIDADCARACTERES) + sColor6)

        print(sColor2 + "ELECCIONES GENERALES 2023".center(ICANTIDADCARACTERES) + sColor6)
        print(sColor2 + ("Categoria: " + sCargo ).center(ICANTIDADCARACTERES) + sColor6)

        print(sEnter)

        print(sColor2 + ("Electores habilitados: {}".format(iTotalRegion)).center(ICANTIDADCARACTERES) + sColor6)
        print(sColor2 + ("Porcentaje de votantes: {}".format(fPorcentajeTotal)).center(ICANTIDADCARACTERES) + sColor6)

        print(sSeparador)
        print(sEnter)

        print(sColor2 + "{:^20} {:^27} {:^20} {:^20}".format("Nº LISTA", "PARTIDO POLÍTICO", "VOTO", "%") + sColor6)
        print(sSeparador)

        for partido in dRegionPartido[clave]:
            if partido!="":
                sNomPartido = partido + ":"
                sNroLista = dPartidos[partido][1]
                iTotalPartido=dRegionPartido[clave][partido][0]
                fPorcentajePartido=dRegionPartido[clave][partido][2]
                print(sEnter)
                print(sColor2 + "{:^20} {:^27} {:^20} {:^20.2f}".format(sNroLista, sNomPartido, iTotalPartido, fPorcentajePartido) + sColor6)
                if sNroLista!="":
                    print(sColor2 + "{:^20} {:^27} {:^20} {:^20}".format("", "<CANDIDATOS>", "", "") + sColor6)                
                print(sSeparador)
        
        print(sColor3 + "{:>48} {}|{:^21}|{:^21.2f}|".format(sColor4 + "VOTOS POSITIVOS:", sColor5, iVotoPositivo, fPorcentajePositivo) + sColor6)
        print(sColor3 + "{:>48} {}|{:^21}|{:^21.2f}|".format(sColor4 + "VOTOS EN BLANCO:", sColor5, iVotoBlanco, fPorcentajeBlanco) + sColor6)
        print(sColor3 + "{:>48} {}|{:^21}|{:^21.2f}|".format(sColor4 + "TOTAL:", sColor5, iTotalRegion, fPorcentajeTotal) + sColor6)
        print()