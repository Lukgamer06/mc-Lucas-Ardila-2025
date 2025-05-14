import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline

# Datos del taller
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 5, 2.5, 4, -1.6, 2])

# 1. Interpolación de Lagrange
poly_lagrange = lagrange(x, y)
lagrange_coeffs = np.poly1d(poly_lagrange).coeffs

# 2. Trazadores cúbicos
cs = CubicSpline(x, y, bc_type='natural')  # 'natural' impone f''=0 en los extremos

# Punto a evaluar
x_eval = 3.55
y_lagrange = poly_lagrange(x_eval)
y_spline = cs(x_eval)

# Crear puntos para graficar las curvas
x_plot = np.linspace(0, 5, 500)
y_lagrange_plot = poly_lagrange(x_plot)
y_spline_plot = cs(x_plot)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Puntos originales')
plt.plot(x_plot, y_lagrange_plot, '-', label=f'Polinomio de Lagrange (grado {len(x)-1})')
plt.plot(x_plot, y_spline_plot, '--', label='Trazadores cúbicos')
plt.axvline(x=x_eval, color='gray', linestyle=':')
plt.plot(x_eval, y_lagrange, 's', label=f'Lagrange(3.55) = {y_lagrange:.4f}')
plt.plot(x_eval, y_spline, 's', label=f'Spline(3.55) = {y_spline:.4f}')
plt.title('Comparación de métodos de interpolación')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

# Mostrar resultados
print("Resultados del Taller 25:")
print("\nPolinomio de Lagrange:")
print(f"Coeficientes (de mayor a menor grado): {lagrange_coeffs}")
print(f"f(3.55) ≈ {y_lagrange:.6f}")

print("\nTrazadores cúbicos:")
print(f"f(3.55) ≈ {y_spline:.6f}")

# Mostrar los polinomios por intervalo para los splines cúbicos
print("\nPolinomios por intervalo para los trazadores cúbicos:")
for i in range(len(x)-1):
    xi = x[i]
    xf = x[i+1]
    coefs = cs.c[:,i]  # Coeficientes para el intervalo [x[i], x[i+1]]
    print(f"\nIntervalo [{xi}, {xf}]:")
    print(f"f{i}(x) = {coefs[3]:.4f}(x-{xi})³ + {coefs[2]:.4f}(x-{xi})² + {coefs[1]:.4f}(x-{xi}) + {coefs[0]:.4f}")