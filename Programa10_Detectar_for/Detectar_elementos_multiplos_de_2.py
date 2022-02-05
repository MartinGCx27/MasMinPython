numero = int(input("De que número quieres la tabla: "))

for i in range(1, 11):
    if i % 2 == 0:
        print("{} X {} = {}".format(numero, i, i * numero))