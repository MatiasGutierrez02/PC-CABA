import random
def imprimir_matriz (mtz):
    for fila in mtz:     
        for elemento in fila:
            print("%5d" %elemento, end="")
        print()

def rellenar_matriz(m, n):
    x = 1
    y = 0
    for filas in range(n):
        for columnas in range(n-x, n-y):
            m[filas][columnas] = random.randint(1,99)
            x += 1
            y += 1
    return m

#Programa Principal
num = int(input("Ingrese el ancho y largo de la matriz: "))
matriz = [[0]*num for i in range(num)]
matriz_rellena = rellenar_matriz (matriz, num)
imprimir_matriz(matriz_rellena)
