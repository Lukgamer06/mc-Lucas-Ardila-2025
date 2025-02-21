opcion=0

def Combinacion(n,r):
    fac_n=1
    fac_r=1
    fac_nr=1
    #Calcular n
    for i in range(1,n+1):
        fac_n*=i
    #Calcular r
    for i in range(1,r+1):
        fac_r*=i
    #Calcular nr
    for i in range(1,(n-r)+1):
        fac_nr*=i
    
    return fac_n/(fac_r*fac_nr)

while True:
    print(
        "Bienvenido\n"
        "Que Ejercicio del taller quieres ver?\n",
        "1. Ejercicio 1\n",
        "2. Ejercicio 2\n",
        "3. Salir\n"
    )
    try: opcion=int(input("Opcion: "))
    except ValueError: print("Error: Debes ingresar un numero entero"); continue
    if opcion==1:
        print("Ayer deje mi telefono celular olvidado en el autobus, por lo que lo reemplace rapidamente por un telefono con menor capacidad de memoria. En mi telefono anterior tenia instaladas 20 aplicaciones y ahora solamente puedo seleccionar 8")
                
        print("a) De cuantas formas puedo realizar esta seleccion?")
        print("Rta: ", Combinacion(20,8))

        print("b) Si deseo mantener instaladas 3 de las 6 aplicaciones de redes sociales que tenia y otras 5 aplicaciones de las 14 restantes, de cuantas formas puedo seleccionar ahora?")
        print("Rta: ",Combinacion(6,3)*Combinacion(14,5))
        input()
    elif opcion==2:
        print("Una baraja comun de 52 cartas consiste en cuatro palos (treboles, diamantes, corazones y espadas) con 13 denominaciones cada uno (as, de 2 a 10, jack [J], reina [Q] y rey [K]).")
                
        print("a) Cuantas manos de poquer (sin ordenar) de cinco cartas, seleccionadas de una baraja comun de 52 cartas, existen?")
        print("Rta: ",Combinacion(52,5))

        print("b) Cuantas manos de poquer contienen cartas todas del mismo palo?")
        print("Rta: ", 4*(Combinacion(13,5)))

        print("c) Cuantas manos de poquer contienen tres cartas de una denominacion y dos de una segunda denominacion?")
        print("Rta: ", Combinacion(13,1)*Combinacion(4,3)*Combinacion(12,1)*Combinacion(4,2))
        input()
    elif opcion==3:
        print("Gracias por utilizar el programa")
        input()
        break
    else:
        print("Selecciona una opcion")