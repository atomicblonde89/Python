def promedio(lista):
    	suma = 0
	div = len(lista)
	for i in lista:
		     suma += int(i)
	promedioFinal = suma/div

	return(promedioFinal)


#Lista de velocidad
velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,
11, 11, 12, 12, 12, 12, 13, 13,
13, 13, 14, 14, 14, 14, 15, 15,
15, 16, 16, 17, 17, 17, 18, 18,
18, 18, 19, 19, 19, 20, 20, 20,
20, 20, 22, 23, 24, 24, 24, 24, 25]

#Lista de distancia
distancia = [2, 10, 4, 22, 16, 10, 18, 26, 34,
17, 28, 14, 20, 24, 28, 26, 34, 34,
46, 26, 36, 60, 80, 20, 26, 54, 32,
40, 32, 40, 50, 42, 56, 76, 84, 36,
46, 68, 32, 48, 52, 56, 64, 66, 54,
70, 92, 93, 120, 85]

#Ejecución promedios
promedio_velocidad = promedio(velocidad)
promedio_distancia = promedio(distancia)

# Para velocidad bajo el promedio
planteo1 = 0
# Para velocidad bajo el promedio y distancia sobre el promedio.
planteo2 = 0 
# Para velocidad sobre el promedio
planteo3 = 0 
# Para velocidad sobre el promedio y distancia bajo el promedio.
planteo4 = 0 

#Logica
for tuplas_zipeadas in zip(velocidad, distancia):

	  if tuplas_zipeadas[0] < promedio_velocidad:
		       planteo1 += 1
	  if tuplas_zipeadas[0] < promedio_velocidad and tuplas_zipeadas[1] > promedio_distancia:
	 	       planteo2 += 1
	  if tuplas_zipeadas[0] > promedio_velocidad:
	 	       planteo3 += 1
	  if tuplas_zipeadas[0] > promedio_velocidad and tuplas_zipeadas[1] < promedio_distancia:
	 	       planteo4 += 1

#Salidas de planteos
print(planteo1)
print(planteo2)
print(planteo3)
print(planteo4)