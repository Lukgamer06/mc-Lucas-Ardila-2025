def calcular_coeficientes(x, y, grado):
    n = len(x)
    # Crear la matriz de Vandermonde
    V = [[x[i] ** j for j in range(grado + 1)] for i in range(n)]
    
    # Calcular los coeficientes usando el método de mínimos cuadrados
    V_transpuesta = [[V[j][i] for j in range(n)] for i in range(grado + 1)]
    V_transpuesta_V = [[sum(V_transpuesta[i][k] * V[k][j] for k in range(n)) for j in range(grado + 1)] for i in range(grado + 1)]
    V_transpuesta_y = [sum(V_transpuesta[i][j] * y[j] for j in range(n)) for i in range(grado + 1)]
    
    # Resolver el sistema de ecuaciones V_transpuesta_V * coeficientes = V_transpuesta_y
    coeficientes = [0] * (grado + 1)
    
    # Método de eliminación de Gauss con manejo de divisiones por cero
    for i in range(grado + 1):
        if V_transpuesta_V[i][i] == 0:
            raise ValueError("División por cero en eliminación de Gauss")
        for j in range(i + 1, grado + 1):
            ratio = V_transpuesta_V[j][i] / V_transpuesta_V[i][i]
            for k in range(i, grado + 1):
                V_transpuesta_V[j][k] -= ratio * V_transpuesta_V[i][k]
            V_transpuesta_y[j] -= ratio * V_transpuesta_y[i]
    
    for i in range(grado, -1, -1):
        coeficientes[i] = V_transpuesta_y[i]
        for j in range(i + 1, grado + 1):
            coeficientes[i] -= V_transpuesta_V[i][j] * coeficientes[j]
        coeficientes[i] /= V_transpuesta_V[i][i]
    
    return coeficientes

def calcular_r_cuadrado(x, y, coeficientes):
    n = len(x)
    y_media = sum(y) / n
    S_t = sum((yi - y_media) ** 2 for yi in y)
    y_pred = [sum(coeficientes[j] * (xi ** j) for j in range(len(coeficientes))) for xi in x]
    S_r = sum((yi - y_pred[i]) ** 2 for i, yi in enumerate(y))
    r_cuadrado = 1 - (S_r / S_t)
    return r_cuadrado

def realizar_regresion(x, y):
    grado = 1
    resultados = []
    
    while True:
        coeficientes = calcular_coeficientes(x, y, grado)
        r_cuadrado = calcular_r_cuadrado(x, y, coeficientes)
        
        resultados.append((grado, coeficientes, r_cuadrado))
        
        if r_cuadrado >= 0.95:
            break
        
        grado += 1
    
    return resultados