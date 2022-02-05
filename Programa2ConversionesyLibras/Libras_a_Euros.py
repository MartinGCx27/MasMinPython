dolar_euro = 0.83
libra_euro = 1.17

opcion = input("Ingresa la opcion de la conversión que quieres realizar:\n"
               "A.- Dolar a euro\n"
               "B.- Euro a dolar\n"
               "C.- Libra a euro\n"
               "D.- Euro a libra\n")
texto = "Ingresa cuantos {} quieres y te dire a cuantos {} equivale\n"
if opcion == "A":
    dolar = float(input("Ingresa cuantos dolares quieres y te dire a cuantos Euros equivale\n"))
    print("Para obtener {} Dolares, debes pagar {} Euros".format(dolar, round(dolar*dolar_euro, 2)))
elif opcion == "B":
    #Esta es otra opción para no repetir el mismo texto en todas podemos guardarlo en una variable y le pasamos los strings que queramos
    euro = float(input(texto.format("Euros","Dolares")))
    print("Para obtener {} Euros, debes pagar {} Dolares".format(euro, round(euro/dolar_euro, 2)))
elif opcion == "C":
    libra = float(input("Ingresa cuantas Libras quieres y te dire a cuantos Euros equivale\n"))
    print("Para obtener {} Libras, debes pagar {} Euros".format(libra, round(libra*libra_euro, 2)))
elif opcion == "D":
    euro = float(input(texto.format("Euros", "Libras")))
    print("Para obtener {} Euros, debes pagar {} Libras".format(euro, round(euro/libra_euro, 2)))
else:
    print("Por favor introduce una opción valida")

# lib = float(input("Captura la cantidad de Libras que quieres: "))
# tipoCam = float(input("Ingresa el tipo de cambio: "))
# print("Para obtener {} Libras, debes pagar {} Euros".format(lib, lib*tipoCam))