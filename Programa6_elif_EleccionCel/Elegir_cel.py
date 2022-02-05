bienvenida = "Bienvenido al ayudante de decisión: Comprar celular"
print("\n" + "-" * len(bienvenida) + "\n" + bienvenida + "\n" + "-" * len(bienvenida) + "\n")

os =  input("Quieres que tu telefono tenga IOS o Android?\n"
            "A.- IOS\n"
            "B.- Android\n")
if os == "A":
    dinero = input("¿Tienes dinero?\n"
                   "A.- Sí\n"
                   "B.- No\n")
    if dinero == "A":
        print("Armate el Iphone Ultra Pro Max 24k Rey")
    elif dinero == "B":
        print("Es agarrando uno de segunda manita miji")
    else:
        print("Nomas una cosa tenias que hacer, 1 sola cosa y la cagas, nomas hay A y B, pon una de esa plox")
        exit()
elif os == "B":
    dinero = input("¿Tienes dinero?\n"
                   "A.- Sí\n"
                   "B.- No\n")
    if dinero == "A":
        cam = input("¿Te importa la cámara del cel?\n"
                    "A.- Sí, me importa la cámara\n"
                    "B.- De las 101 cosas que mas riata me valen\n")
        if cam == "A":
            print("Te recomiendo te compres el Google pixel supercámara")
        elif cam == "B":
            print("Tu si le sabes mi vuen, armate un changomi, calidad precio papuh con eso te armabas una PC")
        else:
            print("Nomas una cosa tenias que hacer, 1 sola cosa y la cagas, nomas hay A y B, pon una de esa plox")
            exit()

    elif dinero == "B":
        print("Es agarrando uno chino pero no cochino, que no pase de 3 bolas, pero con las 3 B's")
    else:
        print("Nomas una cosa tenias que hacer, 1 sola cosa y la cagas, nomas hay A y B, pon una de esa plox")
        exit()
else:
     print("Nomas una cosa tenias que hacer, 1 sola cosa y la cagas, nomas hay A y B, pon una de esa plox")
     exit()