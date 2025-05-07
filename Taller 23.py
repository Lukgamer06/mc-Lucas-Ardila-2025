import numpy as np
import matplotlib.pyplot as plt

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

# Función para graficar
def graficar_interpolaciones(x_data, y_data, x_to_interpolate, interp_degree1, interp_degree2, interp_degree3):
    x_range = np.linspace(min(x_data), max(x_data), 500)
    
    # Grado 1
    y_interp1 = [lagrange_interpolation(x_degree1, y_degree1, x) for x in x_range]
    # Grado 2
    y_interp2 = [lagrange_interpolation(x_degree2, y_degree2, x) for x in x_range]
    # Grado 3
    y_interp3 = [lagrange_interpolation(x_degree3, y_degree3, x) for x in x_range]
    
    # Graficar puntos originales
    plt.scatter(x_data, y_data, color='red', label='Puntos originales')
    
    # Graficar interpolaciones
    plt.plot(x_range, y_interp1, label='Interpolación Grado 1', color='blue')
    plt.plot(x_range, y_interp2, label='Interpolación Grado 2', color='green')
    plt.plot(x_range, y_interp3, label='Interpolación Grado 3', color='purple')
    
    # Punto interpolado
    plt.scatter([x_to_interpolate], [interp_degree1], color='blue', marker='x', label='f(4.25) Grado 1')
    plt.scatter([x_to_interpolate], [interp_degree2], color='green', marker='x', label='f(4.25) Grado 2')
    plt.scatter([x_to_interpolate], [interp_degree3], color='purple', marker='x', label='f(4.25) Grado 3')
    
    # Configuración de la gráfica
    plt.title("Interpolaciones de Lagrange")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid()
    plt.show()

# Llamar a la función para graficar
graficar_interpolaciones(x_data, y_data, x_to_interpolate, interp_degree1, interp_degree2, interp_degree3)
