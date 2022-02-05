bienvenida = "Bienvenido al test mi hermano marimwano"
print("\n" + "-" * len(bienvenida) + "\n" + bienvenida + "\n" + "-" * len(bienvenida) + "\n")

puntuacion = 0

#Si empezamos un string con 3" eso le indica a python que será un string multilinea, la cual respetara
# enters (saltos de linea) y espoacios
res = input("""¿Cuantas veces fumas a la semana?
A.- 0 carnicero krnlin
B.- 2 a 5 veces
C.- 420 *6*
""")#Notar como dejamos espacio en blanco para que la respuesta se muestr abajo, de esta forma no usamos el \n

#Esta es la forma más rudimentaria de hacerlo, funciona pero no es tan optimo ya que aúnque encuentre el caso al que
# pertenece sigue comprobando las demas opciones, lo cual en este caso no es necesario
if res == 'A':
    puntuacion += 0
if res == "B":
    puntuacion += 5
if res == "C":
    puntuacion += 10
if res != "A" and res != "B" and res != "C":
    print("Krnalito ya no fumes, ingresaste alguna mamada las opciones solo son A, B o C")
    exit()


#Tambien podemos imprimir con saltos de linea de esta forma(\n) y respetando que el input éste tódo en una sola linea
res = input("Estas en una fiesta chila, ¿Te das sativa o indica?\nA.- Pura chelita\nB.- La que caiga krnal, más culera la que no, hay venganos tu reino\nC.- Sativa\n")

#Esta es la forma más eficiente ya que el elif nos permite que solo se compruebe hasta que se cumpla alguna condición
# en cuanto se cumpla alguna condición salta hasta despues de los elif o en su caso despues del else
# Siempre necesitan un if para que existan elif y else
if res == "A":
    puntuacion += 0
elif res == "B":
    puntuacion += 5
elif res == "C":
    puntuacion += 10
else:
    print("Krnalito ya no fumes ingresaste alguna mamada las opciones solo son A, B o C")
    exit()


#Esta opción nos permite crar un "bloque" visual de codigo que nos facilita la lectura
res = input("En que prefieres fumar\n"
      "A.- Hiter/Tapa de pluma\n"
      "B.- Bong/Pipa\n"
      "C.- Porro/Hooka\n")

if res == "A":
    puntuacion += 0
elif res == "B":
    puntuacion += 5
elif res == "C":
    puntuacion += 10
else:
    print("Krnalito ya no fumes ingresaste alguna mamada las opciones solo son A, B o C")
    exit()

# por ejemplo en este caso si es necesario un elif, ya que si ponemos en lugar de un if y elif 2 if, al obtener una
# puntuacion de 30 se cumplirian ambas condiciones y nos mostraría los 2 resultados en cambio con el elif en cuanto se
# cumpla una condición deja de comprobar las demas, asi obtenemos solo un resultado, es decir el orden importa
if puntuacion >= 25:
    print("Felicidades, eres un marimbuano de cultura, tu sabes lo que haces y te informas para pasar un buen rato "
          "tu puntuación son: {} ptos" .format(puntuacion))
elif puntuacion >= 15:
        print("Puedes tener mejores habitos, no dejes de fumar por una palida informate más y aprende sobre esta chit "
              "tu puntuacion son: {} ptos" .format(puntuacion))
else:
    print("Abre tu mente hermano hay drogas más dañinas que consumes a diario vrvrvrro "
          "tu puntuacion son: {} ptos" .format(puntuacion))