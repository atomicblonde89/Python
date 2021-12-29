numero = int(input("Ingresé número: \n"))
suma = 0
iteraciones = ""

for i in range (1,numero+1):
    if i% 2 == 0:
        suma += i
print (suma)
