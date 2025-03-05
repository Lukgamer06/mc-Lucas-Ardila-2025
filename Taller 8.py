import math

# Saber si la entrada es un numero base 8
def valido(num):
    try:
        int(num, 8)
    except ValueError:
        return False
    except TypeError:
        return False
    return True


def base16(num):
    if num == 0:
        return "0"
    dig_hex = "0123456789ABCDEF"
    res = ""
    while num > 0:
        res = dig_hex[num % 16] + res  
        num //= 16
    return res


def base8(num, valido):
    num = int(num)
    if valido:
        if num == 0:
            return "0"
        a=list()
        while num:
            a.append(int(num % 8))
            num //= 8
        a.reverse()
        return ''.join(map(str, a))
    else:
        return "Numero invalido"

while True:
    print("Bienvenido")
    print("1. Convertir de base 10 a base 16")
    print("2. Convertir de base 8 a base 10")
    print("3. Salir")
    try:
        op = int(input("Ingresa una opcion: "))
    except ValueError:
        print("Error, ingresa un valor numerico")
        continue
    if op == 1:
        num = int(input("Inserta un numero: ")) 
        print(base16(num))
    elif op == 2:
        num = input("Inserta un numero: ") 
        print(base8(num, valido(num)))
    elif op == 3:
        break
    else:
        print("Error, ingresa una opcion correcta")
