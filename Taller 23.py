import numpy as np

def lagrange_interpolation(x_points, y_points, x):
    """
    Calcula el valor interpolado usando polinomios de Lagrange
    x_points: puntos x conocidos
    y_points: valores f(x) conocidos
    x: punto a interpolar
    """
    n = len(x_points)
    result = 0.0
    
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# Datos del problema
x_data = np.array([1, 3, 5, 7, 9])
y_data = np.array([3, 0, -1, 2.5, 1])
x_to_interpolate = 4.25

# Interpolación de grado 1 (usa 2 puntos más cercanos a 4.25: 3 y 5)
x_degree1 = x_data[1:3]
y_degree1 = y_data[1:3]
interp_degree1 = lagrange_interpolation(x_degree1, y_degree1, x_to_interpolate)

# Interpolación de grado 2 (usa 3 puntos más cercanos: 1, 3 y 5)
x_degree2 = x_data[0:3]
y_degree2 = y_data[0:3]
interp_degree2 = lagrange_interpolation(x_degree2, y_degree2, x_to_interpolate)

# Interpolación de grado 3 (usa 4 puntos más cercanos: 1, 3, 5 y 7)
x_degree3 = x_data[0:4]
y_degree3 = y_data[0:4]
interp_degree3 = lagrange_interpolation(x_degree3, y_degree3, x_to_interpolate)

# Mostrar resultados
print("Resultados para f(4.25):")
print(f"Interpolación grado 1 (usando puntos x=3 y x=5): {interp_degree1:.4f}")
print(f"Interpolación grado 2 (usando puntos x=1, x=3 y x=5): {interp_degree2:.4f}")
print(f"Interpolación grado 3 (usando puntos x=1, x=3, x=5 y x=7): {interp_degree3:.4f}")

# Mostrar polinomios (solo para grados 1 y 2 como pide el problema)
print("\nPolinomio de grado 1 (usando x=3 y x=5):")
print(f"P1(x) = (x - 5)/(3 - 5)*0 + (x - 3)/(5 - 3)*(-1)")
print("Simplificado: P1(x) = 0.5*(x - 3)")

print("\nPolinomio de grado 2 (usando x=1, x=3 y x=5):")
print("P2(x) = (x-3)(x-5)/((1-3)(1-5))*3 + (x-1)(x-5)/((3-1)(3-5))*0 + (x-1)(x-3)/((5-1)(5-3))*(-1)")
print("Simplificado: P2(x) = 0.375(x-3)(x-5) - 0.125(x-1)(x-3)")