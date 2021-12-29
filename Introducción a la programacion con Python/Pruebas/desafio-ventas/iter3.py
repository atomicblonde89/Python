def filter_dict(diccionario,valor): #Definición de metodo
    diccionario_filtrado = {} #Acesso a listas (nueva)
    return {k:v for k,v in diccionario.items () if v > valor} #Logica 


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