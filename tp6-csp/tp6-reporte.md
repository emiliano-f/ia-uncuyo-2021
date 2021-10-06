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


