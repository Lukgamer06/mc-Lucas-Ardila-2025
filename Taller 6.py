from math import cos,pi,factorial

def ErrorAproximado(aproxAct,aproxAnt):
    return abs((aproxAct-aproxAnt)/aproxAct)*100 

#Solicita el valor de la variable 
a=input("Ingresa un valor en radianes: ")

#Analizar que la palabra "pi" esta dentro de la cadena a
if "pi" in a.lower():
    #Si la palabra "pi" esta dentro de la cadena a, reemplazarla por su valor 
    a = a.replace("pi", str(pi))

#Pasar la cadena a a float
try:
    a = float(eval(a))  # Use float to safely convert the input
except Exception as e:
    print("Error: ", e)
    a = None  # Si no funciona, el valor de a sera None

# Inicializar los valores
cos_valor_ACT = 1
i = 1
ea = 100.0  # Estos valores no valen realmente, es solo para que el while funcione
es = 5 * (10 ** -8) * 100 # Error esperado para 8 decimales

while ea >= es:
    cos_valor_ANT = cos_valor_ACT
    cos_valor_ACT += ((1-1) ** i) * (a ** (2 * i)) / factorial(2 * i)
    ea = ErrorAproximado(cos_valor_ACT, cos_valor_ANT)
    print(cos_valor_ACT)
    print(ea)
    i += 1
print(a)

Et = (ea / (cos(a))) * 100

print(f"El valor estimado es: {round(cos_valor_ACT, 8)}")
print(f"El error aproximado porcentual es: {round(Et, 8)}%")
print(f"El numero de iteraciones realizadas fue: {i}")
