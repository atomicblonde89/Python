import string
vocabulario = string.ascii_letters[:26]

password = str(input("Ingresa contraseña\n"))
intentos = 0
string_pass = ''

for i in password:
	intento = 0
	for k in vocabulario:
		intento += 1
		if i == k:
			string_pass += k
			intentos += intento
			continue
		else:
			continue

print(intentos,"intento(s)")