# Taller 17: Regresión Lineal por Mínimos Cuadrados
import numpy as np
import matplotlib.pyplot as plt

def regresion_lineal(x, y):
    n = len(x)
    # Calcular las sumatorias necesarias
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2 = np.sum(x**2)
    
    # Calcular los coeficientes
    a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    a0 = np.mean(y) - a1 * np.mean(x)
    
    return a0, a1

# Datos del taller
x = np.array([ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7])
y = np.array([7.5,5.5,6.5,3.5,4.5, 3 ,2.5, 1])

# Calcular la regresión lineal
a0, a1 = regresion_lineal(x, y)

# Mostrar resultados de la regresión lineal
print("Resultados de la regresión lineal por mínimos cuadrados:")
print(f"Coeficiente a0 (intercepto): {round(a0, 4)}")
print(f"Coeficiente a1 (pendiente): {round(a1, 4)}")
print(f"Coeficiente de determinación R^2: {round(1 - (np.sum((y - (a0 + a1 * x))**2) / np.sum((y - np.mean(y))**2)), 4)}")
print(f"Error estándar de la estimación: {round(np.sqrt(np.sum((y - (a0 + a1 * x))**2) / (len(x) - 2)), 4)}")
print(f"Valor p para la pendiente: {round(2 * (1 - np.abs(a1) / np.sqrt(np.sum((y - (a0 + a1 * x))**2) / (len(x) - 2))), 4)}")
print(f"Valor p para el intercepto: {round(2 * (1 - np.abs(a0) / np.sqrt(np.sum((y - (a0 + a1 * x))**2) / (len(x) - 2))), 4)}")
print(f"Valor p para la regresión: {round(2 * (1 - np.abs(a1) / np.sqrt(np.sum((y - (a0 + a1 * x))**2) / (len(x) - 2))), 4)}")
print(f"Valor p para la regresión (ajustado): {round(2 * (1 - np.abs(a1) / np.sqrt(np.sum((y - (a0 + a1 * x))**2) / (len(x) - 2))), 4)}")
print(f"Ecuación de la recta: y = {round(a0, 4)} + {round(a1, 4)}x")

# Calcular valores predichos
y_pred = a0 + a1 * x

# Calcular suma de cuadrados de los residuos
S_r = np.sum((y - y_pred)**2)
print(f"Suma de cuadrados de los residuos (S_r): {round(S_r,4)}")

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='red', label='Datos observados')
plt.plot(x, y_pred, color='blue', label=f'Regresión lineal: y = {round(a0,3)} + {round(a1,3)}x')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresión Lineal por Mínimos Cuadrados')
plt.legend()
plt.grid(True)
plt.show()