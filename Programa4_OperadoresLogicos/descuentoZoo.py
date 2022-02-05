edad = int(input("Dime tu edad: "))
tipo_de_carnet = input("Digame su tipo de carnet (E para Estudiante / P Pensionista / F Familia numerosa / N Nada): ")
  # (edad < 35 and edad > 25)   <--- Esa sería la forma larga (y antigua) de escribir las primeras 2 condiciones
if (25 >= edad <= 35 and tipo_de_carnet == "E") \
    or edad < 10 or \
    (edad >= 65 and tipo_de_carnet == "P") or \
    (tipo_de_carnet == "F"):
    # La separación del código se hace en los "or"
    print("Se te aplica descuento")
else:
    print("No se te aplica descuen to")
