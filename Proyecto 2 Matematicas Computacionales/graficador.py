import matplotlib.pyplot as plt

def graficar_resultados(puntos_x, puntos_y, coeficientes, grado, r2):
    """
    Grafica los puntos ingresados por el usuario y la curva de la regresión polinomial.

    :param puntos_x: Lista de coordenadas x de los puntos.
    :param puntos_y: Lista de coordenadas y de los puntos.
    :param coeficientes: Lista de coeficientes del polinomio de regresión.
    :param grado: Grado del polinomio de regresión.
    :param r2: Coeficiente de determinación (R²) de la regresión.
    """
    if not puntos_x or not puntos_y or not coeficientes:
        raise ValueError("Datos insuficientes para graficar.")
    
    # Crear un rango de valores x para graficar la curva
    x_min, x_max = min(puntos_x), max(puntos_x)
    x_grafica = [x_min + i * (x_max - x_min) / 1000 for i in range(1001)]
    
    # Evaluar el polinomio en los puntos del rango
    y_grafica = [
        sum(coeficientes[j] * (x ** j) for j in range(len(coeficientes)))
        for x in x_grafica
    ]
    
    # Graficar los puntos originales
    plt.scatter(puntos_x, puntos_y, color='red', label='Puntos originales')
    
    # Graficar la curva de regresión
    plt.plot(x_grafica, y_grafica, color='blue', label=f'Regresión grado {grado}')
    
    # Añadir título y etiquetas
    plt.title(f'Regresión Polinomial (Grado {grado})\nR² = {r2:.4f}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    
    # Mostrar la gráfica
    plt.grid()
    plt.show()

def mostrar_resultados(coeficientes, r_cuadrado, grado):
    print(f"Resultados de la regresión polinómica de grado {grado}:")
    print("Coeficientes:", coeficientes)
    print(f"Coeficiente de determinación (R²): {r_cuadrado:.4f}")