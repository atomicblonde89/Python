import sys

# Entradas:
entrada_1 = int(sys.argv[1])
entrada_2 = int(sys.argv[2])
entrada_3 = int(sys.argv[3])

# Salidas con condicionales 
if entrada_1 > entrada_2 and entrada_1 > entrada_3:
    print(entrada_1)
elif entrada_2 > entrada_3:
    print(entrada_2)
else:
    print(entrada_3)
