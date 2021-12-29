import pandas as pd #Librería de Pandas como pd.

df = pd.read_csv("athlete_events.csv") #Lectura de archivo csv

ejercicio_1 = df.shape # Importar la base de datos athlete_events.csv, y reportar filas y columnas.

ejercicio_2 = len(df["Games"].unique()) # Reportar cantidas de competencias se han realizado a lo largo del tiempo.

ejercicio_3 = df["Season"].vale_counts("%") # Reportar el porcentaje (%) de atletas que participaron para juegos de verano e invierno.

verano = df[df["Season"]]==["Summer"]
ejercicio_4 = verano[verano["Year"]] == verano ["Year"].min()["City"].unique() # Informar donde fue la primera celebración de un juego olimpico de verano.

invierno = df[df["Season"]] == ["Winter"]
ejercicio_5 = invierno[invierno["Year"]] == invierno["Year"].min()["City"].unique() # Informar donde la primera celebración de un juego olimpico de invierno.

ejercicio_6 = df["Team"].value_counts().head(10) # Reportar los 10 primeros países con mayor cantidad de atletas participantes a lo largo de los juegos.

ejercicio_7 = df["Medal"].value_counts("%") # Reportar el porcentaje de medallas asignadas

primeros = df[df["Season"] == ["Summer"]]
ejercicio_8 = primeros[primeros["Year"]== primeros["Year"].min()]["Team"].unique() #Reportar cuáles fuerón los países participantes en las primeras olimpiadas de verano 