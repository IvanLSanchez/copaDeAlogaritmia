# Importa Funciones
from modulos import Archivo
from modulos import Pantalla
from modulos import CargaPartidos
from modulos import CargaRegion

# Guarda nombre de los archivos y genera listas
sArchBoletas = "boletas.txt"
sArchRegiones = "regiones.txt"
lPartidosAct=[]

lPartidosMemoria = Archivo.leer(sArchBoletas)
lRegionMemoria = Archivo.leer(sArchRegiones)

# Pide datos de partidos
CargaPartidos.cargarPartidos(lPartidosAct,lPartidosMemoria)
#Ingreso de regiones
lRegionesAct = CargaRegion.ingresarRegion(lRegionMemoria)

# Guarda  
Archivo.guardar(sArchBoletas, lPartidosAct)
# Guarda regiones
Archivo.guardar(sArchRegiones, lRegionesAct)

# Muestra listados
lPartidosAct = Archivo.leer(sArchBoletas)
lRegionesAct = Archivo.leer(sArchRegiones)
print("\n\n")
Pantalla.visualizar(sArchBoletas, lPartidosAct)
print("\n\n")
Pantalla.visualizar(sArchRegiones, lRegionesAct)
