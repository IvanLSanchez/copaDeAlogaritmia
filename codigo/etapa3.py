from modulos import Archivo
from modulos import Pantalla

sEspeciales=" ¡!\"#$%‰&'()*+,-./0-9:;<<=>>?@A-Z[]^_`{}\\"

sOpcion = Pantalla.menuEscrutinio()

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

print(f"Votos totales: ", len(lVotos))
