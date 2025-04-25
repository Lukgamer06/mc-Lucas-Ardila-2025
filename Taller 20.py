import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([4.5, 6.5, 7.5, 8, 8.4, 8.8, 9, 9.3])

# Función para calcular el coeficiente de determinación R²
def r_squared(y_obs, y_pred):
    ss_res = np.sum((y_obs - y_pred) ** 2)
    ss_tot = np.sum((y_obs - np.mean(y_obs)) ** 2)
    return 1 - (ss_res / ss_tot)

# Función para regresión lineal manual
def linear_regression(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2 = np.sum(x ** 2)
    
    # Pendiente (b) e intercepto (a)
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    a = (sum_y - b * sum_x) / n
    
    return a, b

# 1. Modelo Lineal: y = a + b*x
a_lin, b_lin = linear_regression(x, y)
y_pred_lin = a_lin + b_lin * x
r2_lin = r_squared(y, y_pred_lin)

# 2. Modelo Exponencial: y = a*e^(b*x) -> ln(y) = ln(a) + b*x
if np.all(y > 0):
    log_y = np.log(y)
    a_log, b_exp = linear_regression(x, log_y)
    a_exp = np.exp(a_log)
    y_pred_exp = a_exp * np.exp(b_exp * x)
    r2_exp = r_squared(y, y_pred_exp)
else:
    r2_exp = -np.inf

# 3. Modelo de Potencias: y = a*x^b -> ln(y) = ln(a) + b*ln(x)
if np.all(x > 0) and np.all(y > 0):
    log_x = np.log(x)
    log_y = np.log(y)
    a_log, b_pow = linear_regression(log_x, log_y)
    a_pow = np.exp(a_log)
    y_pred_pow = a_pow * (x ** b_pow)
    r2_pow = r_squared(y, y_pred_pow)
else:
    r2_pow = -np.inf

# 4. Modelo de Razón de Crecimiento: y = a*x/(b + x) -> 1/y = (1/a) + (b/a)*(1/x)
if np.all(x != 0) and np.all(y != 0):
    inv_x = 1 / x
    inv_y = 1 / y
    intercept_rc, slope_rc = linear_regression(inv_x, inv_y)
    a_rc = 1 / intercept_rc
    b_rc = slope_rc * a_rc
    y_pred_rc = a_rc * x / (b_rc + x)
    r2_rc = r_squared(y, y_pred_rc)
else:
    r2_rc = -np.inf

# Resultados
print("Comparación de modelos:")
print(f"1. Lineal: y = {a_lin:.4f} + {b_lin:.4f}x, R² = {r2_lin:.4f}")

if r2_exp != -np.inf:
    print(f"2. Exponencial: y = {a_exp:.4f}e^({b_exp:.4f}x), R² = {r2_exp:.4f}")
else:
    print("2. Exponencial: No aplicable (valores y <= 0)")

if r2_pow != -np.inf:
    print(f"3. Potencias: y = {a_pow:.4f}x^{b_pow:.4f}, R² = {r2_pow:.4f}")
else:
    print("3. Potencias: No aplicable (valores x o y <= 0)")

if r2_rc != -np.inf:
    print(f"4. Razón de crecimiento: y = {a_rc:.4f}x/({b_rc:.4f} + x), R² = {r2_rc:.4f}")
else:
    print("4. Razón de crecimiento: No aplicable (valores x o y = 0)")

# Determinar el mejor modelo
models = {
    "Lineal": r2_lin,
    "Exponencial": r2_exp if r2_exp != -np.inf else -1,
    "Potencias": r2_pow if r2_pow != -np.inf else -1,
    "Razón de crecimiento": r2_rc if r2_rc != -np.inf else -1
}

best_model = max(models, key=models.get)
print(f"\nEl mejor modelo es: {best_model} con R² = {models[best_model]:.4f}")

# Gráficos
plt.figure(figsize=(15, 10))

# Datos originales
plt.subplot(2, 2, 1)
plt.scatter(x, y, color='black', label='Datos')
plt.plot(x, y_pred_lin, color='blue', label=f'Lineal (R²={r2_lin:.4f})')
plt.title('Modelo Lineal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

if r2_exp != -np.inf:
    plt.subplot(2, 2, 2)
    plt.scatter(x, y, color='black', label='Datos')
    plt.plot(x, y_pred_exp, color='red', label=f'Exponencial (R²={r2_exp:.4f})')
    plt.title('Modelo Exponencial')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

if r2_pow != -np.inf:
    plt.subplot(2, 2, 3)
    plt.scatter(x, y, color='black', label='Datos')
    plt.plot(x, y_pred_pow, color='green', label=f'Potencias (R²={r2_pow:.4f})')
    plt.title('Modelo de Potencias')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

if r2_rc != -np.inf:
    plt.subplot(2, 2, 4)
    plt.scatter(x, y, color='black', label='Datos')
    plt.plot(x, y_pred_rc, color='purple', label=f'Razón crecimiento (R²={r2_rc:.4f})')
    plt.title('Modelo de Razón de Crecimiento')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

plt.tight_layout()
plt.show()