# archivo para el modelado del cuadro de salida de la etapa 3. No presenta relevancia en la funcionalidad del codigo principal
ICANTIDADCARACTERES = 90
ICANTIDADCARACTERESENTER = 100
def mostrarEscrutinio(cantPartidos):
    sColor1 = "\33[1;37;41m"
    sColor2 = "\33[1;30;47m"
    sColor3 = "\33[0;30;47m"
    sColor4 = "\33[1m"
    sColor5 = "\33[4m"
    sColor6 = "\33[0m"

    sEnter = sColor2.center(ICANTIDADCARACTERESENTER) + sColor6
    sSeparador = sColor3 + "_".center(ICANTIDADCARACTERES,"_")
    
    print(sColor1 + "<REGION>".center(ICANTIDADCARACTERES) + sColor6)

    print(sColor2 + "ELECCIONES GENERALES 2023".center(ICANTIDADCARACTERES) + sColor6)
    print(sColor2 + "Categoria: <CARGO>".center(ICANTIDADCARACTERES))

    print(sEnter)

    print(sColor2 + "Electores habilitados: <CANTIDAD_DE_ELECTORES_EN_LA_REGION>".center(ICANTIDADCARACTERES) + sColor6)
    print(sColor2 + "Porcentaje de votantes: <PORCENTAJE>".center(ICANTIDADCARACTERES) + sColor6)

    print(sSeparador)
    print(sEnter)

    print(sColor2 + "{:^20} {:^27} {:^20} {:^20}".format("N° LISTA", "PARTIDO POLITICO", "VOTO", "%") + sColor6)
    print(sSeparador)

    for i in range (cantPartidos):
        print(sEnter)
        print(sColor2 + "{:^20} {:^27} {:^20} {:^20}".format(f"<NRO_LISTA_{i+1}>", f"PARTIDO_{i+1}:", "<CANT_VOTOS>", "<PORCENTAJE>") + sColor6)
        print(sColor2 + "{:^20} {:^27} {:^20} {:^20}".format("", "<CANDIDATOS>", "", "") + sColor6)
        print(sSeparador)
    
    print(sColor3 + "{:>48} {}|{:^21}|{:^21}|".format(sColor4 + "VOTOS POSITIVOS:", sColor5,"<CANT_VOTOS>", "<PORCENTAJE>" ) + sColor6)
    print(sColor3 + "{:>48} {}|{:^21}|{:^21}|".format(sColor4 + "VOTOS EN BLANCO:", sColor5,"<CANT_VOTOS>", "<PORCENTAJE>" ) + sColor6)
    print(sColor3 + "{:>48} {}|{:^21}|{:^21}|".format(sColor4 + "TOTAL:", sColor5,"<CANT_VOTOS>", "<PORCENTAJE>" ) + sColor6)


mostrarEscrutinio(3)