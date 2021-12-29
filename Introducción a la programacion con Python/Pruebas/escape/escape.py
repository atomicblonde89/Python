import math as mt
import sys

gravedad = float(sys.argv[1]) # as mts/s*2
radio = int(sys.argv[2])*1000 # Radio as kms to m/s
velocidad_escape = round(mt.sqrt(2*(gravedad*radio)), 1)  #Ecuación de Vel escape 

print("La velocidad de escape es: {}  m/s".format(velocidad_escape))