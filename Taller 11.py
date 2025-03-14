import math

# Definir la función
def f(x):
    return 0.25 * x**4 - 0.75 * x**2 + 4.5

# Definir la derivada exacta de la función
def f_prima(x):
    return x**3 - 1.5 * x

# Definir la segunda derivada exacta de la función
def f_segunda_prima(x):
    return 3 * x**2 - 1.5

# Punto donde se calcularán las derivadas
x = 0.6

# Tamaño del paso
h1 = 0.1
h2 = 0.05

# Función para calcular diferencias finitas
def diferencia_adelante(f, x, h):
    return (f(x + h) - f(x)) / h

def diferencia_atras(f, x, h):
    return (f(x) - f(x - h)) / h

def diferencia_centrada(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def segunda_diferencia_adelante(f, x, h):
    return (f(x + 2*h) - 2*f(x + h) + f(x)) / h**2

def segunda_diferencia_atras(f, x, h):
    return (f(x) - 2*f(x - h) + f(x - 2*h)) / h**2

def segunda_diferencia_centrada(f, x, h):
    return (f(x + h) - 2*f(x) + f(x - h)) / h**2

# Calcular las aproximaciones para h = 0.1
da_prima_h1 = diferencia_adelante(f, x, h1)
dat_prima_h1 = diferencia_atras(f, x, h1)
dc_prima_h1 = diferencia_centrada(f, x, h1)

da_segunda_h1 = segunda_diferencia_adelante(f, x, h1)
dat_segunda_h1 = segunda_diferencia_atras(f, x, h1)
dc_segunda_h1 = segunda_diferencia_centrada(f, x, h1)

# Calcular las aproximaciones para h = 0.05
da_prima_h2 = diferencia_adelante(f, x, h2)
dat_prima_h2 = diferencia_atras(f, x, h2)
dc_prima_h2 = diferencia_centrada(f, x, h2)

da_segunda_h2 = segunda_diferencia_adelante(f, x, h2)
dat_segunda_h2 = segunda_diferencia_atras(f, x, h2)
dc_segunda_h2 = segunda_diferencia_centrada(f, x, h2)

# Calcular los valores exactos
prima_exacta = f_prima(x)
segunda_prima_exacta = f_segunda_prima(x)

# Guardar los resultados en un archivo CSV
with open('resultados_derivadas.csv', 'a+') as archivo:
    archivo.write("Método,h,Primera Derivada Aproximada,Segunda Derivada Aproximada,Primera Derivada Exacta,Segunda Derivada Exacta\n")
    
    # Escribir los resultados para h = 0.1
    archivo.write(f"Hacia Adelante,{h1},{da_prima_h1},{da_segunda_h1},{prima_exacta},{segunda_prima_exacta}\n")
    archivo.write(f"Hacia Atrás,{h1},{dat_prima_h1},{dat_segunda_h1},{prima_exacta},{segunda_prima_exacta}\n")
    archivo.write(f"Centrada,{h1},{dc_prima_h1},{dc_segunda_h1},{prima_exacta},{segunda_prima_exacta}\n")
    
    # Escribir los resultados para h = 0.05
    archivo.write(f"Hacia Adelante,{h2},{da_prima_h2},{da_segunda_h2},{prima_exacta},{segunda_prima_exacta}\n")
    archivo.write(f"Hacia Atrás,{h2},{dat_prima_h2},{dat_segunda_h2},{prima_exacta},{segunda_prima_exacta}\n")
    archivo.write(f"Centrada,{h2},{dc_prima_h2},{dc_segunda_h2},{prima_exacta},{segunda_prima_exacta}\n")

print("Resultados guardados en 'resultados_derivadas.csv'")