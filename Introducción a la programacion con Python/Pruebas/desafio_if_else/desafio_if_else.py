import sys

password = str(sys.argv[1])

if len(password)<6: 
    print("Atención, password muy corta!!\n")
elif password == "12345": 
    print("password incorrecto\n")
else: 
    print("password {} ingresado satisfactoriamente".format(password))
