# archivo para el modelado del cuadro de salida de la etapa 3. No presenta relevancia en la funcionalidad del codigo principal
ICANTIDADCARACTERES = 90
ICANTIDADCARACTERESENTER = 100
def mostrarEscrutinio(cantPartidos):
    sColor1 = "\33[1;37;41m" #Fondo Rojo con letra blanca negrita
    sColor2 = "\33[1;30;47m" #Fondo Blanco con letra 
    sColor3 = "\33[0;30;47m" #Fondo Blanco con letra normal
    sColor4 = "\33[1m" #Negrita
    sColor5 = "\33[4m" #Subrayado
    sColor6 = "\33[0;m" #Color Base

    sEnter = sColor3 + " ".center(ICANTIDADCARACTERES," ") + sColor6
    sSeparador = sColor3 + "_".center(ICANTIDADCARACTERES,"_") + sColor6
    
    print(sColor1 + "<REGION>".center(ICANTIDADCARACTERES) + sColor6)

    print(sColor2 + "ELECCIONES GENERALES 2023".center(ICANTIDADCARACTERES) + sColor6)
    print(sColor2 + "Categoria: <CARGO>".center(ICANTIDADCARACTERES) + sColor6)
    
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



def dhont(nSeats,votes,verbose=False):
    """
    nSeats is the number of seats
    votes is a dictionary with the key:value {'party':votes}
    verbose is an option to print designation info
    """
    t_votes=votes.copy()
    seats={}
    for key in votes: seats[key]=0
    while sum(seats.values()) < nSeats:
        max_v= max(t_votes.values())
        next_seat=list(t_votes.keys())[list(t_votes.values()).index(max_v)]
        if next_seat in seats:
            seats[next_seat]+=1
        else:
            seats[next_seat]=1

        if verbose:
            print("{} Escaño: {}".format(sum(seats.values()),next_seat))
            for key in t_votes:
                print("\t{} [{}]: {:.1f}".format(key,seats[key],t_votes[key]))
            print("\b")
        t_votes[next_seat]=votes[next_seat]/(seats[next_seat]+1)
    return seats



nSeats = 8
votes = {'a':168,'b':104,'c':72,'d':64,'e':40}
seats=dhont(nSeats,votes,verbose=True)
"""1 Escaño: a
    a [1]: 168.0
    b [0]: 104.0
    c [0]: 72.0
    d [0]: 64.0
    e [0]: 40.0"""
"""
2 Escaño: b
    a [1]: 84.0
    b [1]: 104.0
    c [0]: 72.0
    d [0]: 64.0
    e [0]: 40.0

3 Escaño: a
    a [2]: 84.0
    b [1]: 52.0
    c [0]: 72.0
    d [0]: 64.0
    e [0]: 40.0

4 Escaño: c
    a [2]: 56.0
    b [1]: 52.0
    c [1]: 72.0
    d [0]: 64.0
    e [0]: 40.0

5 Escaño: d
    a [2]: 56.0
    b [1]: 52.0
    c [1]: 36.0
    d [1]: 64.0
    e [0]: 40.0

6 Escaño: a
    a [3]: 56.0
    b [1]: 52.0
    c [1]: 36.0
    d [1]: 32.0
    e [0]: 40.0

7 Escaño: b
    a [3]: 42.0
    b [2]: 52.0
    c [1]: 36.0
    d [1]: 32.0
    e [0]: 40.0

8 Escaño: a
    a [4]: 42.0
    b [2]: 34.7
    c [1]: 36.0
    d [1]: 32.0
    e [0]: 40.0
"""
{'a': 4, 'b': 2, 'c': 1, 'd': 1, 'e': 0}