import string

texto = input("Introduce el texto del cual deseas saber cuantas mayusculas contiene: ")
mayusculas = 0

for letra in texto:
    if letra in string.ascii_uppercase:
        mayusculas += 1

print("En el texto hay {}, maysculas".format(mayusculas))
