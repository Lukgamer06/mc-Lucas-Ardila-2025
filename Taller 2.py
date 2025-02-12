from random import randint

U = set()
A = set()
#Generamos el Conjunto Universal
def Gen_Conj_Univ(Tam):
    x=0
    while x<Tam:
        num = randint(0,100)
        if num not in U:
            U.add(num)
            x+=1
#Generamos el Conjunto A, Verificando que sea un subconjunto de U
def Gen_SubConj_A(Tam,U):
    x=0
    while x<Tam:
        num = randint(0,100)
        if num not in A and num in U:
            A.add(num)
            x+=1

#Programa
print("Bienvenido")
#Solicita Cardialidad del conjunto Universal
x=int(input("Ingrese la cardinalidad del conjunto universal: "))
Gen_Conj_Univ(x)
#Solicita la cardinalidad del conjunto A
while True:
    try: y=int(input("Ingrese la cardinalidad del conjunto A: "))
    except ValueError:
        print("Error, ingrese un número entero")
        continue

    if y<x:
        Gen_SubConj_A(y,U)
        break
    else:
        print("La cardinalidad del conjunto A no puede ser mayor o igual a la del conjunto universal")

print ("Conjunto Universal: ",end="")
print(U)
print ("Conjunto A: ",end="")
print(A)

print("")

print("(U ∩ A ) ∪ A = ", end="")
print(U.intersection(A).union(A))
print("(U - A) ∩ A = ", end="") 
if U.difference(A).intersection(A) == set():
    print("{∅}")
print("(U ⨁ A) - A = ", end="")
print (U.symmetric_difference(A).difference(A))