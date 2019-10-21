#!/usr/bin/python
#-*- coding:UTF-8 -*-
import sys
import random
import funciones as f

# Total de reinas
n = int(sys.argv[1])


# Matriz del tablero
matriz = [[' '] * n for i in range(n)]


# Llenar aleatoriamente las reinas
for x in range(n):
    matriz[x][random.randrange(0,n)] = 1


# Mostrar estado inicial
f.imprimirMatriz(matriz)


# Calculamos el total de colisiones
total = f.colisiones(matriz)


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
    print total
    print ''


f.imprimirMatriz(matriz)

print total