#!/usr/bin/python
#-*- coding:UTF-8 -*-
import sys
import funciones as f

# Total de reinas
n = int(sys.argv[1])


# Restriccion de reinas
if(n < 4):
    print '\n Debes ingresar minimo 4 reinas'
    exit()


# Matriz del tablero
matriz = f.llenarMatriz(n)


# Mostrar estado inicial
f.imprimirMatriz(matriz)


# Calculamos el total de colisiones
total = f.colisiones(matriz)
total_aux = total


# Total repeticiones
repeticiones = 0


# Calcular nueva posicion
while total > 0:

    for x in range(n):
        colisionMenor = f.colisionesPosicion(x,matriz[x].index(1),matriz)

        for y in range(n):
            colisionActual = f.colisionesPosicion(x,y,matriz)

            if(colisionActual < colisionMenor):
                colisionMenor = colisionActual
                matriz[x][matriz[x].index(1)] = ' '
                matriz[x][y] = 1

    f.imprimirMatriz(matriz)
    total = f.colisiones(matriz)


    # Guardar total colisiones actual y anterior
    if total < total_aux:
        total_aux = total
    else:
        repeticiones += 1


    # Llevar cuenta de las repeticiones entre las colisiones
    if repeticiones == 10:
        matriz = f.llenarMatriz(n)
        repeticiones = 0


    print (total, total_aux)
    print ''


# Mostrar tablero final y sus colisiones
f.imprimirMatriz(matriz)
print total