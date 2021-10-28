## Descripción secuencial del proceso relevante (A y D)

1. Eliminación de columnas no utilizadas: ultima_modificacion, nombre_seccion

2. Balanceo de clases seleccionando proporcionalmente (en realidad, un poco más) las inclinaciones negativas.

3. Proporción de la inclinación peligrosa según latitud y longitud. Se divide las respectivas clases uniformemente, para latitud 30, para longitud 100. Se agregan como nuevas columnas tales proporciones.

4. Proporción de la inclinación peligrosa según especie.

5. Aplicación de random forest, con ntree=700, utilizando las columnas anteriormente descritas junto a altura y diametro_tronco.

## Resultados obtenidos sobre el conjunto de validación

Ratio de error: 29.82%

Confusion matrix:

|   | 0  |    1| class.error|
|:-:|:--:|:---:|:----------:|
|0| 2838 |1293  | 0.3129993|
|1| 1006 |2573  | 0.2810841|

## Resultado final obtenido en Kaggle

Puntaje: 0.70180
