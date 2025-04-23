import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados en el taller
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1.5, 2.5, 3.5, 4.5, 6.5, 9.0])

# Paso 1: Transformación logarítmica de y
ln_y = np.log(y)

# Paso 2: Aplicar regresión lineal a los datos transformados
n = len(x)
sum_x = np.sum(x)
sum_ln_y = np.sum(ln_y)
sum_x_squared = np.sum(x**2)
sum_x_ln_y = np.sum(x * ln_y)

# Calcular pendiente (beta) e intercepto (ln_alpha)
beta = (n * sum_x_ln_y - sum_x * sum_ln_y) / (n * sum_x_squared - sum_x**2)
ln_alpha = (sum_ln_y - beta * sum_x) / n
alpha = np.exp(ln_alpha)

# Paso 3: Calcular valores predichos
y_pred = alpha * np.exp(beta * x)

# Paso 4: Calcular métricas de error
S_r = np.sum((y - y_pred)**2)  # Suma de cuadrados de los residuos
y_mean = np.mean(y)
S_t = np.sum((y - y_mean)**2)   # Suma total de cuadrados
r_squared = 1 - S_r / S_t       # Coeficiente de determinación

# Paso 5: Mostrar resultados
print(f"Modelo ajustado: y = {alpha:.4f} * e^({beta:.4f}x)")
print(f"Coeficiente de determinación (R²): {r_squared:.4f}")

# Paso 6: Graficar resultados
plt.figure(figsize=(10, 6))

# Datos originales
plt.scatter(x, y, color='red', label='Datos originales')

# Curva ajustada
x_curve = np.linspace(min(x), max(x), 100)
y_curve = alpha * np.exp(beta * x_curve)
plt.plot(x_curve, y_curve, 'b-', label=f'Ajuste: y = {alpha:.2f}e^({beta:.2f}x)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresión Exponencial por Mínimos Cuadrados')
plt.legend()
plt.grid(True)
plt.show()