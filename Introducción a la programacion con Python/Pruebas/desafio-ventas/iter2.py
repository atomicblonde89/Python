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

diccionario_filtrado = [] #Acesso a listas
for k,v in ventas.items(): #Iteración de lista
    if v > 45000: #Logica 
        print(k) #Salida / Output de key (meses)
