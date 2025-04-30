import numpy as np
import matplotlib.pyplot as plt

# Datos del taller
x = np.array([0, 2, 4, 6, 8, 10, 12])
y = np.array([7.5, 1.8, -1, -1.8, -1.2, 2.2, 7.2])

# Ajuste de polinomio de segundo grado (cuadrático)
coefficients = np.polyfit(x, y, 2)
polynomial = np.poly1d(coefficients)

# Valores predichos
y_pred = polynomial(x)

# Cálculo del coeficiente de determinación (R²) manualmente
ss_res = np.sum((y - y_pred)**2)  # Suma de cuadrados de los residuos
ss_tot = np.sum((y - np.mean(y))**2)  # Suma total de cuadrados
r2 = 1 - (ss_res / ss_tot)

# Coeficiente de correlación (r)
r = np.sqrt(r2) if r2 >= 0 else -np.sqrt(abs(r2))

# Imprimir resultados
print("Polinomio ajustado:")
print(polynomial)
print(f"\nCoeficiente de determinación (R²): {r2:.4f}")
print(f"Coeficiente de correlación (r): {r:.4f}")

# Crear gráfica
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='red', label='Datos originales')
plt.plot(x, y_pred, color='blue', label=f'Ajuste polinomial: {polynomial}')
plt.title('Regresión Polinomial de Segundo Grado')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()