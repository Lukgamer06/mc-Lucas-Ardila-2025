from random import randint
#Ejercicio 1
def generar_vector(n):
    vector = []
    for i in range(n):
        vector.append(randint(1, 100))
    return vector

def producto_punto(v1, v2):
    producto = 0
    for i in range(len(v1)):
        producto += v1[i] * v2[i]
    return producto

n=int(input("Ingrese el tamaño de los vectores: "))
v1 = generar_vector(n)
v2 = generar_vector(n)
print("Vector 1:", v1)
print("Vector 2:", v2)
print("Producto punto:", producto_punto(v1, v2))

print("\n\n")

#Ejercicio 2
def generar_matrizes():
    matriz1 = []
    matriz2 = []
    n = randint(2, 8)
    for i in range(n):
        filam1 = []
        filam2 = []
        for j in range(n):
            filam1.append(randint(1, 20))
            filam2.append(randint(1, 20))
        matriz1.append(filam1)
        matriz2.append(filam2)
    return matriz1, matriz2

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def suma_matrices(m1, m2):
    suma = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[i])):
            fila.append(m1[i][j] + m2[i][j])
        suma.append(fila)
    return suma

def multiplicacion_matrices(m1, m2):
    multiplicacion = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m2[0])):
            suma = 0
            for k in range(len(m1[i])):
                suma += m1[i][k] * m2[k][j]
            fila.append(suma)
        multiplicacion.append(fila)
    return multiplicacion

m1, m2 = generar_matrizes()
print("Matriz 1:")
imprimir_matriz(m1)
print("Matriz 2:")
imprimir_matriz(m2)
print("Suma de matrices:")
imprimir_matriz(suma_matrices(m1, m2))
print("Multiplicación de matrices:")
imprimir_matriz(multiplicacion_matrices(m1, m2))
