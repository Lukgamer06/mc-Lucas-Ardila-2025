import matplotlib.pyplot as plt
import numpy as np

def multiplicar_binomios(p1, p2):  
    # Grado del polinomio resultante
    grado = len(p1) + len(p2) - 2
    # Inicializar el polinomio resultante con ceros
    resultado = [0] * (grado + 1)
    
    # Multiplicar los polinomios
    for index_a, coef_a in enumerate(p1):
        for index_b, coef_b in enumerate(p2):
            resultado[index_a + index_b] += coef_a * coef_b

    return resultado


def evaluar_polinomio(polinomio, x):
    """Evalúa un polinomio en un valor x."""
    resultado = 0
    for i, coef in enumerate(polinomio):
        resultado += coef * (x ** i)
    return resultado


def main():
    # Puntos de interpolación
    x = [1, 2, 3, 4, 5]
    y = [2, 0.5, -2, -3.5, 0.5]

    n = len(x)
    polinomio_final = [0]  # Polinomio acumulado

    # Construcción del polinomio de interpolación
    for i in range(n):
        # Inicializar L_i como [1] (polinomio constante)
        L_i = [1]
        denominador = 1

        # Construir el término L_i
        for j in range(n):
            if i != j:
                # Multiplicar los binomios
                L_i = multiplicar_binomios(L_i, [1, -x[j]])
                denominador *= (x[i] - x[j])

        # Escalar L_i por y[i] / denominador
        L_i = [coef * (y[i] / denominador) for coef in L_i]

        # Sumar L_i al polinomio final
        polinomio_final = [a + b for a, b in zip(polinomio_final + [0] * (len(L_i) - len(polinomio_final)), L_i)]

    # Mostrar el polinomio final
    print("Polinomio de interpolación de Lagrange:")
    print(polinomio_final)

    # Evaluar el polinomio en varios puntos
    print("\nEvaluación del polinomio:")
    for xi in x:
        print(f"P({xi}) = {evaluar_polinomio(polinomio_final, xi)}")

    # Graficar el polinomio
    x_vals = np.linspace(min(x) - 1, max(x) + 1, 500)  # Valores de x para la gráfica
    y_vals = [evaluar_polinomio(polinomio_final, xi) for xi in x_vals]  # Evaluar el polinomio en esos puntos

    plt.plot(x_vals, y_vals, label="Polinomio de Lagrange", color="blue")
    plt.scatter(x, y, color="red", label="Puntos de interpolación")  # Puntos originales
    plt.title("Polinomio de Interpolación de Lagrange")
    plt.xlabel("x")
    plt.ylabel("P(x)")
    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
    plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
    plt.legend()
    plt.grid()
    plt.show()


main()