gradosFah = float(input("Ingresa los grados fahrenheit: "))
gradosCel = (gradosFah-32)*5/9
#Cuando usamos esta forma automaticamente se inserta 1 espacio antes y despues de la varible insertada
print("Los", gradosFah, "° Fahrenheit equivalen a", gradosCel, "° Celcius")

print("Los {}° Fahrenheit equivalen a {}° Celcius".format(gradosFah, gradosCel))
