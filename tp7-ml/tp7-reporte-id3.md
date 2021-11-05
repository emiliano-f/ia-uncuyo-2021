# Evaluación sobre tennis.csv

outlook

    ('sunny', 'humidity')

    ('overcast', 'no')

    ('rainy', 'windy')

humidity

    ('high', 'yes')

    ('normal', 'no')

windy

    (False, 'no')

    (True, 'yes')

# Ärboles de regresión para datos de tipo real

Si intentamos predecir un valor numérico, como el precio de una obra de arte, más que una clasificación discreta necesitamos un árbol de regresión. Este tipo de árbol tiene en cada hoja una función lineal de algún subconjunto de atributos numéricos, en vez de un valor simple. Por ejemplo, la rama para grabados pintados a mano puede terminar con una función lineal del área, edad y número de colores. El algoritmo de aprendizaje debe decidir cuándo dejar de dividir para comenzar a aplicar regresión lineal utilizando los atributos restantes (o algún subconjunto).
