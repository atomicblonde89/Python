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

quarters = {"Q1":[], "Q2":[], "Q3": [], "Q4":[]} 
q1 = ["Enero", "Febrero", "Marzo"]
q2 = ["Abril", "Mayo", "Junio"] 
q3 = ["Julio", "Agosto", "Septiembre"]
q4 = ["Octubre", "Noviembre", "Diciembre"]

for i in ventas:
    if i in q1:
        quarters["Q1"].append(ventas[i])
    elif i in q2:
        quarters["Q2"].append(ventas[i])
    elif i in q3:
        quarters["Q3"].append(ventas[i])
    elif i in q4:
        quarters["Q4"].append(ventas[i])