import copy
import numpy as np
import matplotlib.pyplot as plt

def gaussJordan(a, b):
    aAux = copy.deepcopy(a)
    bAux = b.copy()

    n = len(bAux)

    # Se realiza la reducción a matriz identidad
    for i in range(n):
        # Pivoteo
        if aAux[i][i] == 0:
            for k in range(i + 1, n):
                if aAux[k][i] != 0:
                    filaAux = aAux[i]
                    aAux[i] = aAux[k]
                    aAux[k] = filaAux

                    valoAux = bAux[i]
                    bAux[i] = bAux[k]
                    bAux[k] = valoAux
                    break

        # Escalonamiento
        valorAux = aAux[i][i]
        for j in range(i, n):
            aAux[i][j] /= valorAux
        bAux[i] /= valorAux

        # Reducción
        for j in range(n):
            if j != i:
                fact = aAux[j][i] / aAux[i][i]

                for k in range(n):
                    aAux[j][k] -= (aAux[i][k] * fact)
                bAux[j] -= (bAux[i] * fact)
                
    return bAux

def trazadoresCubicos(x, y):
    n = len(x)

    # Se crea la matriz de los trazadores
    a = []
    b = [0] * (n - 2)
    for i in range(n - 2):
        a.append(b.copy())
              
    for i in range(1, n - 1):
        if i > 1:
            a[i - 1][i - 2] = x[i] - x[i - 1]
        a[i - 1][i - 1] = 2 * (x[i + 1] - x[i - 1])
        if i < n - 2:
            a[i - 1][i] = x[i + 1] - x[i]
        b[i - 1] = (6 / (x[i + 1] - x[i])) * (y[i + 1] - y[i]) + (6 / (x[i] - x[i - 1]) * (y[i - 1] - y[i]))

    rtaAux = gaussJordan(a, b)

    # Se agrega el valor de la derivada de los extremos como cero
    f2 = [0] + rtaAux + [0]

    # Matriz de coeficientes
    coeficientes = []

    for i in range(1, n):
        t1 = f2[i - 1] / (6 * (x[i] - x[i - 1]))
        t2 = f2[i] / (6 * (x[i] - x[i - 1]))
        t3 = y[i - 1] / (x[i] - x[i - 1]) - f2[i - 1] * (x[i] - x[i - 1]) / 6
        t4 = y[i] / (x[i] - x[i - 1]) - f2[i] * (x[i] - x[i - 1]) / 6

        arrCoef = [0] * 4

        # Se calculan los coeficientes del polinomio
        arrCoef[0] = t1 * x[i]**3 - t2 * x[i - 1]**3 + t3 * x[i] - t4 * x[i - 1]
        arrCoef[1] = -t1 * 3 * x[i]**2 + t2 * 3 * x[i - 1]**2 - t3 + t4
        arrCoef[2] = t1 * 3 * x[i] - t2 * 3 * x[i - 1]
        arrCoef[3] = -t1 + t2

        coeficientes.append(arrCoef)

    return coeficientes

def lagrange_interpolation(x, y, x_eval):
    n = len(x)
    result = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_eval - x[j]) / (x[i] - x[j])
        result += term
    return result

def main():
    # Datos del taller
    x = [0, 1, 2, 3, 4, 5]
    y = [0, 5, 2.5, 4, -1.6, 2]

    # Trazadores cúbicos
    coeficientes = trazadoresCubicos(x, y)

    # Imprimir los trazadores cúbicos
    print("Trazadores cúbicos:")
    for i, arrCoef in enumerate(coeficientes):
        print(f'f(x) = {arrCoef[0]:.4f} + {arrCoef[1]:.4f}x + {arrCoef[2]:.4f}x^2 + {arrCoef[3]:.4f}x^3 [{x[i]} <= x < {x[i + 1]}]')

    # Evaluar f(3.55) con trazadores cúbicos
    x_eval = 3.55
    for i in range(len(x) - 1):
        if x[i] <= x_eval < x[i + 1]:
            a, b, c, d = coeficientes[i]
            y_eval_spline = a + b * x_eval + c * x_eval**2 + d * x_eval**3
            break
    print(f"\nEstimación con trazadores cúbicos en f(3.55): {y_eval_spline:.4f}")

    # Evaluar f(3.55) con interpolación de Lagrange
    y_eval_lagrange = lagrange_interpolation(x, y, x_eval)
    print(f"Estimación con Lagrange en f(3.55): {y_eval_lagrange:.4f}")

    # Graficar los puntos y los trazadores cúbicos
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='red', label='Puntos dados')

    # Graficar los trazadores cúbicos
    x_vals = np.linspace(x[0], x[-1], 500)
    y_vals = np.zeros_like(x_vals)
    for i in range(len(coeficientes)):
        a, b, c, d = coeficientes[i]
        mask = (x_vals >= x[i]) & (x_vals <= x[i + 1])
        y_vals[mask] = a + b * x_vals[mask] + c * x_vals[mask]**2 + d * x_vals[mask]**3
    plt.plot(x_vals, y_vals, label='Trazadores cúbicos')

    # Graficar el polinomio de Lagrange (opcional, puede ser lento para muchos puntos)
    x_lagrange = np.linspace(x[0], x[-1], 500)
    y_lagrange = [lagrange_interpolation(x, y, xi) for xi in x_lagrange]
    plt.plot(x_lagrange, y_lagrange, '--', label='Polinomio de Lagrange')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Interpolación con Trazadores Cúbicos y Polinomio de Lagrange')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
