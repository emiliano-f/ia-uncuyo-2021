# Reporte

## Formulación CSP para el Sudoku

CSP = (X, D, C):

X = {Xij}, 1<=i<=9, 1<=j<=9.

D = {Dij}, Dij = {1,2,3,4,5,6,7,8,9} 1<=i<=9, 1<=j<=9.

C = {Row(Xij), Col(Xij)}, Row = {Alldiff(Xij)}, 1<=i<=9, Col = {Alldiff(Xij)}, 1<=j<=9.

## Detectar la inconsistencia de la asignación parcial {WA = red, V = blue} con el algoritmo AC-3.

El dominio de WA solo contendrá un elemento (red) al igual que el dominio de V (blue).
En la cola se añadiran los arcos (NT, WA), (SA, WA), (SA, V), (NT, SA), (Q, NT), (Q, SA), (NSW, Q), (NSW, SA), (NSW, V) ... (los demás son irrelevantes en el tratamiento del problema).

El primer elemento a tratar en el algoritmo será el arco (NT, WA), donde su único valor en D(WA) detecta inconsistencia en D(NT), se elimina red de D(NT). y se agregan los arcos (SA, NT) y (Q, NT) a la cola.

El siguiente elemento de la cola es (SA, WA), donde se repite la situación anterior por lo que se elimina red de D(SA) y se agregan los arcos (NT, SA), (Q, SA), (NSW, SA) y (V, SA).

Luego, el elemento es (SA, V). Se elimina blue de D(SA) y se agregan los arcos (WA, SA), (NT, SA), (Q, SA) y (NSW, SA).

El siguiente es el arco (NT, SA). Se elimina green de D(NT), se agregan los arcos (WA, NT) y (Q, NT).

Se extrae el arco (Q, NT). Se elimina blue de D(Q). Se agregan los arcos (SA, Q) y (NSW, Q).

Obtenemos el arco (Q, SA). Se elimina green de D(Q) y agregamos (NT, Q) y (NSW, Q).

Si aplicamos el algoritmo a los siguientes tres arcos (Q, NSW), (SA, NSW) y (V, NSW), el conjunto D(NSW) será vacio por lo que se encontró una inconsistencia.

## Complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado

La complejidad en un árbol estructurado CSP es O(nd^2) pero si consideramos que cada arco será visitado una única vez, O(nd).

## Si por cada arco (Xk,Xi) se lleva cuenta del número de valores que quedan de Xi que sean consistentes con Xk, explicar como actualizar ese número de manera eficiente y demostrar que la arco consistencia puede lograrse en un tiempo total O(n^2d^2)

La actualización del número de valores consistentes puede realizarse disminuyendo en una unidad cada que se quite un arco. Esto tiene una complejidad de O(1) y para la totalidad de los arcos O(d) siempre que todos ellos se encuentren afectados según la naturaleza del problema. No obstante, esto no implica agregar d veces un arco a la cola, sino que no es agregado. por lo que la complejidad restante es de la consistencia de arco. En conclusión, la complejidad es de O(n^2d^2)

## Demostrar la correctitud del algoritmo CSP para árboles estructurados

a. Los pasos desarrollados en el libro tienen como objetivo reducir un problema de n-consistencia a uno de 2-consistencia (arco consistencia). Si los nodos se ordenan tal como lo requiere el algoritmo, entonces la comprobación de arco-consistencia en orden inverso logra que cualquier valor suprimido posteriormente no coloca en peligro la consistencia de arcos que ya han sido tratados. En conclusión, la 2-consistencia puede resolver una n-consistencia dadas las hipótesis.

b. Esto es así debido a que en el algoritmo AC-3, los arcos reinsertados corresponden a los pares (Xk, Xi) donde Xi contiene el dominio de elementos recientemente suprimidos (en el análisis de (Xi,Xj)). En otras palabras, para que un valor suprimido pudiera afectar la consistencia ya lograda, los arcos reinsertados en AC-3 deberían involucrar elementos de Xj.

## Tiempos de ejecución

Promedios (los datos en bruto se encuentran en out_bt.csv y out_fc.csv para backtracking y forward checking respectivamente).

|     | Backtracking | Forward checking |
|:--: |:------------:|:----------------:|
|4 | 6.516218185424805e-05 | 9.282112121582031e-05 |
|8 | 0.0012094879150390625 | 0.0011130285263061524 |
|10 | 0.001434159278869629 | 0.001191246509552002 |
|12 | 0.004759273529052734 | 0.003332078456878662 |
|15 | 0.03411295652389526 | 0.02230879306793213 |

## Cantidad de estados recorridos

|     | Backtracking | Forward checking |
|:--: |:------------:|:----------------:|
|4 | 26 | 8|
|8 | 876 | 88|
|10 | 975 | 83|
|12 | 3066 | 193|
|15 | 20280 | 1026|

## Gráfico de cajas

### Size: 4
![size4](size4.png?raw=true "Title")

### Size: 8
![size8](size8.png?raw=true "Title")

### Size: 10
![size10](size10.png?raw=true "Title")

### Size: 12
![size12](size12.png?raw=true "Title")

### Size: 15
![size15](size15.png?raw=true "Title")
