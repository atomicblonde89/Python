import sys # Librería Sys para argumentos (Argv)
from random import randint as rd # Librería de random para radint llamada rd


# Entradas: 
opciones = ["piedra","papel","tijera"] #Lista de opciones de Jankenpon 
usuario = (sys.argv [1])

# Condicional de argumento invalido :
if sys.argv[1] not in opciones:
     print("Debe ser piedra, papel o tijera.")
else: 
	usuario = (sys.argv[1])
	computador = rd(0,2)
	print("Computador juega:", opciones[computador])
	computador_versus = opciones[computador]

# Logica y salida de funcionamiento
	if usuario == "tijera" and computador_versus == "papel": 
         print("Ganaste")
	elif usuario == "papel" and computador_versus == "piedra":
         print("Ganaste")
	elif usuario == "piedra" and computador_versus == "tijera": 
         print("Ganaste")
	elif usuario == computador_versus:
         print("Empataste")
	else: 
         print("Perdiste")

