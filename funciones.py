#!/usr/bin/python
#-*- coding:UTF-8 -*-


# Obtener las colisiones verticalmente de una posicion
def colisionesVertical(x,y,matriz):

    colisiones = 0

    for x in range(len(matriz[0])):
        if(matriz[x][y] == 1):
            colisiones += 1


    return colisiones-1



# Calcular las colisiones diagonal inferior izquierda de una posicion
def diagonalInferiorIzquierda(x,y,matriz):
    
    a = x
    b = y
    colisiones = 0

    while b >= 0 and a <= len(matriz[0])-1:

        if(matriz[a][b] == 1):
            colisiones += 1

        a = a+1
        b = b-1

    return colisiones-1



# Calcular las colisiones diagonal inferior izquierda de una posicion
def diagonalInferiorDerecha(x,y,matriz):
    
    a = x
    b = y
    colisiones = 0

    while a <= len(matriz[0])-1 and b <= len(matriz[0])-1:

        if(matriz[a][b] == 1):
            colisiones += 1

        a = a+1
        b = b+1

    return colisiones-1



# Calcular las colisiones diagonal inferior izquierda de una posicion
def diagonalSuperiorDerecha(x,y,matriz):
    
    a = x
    b = y
    colisiones = 0

    while a >= 0 and b <= len(matriz[0])-1:

        if(matriz[a][b] == 1):
            colisiones += 1

        a = a-1
        b = b+1

    return colisiones-1



# Calcular las colisiones diagonal inferior izquierda de una posicion
def diagonalSuperiorIzquierda(x,y,matriz):
    
    a = x
    b = y
    colisiones = 0

    while a >= 0 and b >= 0:

        if(matriz[a][b] == 1):
            colisiones += 1

        a = a-1
        b = b-1

    return colisiones-1



# Obtener las colisiones digonalmente de una posicion
def colisionesDiagonal(x,y,matriz):
    colisiones = 0
    colisiones += diagonalInferiorIzquierda(x,y,matriz)
    colisiones += diagonalInferiorDerecha(x,y,matriz)
    colisiones += diagonalSuperiorDerecha(x,y,matriz)
    colisiones += diagonalSuperiorIzquierda(x,y,matriz)

    return colisiones



# Calcular las colisiones total de una posicion
def colisionesPosicion(x,y,matriz):
    colisiones = 0
    colisiones += colisionesVertical(x,y,matriz)
    colisiones += colisionesDiagonal(x,y,matriz)

    return colisiones



# Calcular Colisiones Matriz
def colisiones(matriz):
    colisiones = 0

    for x in range(len(matriz[0])):

        colisiones += colisionesPosicion(x,matriz[x].index(1),matriz)

    return colisiones



# Función para imrimir una matriz en consola
def imprimirMatriz(matriz):

    # linea separacion vertical
    linea = '-'
    for y in range(len(matriz[0])*4):
        linea += '-'

    # mostrar la matriz
    for x in range(len(matriz)):

        print linea

        for y in range(len(matriz[x])):

            print '| %s' % matriz[x][y] ,

        print '|'

    print linea