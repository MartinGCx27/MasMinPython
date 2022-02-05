Texto = "Bienvenido al text de otakus"
print("\n" + Texto + "\n" + "-" * len(Texto) + "\n")
puntuacion = 0
p1 = input("Cuantas veces te bañas a la semana \n"
           "A) De 4 de 7\n"
           "B) De 2 a 3\n"
           "C) Solo 1 o 2\n")
if p1 == "A":
    puntuacion += 0
elif p1 == "B":
    puntuacion += 5
elif p1 == "C":
    puntuacion += 10
else:
    print("Ponlo bien ctm\n")
    exit()
p2 = input("Te sabes el final de Evangelion\n"
           "A) Si\n"
           "B) No\n"
           "C) ¿Que es eso?, se come\n")
if p2 == "A":
    puntuacion += 10
elif p2 == "B":
    puntuacion += 5
elif p2 == "C":
    puntuacion += 0
else:
    print("Ponlo bien we\n")
    exit()
p3 = input("Ves anime subtitulado o doblado?\n"
           "A) Subtitulado que no se japones\n"
           "B) A mi me gusta doblado\n"
           "C) Sin subtitulos y en japones aunque no entienda nada\n")
if p3 == "A":
    puntuacion += 5
elif p3 == "B":
    puntuacion += 0
elif p3 == "C":
    puntuacion += 10
else:
    print("Ponlo bien boludo\n")
    exit()
if puntuacion <= 30 and puntuacion >= 21:
    print("Eres muy otaku y te bañas muy poco, te recomiendo un baño,"
          " su puntuacion fue: {}".format(puntuacion))
if puntuacion <= 20 and puntuacion >= 11:
    print("Eres un poser te recomiendo dejar de publicar tu vida en las redes,"
          " su puntuacion fue: {}".format(puntuacion))
if puntuacion <= 10 and puntuacion >= 0:
    print("Eres muy amateur ponte a ver one piece y no mueras en el intento,"
          " su puntuacion fue: {}".format(puntuacion))
