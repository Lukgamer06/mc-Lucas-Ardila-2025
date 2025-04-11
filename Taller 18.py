import numpy as np
import matplotlib.pyplot as plt

# Datos del taller
x = np.array([0, 1 ,2, 3 , 4 ,5,  6  ])
y = np.array([0,0.5,2,3.5,4.5,9, 13.5])

# 1. Cálculo de la regresión lineal (mínimos cuadrados)
def regresion_lineal(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2 = np.sum(x ** 2)

    # Pendiente (a1) e intercepto (a0)
    a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    a0 = (sum_y - a1 * sum_x) / n

    return a0, a1

n = len(x)  # Número de datos

# Pendiente (a1) e intercepto (a0)
a0, a1 = regresion_lineal(x, y)

print(f"Ecuación de regresión: y = {round(a0,4)} + {round(a1,4)}x")

# 2. Cálculo de las predicciones y residuos
y_pred = a0 + a1 * x
residuos = y - y_pred

# 3. Cálculo de St (suma total de cuadrados)
y_mean = np.mean(y)
St = np.sum((y - y_mean) ** 2)

# 4. Cálculo de Sr (suma de los cuadrados de los residuos)
Sr = np.sum(residuos ** 2)

# 5. Cálculo de sy (desviación estándar)
sy = np.sqrt(St / (n - 1))

# 6. Cálculo de sy/x (error estándar de la estimación)
syx = np.sqrt(Sr / (n - 2))

# 7. Cálculo de r2 (coeficiente de determinación)
r2 = (St - Sr) / St

# 8. Cálculo de r (coeficiente de correlación)
r = np.sqrt(r2)  # Podría ser positivo o negativo, depende de la pendiente

# Resultados
print("\nResultados:")
print(f"Suma total de cuadrados (St): {round(St,4)}")
print(f"Suma de cuadrados de residuos (Sr): {round(Sr,4)}")
print(f"Desviación estándar (sy): {round(sy,4)}")
print(f"Error estándar de la estimación (sy/x): {round(syx,4)}")
print(f"Coeficiente de determinación (r²): {round(r2,4)}")
print(f"Coeficiente de correlación (r): {round(r,4)}")

# Gráfico de los datos y la línea de regresión
plt.scatter(x, y, color='blue', label='Datos reales')
plt.plot(x, y_pred, color='red', label=f'Regresión: y = {round(a0,2)} + {round(a1,2)}x')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresión Lineal y Medidas de Error')
plt.legend()
plt.grid(True)
plt.show()