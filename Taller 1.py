import random

Conjunto1=set()
Conjunto2=set()


print("Bienvenido")
print("Antes de continuar, ingresa la cantidad de elementos que quieres en los conjuntos")
n=int(input("Ingrese la cantidad de elementos para el conjunto 1: "))
n2=int(input("Ingrese la cantidad de elementos para el conjunto 2: "))
for i in range(n):
    Conjunto1.add(random.randint(0,30))
for i in range(n2):
    Conjunto2.add(random.randint(0,30))
print("Conjuntos Generados con Exito!")

print("Conjunto 1: ", Conjunto1)
print("Conjunto 2: ", Conjunto2)
print("Conjunto Unido: ", Conjunto1.union(Conjunto2))
print("Conjunto Interseccion: ", Conjunto1.intersection(Conjunto2))
print("Conjunto 1 - 2: ", Conjunto1.difference(Conjunto2))
print("Conjunto 2 - 1: ", Conjunto2.difference(Conjunto1))
print("Conjunto 1: ", Conjunto1.symmetric_difference(Conjunto2))
print("Gracias por utilizar el programa")
