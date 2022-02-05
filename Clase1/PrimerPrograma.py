Num1 = int(input("Captura el primer número: "))
Num2 = int(input("Captura el segundo número: "))
Num3 = int(input("Captura el tercer número: "))

print("El número más grande es: ", max(Num1, Num2, Num3))
print("El número más chico es: ", min(Num1, Num2, Num3))


print("El número más grande es: {}".format(max(Num1, Num2, Num3)))
print("El número más chico es: {}".format(min(Num1, Num2, Num3)))

#En python la convección es que las lineas de código no excedan los 120 caracteres
print("El número más grande entre {}, {} y {} es {} y el más chico es {}".format(Num1, Num2, Num3,
                                                                                 max(Num1, Num2, Num3),
                                                                                 min(Num1, Num2, Num3)))
