texto = input("Introduce el texto del que deseas saber espacios, puntos y comas:")
espacios = 0
puntos = 0
comas = 0

for letra in texto:
    if letra == " ":
        espacios += 1
    elif letra == ".":
        puntos += 1
    elif letra == ",":
        comas += 1

print("Hay {}, espacios y {} puntos y {} comas en el texto".format(espacio, puntos, comas))

