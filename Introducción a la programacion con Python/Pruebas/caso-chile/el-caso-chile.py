import pandas as pd # Importación librerias Panda

df = pd.read_csv("athlete_events.csv") # Lectura de archivo CSV

subset = df.loc[:,["Name", "Team", "Year", "Medal"]] # Declaración de columnas y lineas
subset2 = subset[subset["Team"] == ["Chile"]]

subset3 = subset2["Year"].value_counts().head(1) #Año de la participación más alta
print("El año con más participación fué: ")
print("Año Cantidad")
print(subset3)
print("\n")

subset4 = subset2[subset2["Medal"] != "NaN"].dropna().loc[:,["Name", "Medal"]] # Ganadores de medallas
print("Nombres de los ganadores Chilenos de medallas:")
print(subset4)
print("\n")

subset5 = subset2[subset2["Medal"] != "NaN"].dropna().loc[:,["Year", "Medal"]].value_counts().head(1) #Año con más medallas
print("Año con más medallas ganadas por Chile:")
print(subset5)