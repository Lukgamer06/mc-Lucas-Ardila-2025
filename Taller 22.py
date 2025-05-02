import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Datos del taller (x1, x2, y)
data = np.array([
    [1, 0, 0.2],
    [1, 0.5, 3],
    [2, 0.5, -0.8],
    [3, 1, -0.4],
    [-1.5, -1.2, 3.5],
    [2, 1.5, 3.6],
    [3, 1.5, 0.5],
    [3, 0.5, -1]
])

# Separar variables
x1 = data[:, 0]
x2 = data[:, 1]
y = data[:, 2]
n = len(y)

# Calcular sumatorias necesarias
sum_x1 = np.sum(x1)
sum_x2 = np.sum(x2)
sum_y = np.sum(y)
sum_x1_sq = np.sum(x1**2)
sum_x2_sq = np.sum(x2**2)
sum_x1x2 = np.sum(x1 * x2)
sum_x1y = np.sum(x1 * y)
sum_x2y = np.sum(x2 * y)

# Construir sistema de ecuaciones
A = np.array([
    [n, sum_x1, sum_x2],
    [sum_x1, sum_x1_sq, sum_x1x2],
    [sum_x2, sum_x1x2, sum_x2_sq]
])

b = np.array([sum_y, sum_x1y, sum_x2y])

# Resolver sistema para obtener coeficientes
coefficients = np.linalg.solve(A, b)
a0, a1, a2 = coefficients

# Calcular valores predichos
y_pred = a0 + a1*x1 + a2*x2

# Calcular suma de cuadrados de los residuos
S_r = np.sum((y - y_pred)**2)

# Calcular suma total de cuadrados
S_t = np.sum((y - np.mean(y))**2)

# Calcular coeficiente de determinación R²
R2 = 1 - (S_r / S_t)

# Calcular coeficiente de correlación r
r = np.sqrt(R2)

# Calcular error estándar
s_yx = np.sqrt(S_r / (n - 3))  # m=2 (x1 y x2)

# Resultados
print("Ecuación de regresión:")
print(f"y = {a0:.4f} + {a1:.4f}x1 + {a2:.4f}x2")
print(f"Coeficiente de determinación (R²): {R2:.4f}")
print(f"Coeficiente de correlación (r): {r:.4f}")
print(f"Error estándar (s_y/x): {s_yx:.4f}")

# Gráfica 2D (proyecciones)
plt.figure(figsize=(15, 5))

# Gráfica y vs x1
plt.subplot(1, 2, 1)
plt.scatter(x1, y, color='red', label='Datos')
x1_line = np.linspace(min(x1), max(x1), 100)
y_x1_line = a0 + a1*x1_line + a2*np.mean(x2)  # Usamos x2 promedio
plt.plot(x1_line, y_x1_line, label=f'y = {a0:.2f} + {a1:.2f}x1 + {a2:.2f}·x2_avg')
plt.xlabel('x1')
plt.ylabel('y')
plt.title('Relación y vs x1 (con x2 fijo en promedio)')
plt.legend()
plt.grid(True)

# Gráfica y vs x2
plt.subplot(1, 2, 2)
plt.scatter(x2, y, color='blue', label='Datos')
x2_line = np.linspace(min(x2), max(x2), 100)
y_x2_line = a0 + a1*np.mean(x1) + a2*x2_line  # Usamos x1 promedio
plt.plot(x2_line, y_x2_line, label=f'y = {a0:.2f} + {a1:.2f}·x1_avg + {a2:.2f}x2')
plt.xlabel('x2')
plt.ylabel('y')
plt.title('Relación y vs x2 (con x1 fijo en promedio)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Gráfica 3D

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Puntos de datos
ax.scatter(x1, x2, y, color='purple', label='Datos')

# Superficie de regresión
x1_surf, x2_surf = np.meshgrid(
    np.linspace(min(x1), max(x1), 100),
    np.linspace(min(x2), max(x2), 100)
)
y_surf = a0 + a1 * x1_surf + a2 * x2_surf
ax.plot_surface(x1_surf, x2_surf, y_surf, color='cyan', alpha=0.5, label='Superficie de regresión')

# Etiquetas y título
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
ax.set_title('Regresión múltiple: Gráfica 3D')
ax.legend()

plt.show()
