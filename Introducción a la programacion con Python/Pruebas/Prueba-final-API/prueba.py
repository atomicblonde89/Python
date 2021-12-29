#Libreria Json y Requests
import requests
import json

#URL + API Key
url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key=XshBAhMQas0kOAo1uM2njKcz03e1VZG3epbZNSdS"
payload = {}
headers = {}
response = requests.request("GET", url,headers=headers, data=payload)
response = json.loads(response.text)

listado_fotos = response["latest_photos"]

#Ejercicio 1 // Consulta en API en: listado_fotos
update_foto = []
for i in range(25):
    update_foto.append(listado_fotos[i])

#Ejercicio 2 // Requerimientos para listado de foto
url_fotos = []
for j in update_foto:
    url_fotos.append(j["img_src"])

#Ejercicio 3 // Salida para generación de archivo.html
def build_web_page(UrlFotos):
    html = ""
    for k in url_fotos:
        html += "<li><img src=\"{}\" width=550px height=550px></li> \n".format(k)

    with open("nasa_index.html", "w") as f:
        f.write(" <html> \n <head> \n </head> \n <body> \n <ul>") #Creación de nodos html
        f.write(html)
        f.write(" </ul> \n </body> \n </head> \n </html>") #Creación lista html (UL)

build_web_page(url_fotos) #Creación de html