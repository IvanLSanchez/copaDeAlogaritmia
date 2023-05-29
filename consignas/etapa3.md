# Etapa 3
Se solicita desarrollar un programa para realizar el escrutinio de los sufragios.

A partir de los archivos generados en la ETAPA 1 y 2, realizar un programa en Python que gestione el escrutinio de todos los votos emitidos para ambos poderes:

### Poder Ejecutivo:
- Presidente y vicepresidente
- Gobernadores y Jefe de Gobierno de la Ciudad Autónoma de Buenos Aires

### Poder Legislativo:
- Senadores (por mayoría y primera minoría)
- Diputados (por sistema D'hondt)

## Deberá implementarse la siguiente funcionalidad:

### a.Disponer un menú de consulta de resultados:
1. Consulta de resultados Presidente y Vicepresidente
2. Consulta de resultados Gobernador y Vicegobernador
3. Consulta de resultados Senadores
4. Consulta de resultados Diputados

Cada opción de menú deberá asimismo mostrar por pantalla un informe con el siguiente formato y ordenado de mayor a menor según el total de votos:

![formato de salida]()

### b.Generación de archivos: 
Por cada región y tipo de cargo se deberá generar un archivo de texto llamado <REGION>_<CARGO>.csv (por ejemplo MENDOZA_GOBERNADOR.csv o SALTA_PRESIDENTE.csv) con el resumen del resultado según el siguiente diseño de registro:

> **COD_REGION ; NRO_LISTA ; VOTOS_OBTENIDOS ; PORCENTAJE_SOBRE_TOTAL**

### Criterios de aceptación:
- El material a entregar consistirá en el programa fuente escrito en Python y los archivos de datos obtenidos a partir de él.
- La entrega deberá realizarse a través del canal de Microsoft Teams asignado a cada grupo, adjuntando el material a la sección "Archivos" del mismo.
- El código debe modularizarse a través de funciones. Cada una debe resolver un subproblema completo, evitándose la realización de funciones elementales.
- La interfaz del programa deberá ser de línea de comandos.
- No se admitirá el uso de programación orientada a objetos, dado que este paradigma de programación no se instrumenta en las materias a las que apunta este certamen.
- El uso de módulos debe reducirse todo lo posible, salvo los esenciales como random. 
- Cualquier acto de plagio o deshonestidad académica será sancionado de acuerdo con la normativa vigente.

[Inicio](../README.md)