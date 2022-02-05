bienvenida = "Bienvenido a la lista de la compra"
print("\n" + "*" * len(bienvenida) + "\n" + bienvenida + "\n" + "*" * len(bienvenida) + "\n")

producto = None
confirmacion = None
lista_compra = []

while producto != "Q":
    producto = input("¿Que desea comprar? ([Q] para salir)")
    if producto == "Q":
        pass
    elif producto in lista_compra:
        print("{} ya esta en la lista!".format(producto))
    else:  #La forma de abajo de 2 lineas es una manera pero tambien se puede reducir a una sola lina como se muestra
        """confirmacion = input("Seguro que desea agregar {}? [S]/[N]".format(producto))
           if confirmacion == "S":"""
        if input("Seguro que desea agregar {}? [S]/[N]".format(producto)) == "S":
            lista_compra.append(producto)
            print("{} añadido!".format(producto))

print("\nLa lista de la compra es: {}".format(lista_compra))
