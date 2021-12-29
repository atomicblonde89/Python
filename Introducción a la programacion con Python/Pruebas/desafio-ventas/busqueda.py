import sys # Librería para trabajar en terminal

#Diccionario para ventas
ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

bit_memoria = 0 #Variable de apoyo
for i in sys.argv[1:]: #Condición para entrada
    for k,v in ventas.items ():
        if v == int(i): #
            print(k)
            bit_memoria = True
            break
        else:
           bit_memoria = False
        if bit_memoria == False:
              print("No encontrado") #Se repite por sobre lo establecido :(