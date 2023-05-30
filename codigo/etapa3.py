from modulos import Archivo
from modulos import Pantalla
from modulos import Diccionario
from modulos import Escrutinio

sEspeciales=" ¡!\"#$%‰&'()*+,-./0-9:;<<=>>?@A-Z[]^_`{}\\"




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
    while sOpcion=="" or sOpcion.isalpha() or not sOpcion.isdigit() or int(sOpcion)<=0 or int(sOpcion) > 4:
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
if sOpcion == "2":
    #Esta opcion es la opción 4 de votos posibles
    sOpcion = "4"
elif sOpcion == "4":
    #Esta opcion es la opción 2 de votos posibles
    sOpcion = "2"

sRuta = "archivo_votacion.csv"
lVotos = Archivo.leerVotos(sRuta, sOpcion)
sRuta = "boletas.txt"
lPartidos = Archivo.leer(sRuta)
dPartidos = Diccionario.generarDiccionario(lPartidos)

sRuta = "regiones.txt"
lRegiones = Archivo.leer(sRuta)
dRegiones = Diccionario.generarDiccionario(lRegiones)

dVotosRegiones=Escrutinio.generarVotoRegion(lVotos)
dVotosTotales=Escrutinio.contarVotosRegion(dVotosRegiones)
dRegionPartido = Escrutinio.contarVotosPartido(dVotosRegiones)
for sCodRegion in dRegionPartido:
    for sPartido in dRegionPartido[sCodRegion]:
        lCantVotos = dRegionPartido[sCodRegion][sPartido]
        sNomRegion = dRegiones.get(sCodRegion, [])[0]
        lPartido = dPartidos.get(sPartido, "")
        if lPartido != "":
            sNumLista = lPartido[1]
        else:
            sNumLista = ""
        print(sNomRegion, sCodRegion, sNumLista, lCantVotos[0], "{:.2f}%".format(lCantVotos[2]))

