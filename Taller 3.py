# Genera las combinaciones
x=["True","True","True","True","False","False","False","False"]
y=["True","True","False","False","True","True","False","False"]
z=["True","False","True","False","True","False","True","False"]
# Crea una tabla en excel con el nombre de la propiedad
with open("Asociativa.csv","w") as archivo:
    archivo.write("x;y;z;(x v y) v z; (x v y) v (x v z) \n")
    for i in range(len(x)):
        archivo.write(str(x[i])+";"+str(y[i])+";"+str(z[i])+";"+str((x[i] or y[i]) or z[i])+";"+str((x[i] or y[i]) or (x[i] or z[i]))+"\n")
    
    archivo.write("\n")
    
    archivo.write("x;y;z;(x ^ y) ^ z; (x ^ (y ^ z) \n")
    for i in range(len(x)):
        archivo.write(str(x[i])+";"+str(y[i])+";"+str(z[i])+";"+str((x[i] and y[i]) and z[i])+";"+str((x[i] and (y[i] and z[i]))+"\n"))
# Crea una tabla en excel con el nombre de la propiedad
with open("Conmutativa.csv","w") as archivo:
    archivo.write("x;y;z;x v y;y v x\n")
    for i in range(len(x)):
        archivo.write(str(x[i])+";"+str(y[i])+";"+str(z[i])+";"+str(x[i] or y[i])+";"+str(y[i] or x[i])+"\n")
    
    archivo.write("\n")

    archivo.write("x;y;z;x ^ y;y ^ x\n")
    for i in range(len(x)):
        archivo.write(str(x[i])+";"+str(y[i])+";"+str(z[i])+";"+str(x[i] and y[i])+";"+str(y[i] and x[i])+"\n")
# Crea una tabla en excel con el nombre de la propiedad
with open("Distributiva.csv","w") as archivo:
    archivo.write("x;y;z;x ^ (y v z);(x ^ y) v (x ^ z)\n")
    for i in range(len(x)):
        archivo.write(str(x[i])+";"+str(y[i])+";"+str(z[i])+";"+str(x[i] and (y[i] or z[i])+";"+str((x[i] and y[i]) or (x[i] and z[i]))+"\n"))
    
    archivo.write("\n")

    archivo.write("x;y;z;x v (y ^ z); (x v y) ^ (x v z)\n")
    for i in range(len(x)):
        archivo.write(str(x[i])+";"+str(y[i])+";"+str(z[i])+";"+str(x[i] or (y[i] and z[i]))+";"+str((x[i] or y[i]) and (x[i] or z[i]))+"\n")
# Crea una tabla en excel con el nombre de la propiedad
with open("Identidad.csv","w") as archivo:
    archivo.write("x;y;z;x ^ False\n")
    for i in range(len(x)):
        archivo.write(str(x[i])+";"+str(y[i])+";"+str(z[i])+";"+str(x[i] and False)+"\n")
    
    archivo.write("\n")

    archivo.write("x;y;z;x ^ True\n")
    for i in range(len(x)):
        archivo.write(str(x[i])+";"+str(y[i])+";"+str(z[i])+";"+str(x[i] and True)+";"+str(x[i] and False)+"\n")
# Crea una tabla en excel con el nombre de la propiedad
with open("Complementos.csv","w") as archivo:
    archivo.write("x;y;z;x v ~x\n")
    for i in range(len(x)):
        archivo.write(str(x[i])+";"+str(y[i])+";"+str(z[i])+";"+str(x[i] or not x[i])+";"+str(x[i] or not x[i])+"\n")
    
    archivo.write("\n")
    archivo.write("x;y;z;x ^ ~x\n")
    for i in range(len(x)):
        archivo.write(str(x[i])+";"+str(y[i])+";"+str(z[i])+";"+str(x[i] and not x[i])+";"+str(x[i] and not x[i])+"\n")