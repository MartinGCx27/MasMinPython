numero = int(input("De que número quieres la tabla: "))

for i in range(1, 11):
    print("{} X {} = {}".format(numero, i, i * numero))
