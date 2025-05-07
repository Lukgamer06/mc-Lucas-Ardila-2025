def suma_cuadrados(x, y):
    return sum((xi - y_mean(y)) ** 2 for xi in y)

def suma_cuadrados_residuos(y, y_pred):
    return sum((yi - y_pred_i) ** 2 for yi, y_pred_i in zip(y, y_pred))

def y_mean(y):
    return sum(y) / len(y)

def coeficiente_determinacion(y, y_pred):
    ss_tot = suma_cuadrados(y, y)
    ss_res = suma_cuadrados_residuos(y, y_pred)
    return 1 - (ss_res / ss_tot) if ss_tot != 0 else 0

def calcular_coeficientes(x, y, grado):
    n = len(x)
    coeficientes = [0] * (grado + 1)
    
    for i in range(grado + 1):
        coeficientes[i] = sum(x[j] ** i * y[j] for j in range(n)) / n
    
    return coeficientes

def evaluar_polinomio(coeficientes, x):
    return sum(coeficientes[i] * (x ** i) for i in range(len(coeficientes)))