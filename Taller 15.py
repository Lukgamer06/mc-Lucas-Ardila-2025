import copy

def imprimirSistema(a, b, etiqueta):
    n = len(b)
    print(etiqueta)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end = " ")
        print("|", b[i])
    print()

def intercambiarFilas(a, b, fila1, fila2):
    a[fila1], a[fila2] = a[fila2], a[fila1]
    b[fila1], b[fila2] = b[fila2], b[fila1]

def gaussJordan(ao, bo):
    a = copy.deepcopy(ao)
    b = copy.copy(bo)
    n = len(b)

    imprimirSistema(a, b, "Matriz inicial")
    
    for i in range(n):
        # Verificar si el pivote es cero y buscar fila para intercambiar
        if a[i][i] == 0:
            for k in range(i+1, n):
                if a[k][i] != 0:
                    intercambiarFilas(a, b, i, k)
                    print(f"Intercambio de fila {i+1} con fila {k+1}")
                    imprimirSistema(a, b, "Después del intercambio")
                    break
            else:
                raise ValueError("El sistema no tiene solución única")
        
        pivote = a[i][i]
        
        #Dividir por el pivote
        for j in range(n):
            a[i][j] /= pivote
        b[i] /= pivote
        imprimirSistema(a, b, "División")

        #Reducción
        for k in range(n):
            if i != k:
                #Se reduce
                valorAux = -a[k][i]
                for j in range(n):
                    a[k][j] += a[i][j] * valorAux
                b[k] += b[i] * valorAux
        imprimirSistema(a, b, "Reducción")
    
    return b

a = [[2, 0, 2], [4, 0, -1], [3, 2, -2]]
b = [7, 18, 16]

try: 
    x = gaussJordan(a, b)
    print("Respuesta:")
    for i in range(len(x)):
        print("x" + str(i+1), "=", x[i])

    #Pruebas
    print("\nPruebas:")
    for i in range(len(b)):
        valorAux = b[i]
        for j in range(len(b)):
            valorAux -= a[i][j] * x[j]
        print("Test", i + 1, "=", valorAux)
except ValueError as e:
    print(e)
    print("El sistema no tiene solución única")
except Exception as e:
    print("Error inesperado:", e)
