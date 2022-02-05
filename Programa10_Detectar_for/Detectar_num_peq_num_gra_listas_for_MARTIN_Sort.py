numero = None
lista_numeros = []

numero = int(input("¿Qué Número desea añadir?"))
lista_numeros.append(numero)
print("{} añadido!".format(numero))
while input("Deseas agregar más números? [S/N] ") == "S":
    numero = int(input("¿Qué Número desea añadir?"))
    lista_numeros.append(numero)
    print("{} añadido!".format(numero))

print("\nLa lista de los números es: {}".format(lista_numeros))
lista_numeros.sort()
print("El número más pequeño es: {}, y el número más grande es: {}".format(lista_numeros[0], lista_numeros[-1]))
