# Etapa 4
En el caso que ninguna fórmula presidencial haya obtenido el 45% del total de sufragios, o al menos 40% y una diferencia de 10 puntos porcentuales o más con respecto a la fórmula que le sigue, la Constitución Nacional establece la necesidad de realizar una segunda vuelta o balotaje. 

De esta segunda instancia sólo participan las dos fórmulas más votadas, y sólo integran las listas los candidatos a presidente y vicepresidente de cada partido ya que los demás cargos electivos se definen a través de otros mecanismos. En el balotaje el candidato ganador no necesita alcanzar un porcentaje determinado sino que se consagra por mayoría simple. 

Esta etapa final de la Copa de Algoritmia UADE 2023 consiste en la realización de dos programas:
1. Un programa para generar un archivo CSV con la misma estructura de registro utilizada en la etapa 2, pero incluyendo exclusivamente votos para la categoría presidente y vicepresidente de las dos fórmulas más votadas obtenidas en la etapa 3. La generación de los registros se instrumentará mediante números al azar, cuidando que se introduzca un sesgo similar al de la etapa 2 para evitar un posible empate técnico debido a la distribución uniforme de los números al azar.

Recordamos el formato de registro:

> **DNI ; Región ; Cargo ; Partido**

- **DNI:** Número de DNI del votante (valor entero positivo menor a 100000000)
- **Región:** Código de provincia, obtenido del archivo de regiones geográficas generado en la Etapa 1.
- **Cargo:** Código del cargo votado (sólo se admite código 1, ya que se vota únicamente a la categoría presidente y vice).
- **Partido:** Abreviatura del partido político votado, obtenida del archivo de partidos políticos generado en la Etapa 1.

2. Otro programa para realizar el escrutinio del archivo obtenido en el apartado ante-rior y proclamar al partido político ganador. Además deberá mostrarse por pantalla un listado de votos por región geográfica, ordenado alfabéticamente según el nombre de la misma y en forma descendente por cantidad de votos dentro de cada una:

![](imagenes/Captura(2).PNG)

Por último se informará el partido político triunfador:

**Partido ganador: <PARTIDO>**

**Porcentaje total país: <PORCENTAJE>**

### Criterios de aceptación:
- El material a entregar consistirá en el programa fuente escrito en Python y los archivos de datos obtenidos a partir de él.
- La entrega deberá realizarse a través del canal de Microsoft Teams asignado a cada grupo, adjuntando el material a la sección "Archivos" del mismo.
- El código debe modularizarse a través de funciones. Cada una debe resolver un subproblema completo, evitándose la realización de funciones elementales.
- La interfaz del programa deberá ser de línea de comandos.
- No se admitirá el uso de programación orientada a objetos, dado que este paradigma de programación no se instrumenta en las materias a las que apunta este certamen.
- El uso de módulos debe reducirse todo lo posible, salvo los esenciales como random.
- Cualquier acto de plagio o deshonestidad académica será sancionado de acuerdo con la normativa vigente.

[Inicio](../README.md)