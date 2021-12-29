# Importación de librerias, *incluida numpy
import pandas as pd

df = pd.read_csv('athlete_events.csv') #Lectura de archivo csv

subset = df.loc[:, ["Name","Team", "Year", "Medal", "Sex"]].fillna(0)

#Requerimiento n°1
subset2 = subset[subset["Medal"] == "Gold" ].loc[:, ["Name", "Medal", "Team", "Sex"]] #Ganadores de Oro
subset3 = subset[subset["Medal"] == "Silver" ].loc[:, ["Name", "Medal", "Team", "Sex"]] # Ganadores de Plata
subset4 = subset[subset["Medal"] == "Bronze" ].loc[:, ["Name", "Medal", "Team", "Sex"]] # Ganadores de Bronce
subset5 = subset[subset["Medal"] == 0 ].loc[:, ["Name", "Medal", "Team", "Sex"]] # Atletas sin medallas

#Requerimiento n°2
subset['Female'] = ["1" if s == "F" else "0" for s in subset['Sex']]
print(subset)

#Requerimiento n°3

#Mayor cantidad Gold
subset6 = subset2["Team"].value_counts().head(10)
print("#Mayor cantidad Gold:")
print(subset6)
print("\n")

#Mayor cantidad Silver
subset7 = subset3["Team"].value_counts().head(10)
print("#Mayor cantidad Silver:")
print(subset7)
print("\n")

#Mayor cantidad Bronze
subset8 = subset4["Team"].value_counts().head(10)
print("#Mayor cantidad Bronze:")
print(subset8)
print("\n")

#Mayor cantidad Sin Medalla
subset9 = subset5["Team"].value_counts().head(10)
print("#Mayor cantidad SinMedalla:")
print(subset9)
print("\n")

#Requerimiento n°4

#Cantidad por genero Gold
subset10 = subset2["Sex"].value_counts().head(10)
print("#Cantidad x genero Gold:")
print(subset10)
print("\n")

#Cantidad por genero Silver
subset11 = subset3["Sex"].value_counts().head(10)
print("#Cantidad x genero Silver:")
print(subset11)
print("\n")

#Cantidad por genero Bronze
subset12 = subset4["Sex"].value_counts().head(10)
print("#Cantidad x genero Bronze:")
print(subset12)
print("\n")

#Cantidad por genero sin Medalla
subset13 = subset5["Sex"].value_counts().head(10)
print("#Cantidad x genero SinMedalla:")
print(subset13)
print("\n")

#Requerimiento n°5

def media(df, analyze, gender): #Definición de "media" para reportar medias entre hombres y mujeres en columna
    subset14 = df.loc[:, [analyze, "Sex"]]
    subset15 = subset14[subset14["Sex"] == gender].value_counts().mean()
    subset16 = subset14[subset14["Sex"] != gender].value_counts().mean()
    media = (int(subset15) + int(subset16))/2
    print("La media entre Hombres y mujeres en "+str(analyze)+" es "+str(media))

media(subset,"Team", "F") #Función "media"

#Requerimiento n°6

subset17 = df.loc[:, ["Height", "Weight"]]
subset18 = subset17["Height"].mean()
subset19 = subset17["Weight"].mean()
print("La media de columna Height es: "+str(subset18))
print("La media de columna Weight es: "+str(subset19))