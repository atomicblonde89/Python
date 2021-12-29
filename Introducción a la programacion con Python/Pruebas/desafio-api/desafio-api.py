#Librerías
import requests
import json

#URLS
url = "https://reqres.in/api/users"
url2 = "https://reqres.in/api/users/2"

#Objetos Python a objetos JSON
payload = {}
payload1=json.dumps({"name": "ignacio", "job":"Profesor"}) #Variable para desafio 2
payload2=json.dumps({"name": "morpheus", "resident": "zion"}) #Variable para desafio 3
headers = {}

#Desafio 1 // Adquisición de usuarios
users_data = requests.request("GET", url, headers=headers, data=payload)
print(users_data.text)
print(users_data)
print("\n")

#Desafio 2 // Creación de usuarios
created_user = requests.request("POST", url, headers=headers, data=payload1)
print(created_user.text)
print(created_user)
print("\n")

#Desafio 3 // Actualización de usuarios 
updated_user = requests.request("PUT", url2, headers=headers, data=payload2)
print(updated_user.text)
print(updated_user)
print("\n")

#Desafio 4 // Eliminación de usuarios
deletePepe = requests.request("DELETE", url2, headers=headers, data=payload)
print("DELETE") #Verbo 
print("Código: "+str(deletePepe)) #Response
print("\n")