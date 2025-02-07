#Importamos la libreria random
import random
#Creamos los conjuntos
Conjunto1=set()
Conjunto2=set()
#Creamos la funcion para crear el primer conjunto
def generar_conjunto1(cant):
    x=0
    while x<cant:
        num=random.randint(0,30)
        for i in range (cant):
            if num in Conjunto1:
                break
        Conjunto1.add(num)
        x+=1
#Creamos la funcion para crear el segundo conjunto
def generar_conjunto2(cant):
    x=0
    while x<cant:
        num=random.randint(0,30)
        for i in range (cant):
            if num in Conjunto1:
                break
        Conjunto2.add(num)
        x+=1
#Le pedimos al usuario la cantidad de elementos que quiere en el conjunto
print("Bienvenido")
print("Antes de continuar, ingresa la cantidad de elementos que quieres en los conjuntos")
n=int(input("Ingrese la cantidad de elementos para el conjunto 1: "))
n2=int(input("Ingrese la cantidad de elementos para el conjunto 2: "))
#Generamos los conjuntos
generar_conjunto1(n)
generar_conjunto2(n2)
print("Conjuntos Generados con Exito!")
#Se realizan todas las operaciones 
print("Conjunto 1: ", Conjunto1)
print("Conjunto 2: ", Conjunto2)
print("Conjunto Unido: ", Conjunto1.union(Conjunto2))
print("Conjunto Interseccion: ", Conjunto1.intersection(Conjunto2))
print("Conjunto 1 - 2: ", Conjunto1.difference(Conjunto2))
print("Conjunto 2 - 1: ", Conjunto2.difference(Conjunto1))
print("Conjunto 1: ", Conjunto1.symmetric_difference(Conjunto2))
print("Gracias por utilizar el programa")
