# Etapa 2
Se solicita desarrollar un programa para simular la emisión de los sufragios.

A partir de los archivos de datos que se obtuvieron en la ETAPA 1 de la COPA UADE DE ALGORITMIA 2023 (partidos políticos y regiones geográficas) se generará el archivo **archivo_votacion.csv** con N registros, donde cada uno represente un voto para un partido político en un cargo y región determinados. El valor de N se ingresa desde el teclado, verificando que sea un número natural. Tener en cuenta que este valor puede ser alto, pudiendo fácilmente superar los 200 millones de sufragios.

El formato de registro será el siguiente:

> **DNI ; Región ; Cargo ; Partido**

- **DNI:** Número de DNI del votante (valor entero positivo menor a 100000000)
- **Región:** Código de provincia, obtenido del archivo de regiones geográficas generado en la Etapa 1.
- **Cargo:** Código del cargo votado (1, 2, 3 o 4, según tabla más abajo).
- **Partido:** Abreviatura del partido político votado, obtenida del archivo de partidos políticos generado en la Etapa 1.

Cada persona puede elegir candidatos en una sola región geográfica, limitándose a un **único candidato** por cargo. Esto significa que el DNI puede aparecer varios registros, pero no puede emitir más de un voto para un mismo cargo o en provincias diferentes.

Los datos se obtendrán al azar, procurando introducir un sesgo en los mismos a efectos de evitar que la distribución uniforme de los números al azar genere empates técnicos en regiones o categorías. Se contemplará la posibilidad de que algún elector vote en blanco para algún cargo, lo que se manifestará como la ausencia del voto para cierta combinación de DNI, región y cargo. La cantidad de electores de cada región se deja a criterio del equipo de desarrollo.

Al finalizar la generación del archivo emitir un informe por pantalla con los totales de votos procesados para cada una de las regiones.

### Tabla de cargos a elegir:
Los cargos a elegir serán presidente y vicepresidente (código 1), diputado (2), senador (3), gobernador y vicegobernador (4).

### Criterios de aceptación:
- El material a entregar consistirá en el programa fuente escrito en Python. En esta oportunidad no se incluirá el archivo de datos debido a su volumen.
- El código debe modularizarse a través de funciones. Cada una debe resolver un subproblema completo, evitándose la realización de funciones elementales.
- La interfaz del programa deberá ser de línea de comandos.
- El uso de módulos debe reducirse al máximo, salvo los esenciales como random. 


[Inicio](../README.md)