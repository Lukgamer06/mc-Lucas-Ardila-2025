# Taller 16: Inversión de matrices usando el método de Gauss-Jordan
# Funcion para imprimir matrices de forma legible
def print_matrix(matrix):
    for row in matrix:
        print("[", end="")
        for i, num in enumerate(row):
            print(f"{num:8.4f}", end="")
            if i != len(row) - 1:
                print(", ", end="")
        print("]")

# Funcion para multiplicar matrices
def multiplicar_matriz(a, b):
    n = len(a)
    m = len(b[0])
    p = len(b)
    result = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            for k in range(p):
                result[i][j] += a[i][k] * b[k][j]
    return result

# Funcion para crear una matriz identidad de tamaño n
def matriz_identidad(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# Funcion para copiar una matriz
def copiar_matriz(matrix):
    return [row[:] for row in matrix]

# Funcion para calcular la inversa de una matriz usando el metodo de Gauss-Jordan
def gauss_jordan_inverso(matrix):
    n = len(matrix)
    inverse = matriz_identidad(n)
    augmented = [row[:] + inverse[i] for i, row in enumerate(matrix)]
    
    for col in range(n):
        # Pivoteo parcial
        max_row = col
        for i in range(col + 1, n):
            if abs(augmented[i][col]) > abs(augmented[max_row][col]):
                max_row = i
        augmented[col], augmented[max_row] = augmented[max_row], augmented[col]
        
        # Normalizar fila pivote
        pivot = augmented[col][col]
        if pivot == 0:
            raise ValueError("La matriz no es invertible")
        for j in range(col, 2 * n):
            augmented[col][j] /= pivot
        
        # Eliminación
        for i in range(n):
            if i != col and augmented[i][col] != 0:
                factor = augmented[i][col]
                for j in range(col, 2 * n):
                    augmented[i][j] -= factor * augmented[col][j]
    
    # Extraer la inversa
    inverse = [row[n:] for row in augmented]
    return inverse

# Funcion para verificar si la inversa es correcta
def verificar_inverso(original, inverse):
    product = multiplicar_matriz(original, inverse)
    n = len(original)
    identity = matriz_identidad(n)
    
    # Verificar si el producto es aproximadamente la matriz identidad
    for i in range(n):
        for j in range(n):
            if abs(product[i][j] - identity[i][j]) > 1e-6:
                return "No Es Inversa"
    return "Si Es Inversa"

# Matrices del problema
A = [
    [3, 2, 2],
    [3, 1, -3],
    [1, 0, -2]
]

B = [
    [1, 2, 0, 4],
    [2, 0, -1, -2],
    [1, 1, -1, 0],
    [0, 4, 1, 0]
]

# Calcular y mostrar resultados para la matriz A
print("=== Matriz A ===")
try:
    A_inv = gauss_jordan_inverso(A)
    print("\nInversa de A:")
    print_matrix(A_inv)
    
    print("\nVerificación A * A_inv:")
    verification = multiplicar_matriz(A, A_inv)
    print_matrix(verification)
    
    print("\n¿Es correcta la inversa?\n", verificar_inverso(A, A_inv))
except ValueError as e:
    print(f"\nError: {e}")

# Calcular y mostrar resultados para la matriz B
print("\n=== Matriz B ===")
try:
    B_inv = gauss_jordan_inverso(B)
    print("\nInversa de B:")
    print_matrix(B_inv)
    
    print("\nVerificación B * B_inv:")
    verification = multiplicar_matriz(B, B_inv)
    print_matrix(verification)
    
    print("\n¿Es correcta la inversa?\n", verificar_inverso(B, B_inv))
except ValueError as e:
    print(f"\nError: {e}")