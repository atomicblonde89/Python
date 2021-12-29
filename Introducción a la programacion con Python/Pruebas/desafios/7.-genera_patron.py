numero = int(input("Ingrese número: \n"))
patron = ""

for i in range (numero):
    for j in range (i+1):
        patron += str (j+1)
    patron += "\n"

print (patron)