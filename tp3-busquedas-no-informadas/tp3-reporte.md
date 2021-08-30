# Reporte

### Condiciones particulares.

Cada entorno generado tiene una proporción de 0.3 obstáculos, en una dimensión de 100x100. La posición inicial y final son generadas aleatoriamente. Cada evaluación fue dada a partir de un nuevo entorno, siendo la cantidad de pruebas 90 en total, 30 por algoritmo. El límite de la búsqueda en profundidad fue establecido en 50, razón por la que los parámetros dan un valor tan bajo en comparación a los otros dos tipos de búsqueda.

## Agente mediante búsqueda en anchura:

Media: 3380.04
Desviación estándar: 2025.08

## Agente en búsqueda uniforme:

Media: 4089.74
Desviación estándar: 2750.39

## Agente en búsqueda en profundidad:

Media 245.33
Desviación estándar: 142.47

## Graficos

![report](report.png?raw=true "Title")

En rojo: media. En azul: desviación estándar.
BFS (1), US (2), DLS (3).

## Conclusión

Para las características planteadas en el problema, lo más conveniente es utilizar búsqueda en anchura. Las razones son sencillas:

1. Originalmente, el problema puede ser expresado como un grafo no dirigido ni ponderado. Por ende, utilizar búsqueda uniforme no tiene sentido en este escenario.

2. El objetivo es encontrar el camino más corto. Esto puede hallarse a medida que se descubren nodos en anchura, entregando la secuencia en primera instancia de ser encontrada. Sin embargo, utilizar una búsqueda en profundidad no me asegura hallar en primera instancia el camino más corto, por lo que en sucesivas búsquedas éste debe ser actualizado en caso de encontrar uno de menor longitud. En consecuencia, DLS no es apto para este problema.

Quedan expuestos los motivos para decantar por BFS.
