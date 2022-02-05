import random

bienvenida = "Bienvenido al magiko jueko mistikooh"
print("\n" + "*" * len(bienvenida) + "\n" + bienvenida + "\n" + "*" * len(bienvenida) + "\n")

print("Al fin conseguiste hacerte con el Enchiridion, en el venía la ubicación exacta de la lanza de longinus\n"
      "la cual conseguiste despues derrotar al terramorfo eridiano, ya en la huida se quedo sin combustible tu\n"
      "motocicleta hyliana, así que te escabuiste en el going merry la nave más cercana para huir de ahi.\n"
      "Ya en el espacio te das cuenta que la nave es de una compañia de cazarrecompenzas y el valor de tu cabeza\n"
      "acaba de alcanzar el top #1 de la galaxia, esperas toda la noche para empezar tu huida, sales por fin del\n"
      "sistema de desague ves 2 habitaciones al final del pasillo una que proyecta una luz verde y otra que tiene\n"
      "que emana un fuerte ruido ¿A donde te dirijes?\n")

res = input("[OPCION (A): Puerta luz verde]\n"
      "[OPCION (B): Puerta fuerte ruido]\n")
if res == "A":
    print("Descubres que la luz verde es un portal interdimensional que esta usando Rick Sanchez para escapar\n"
        "¿Que haces?")
    res = input("[OPCION (A): Entras al portal]\n"
              "[OPCION (B): Sales del cuarto]\n")
    if res == "A":
        print("El portal te lleva a otra dimensión, lograste escapar pero te percatas que vas cayendo directamente\n"
              "a un volcan de LCL, al entrar en contacto con el, mueres en tu forma fisica y te haces uno mismo\n"
              "con el todo, ahora eres parte de la instrumentalización humana OMEDETTO!\n"
              "|FIN|\n")
        exit()
    elif res == "B":
        print("Sales del cuarto y sigues escabullendote entre las sombras, encuentras el diagrama de la nave,\n"
              "notas dos posibles rutas de escape la primera a traves de la capsula de escape de la sala de control\n"
              "y la segunda por la salida de emergencia ¿Por cual decides huir\n")
        res = input("[OPCION (A): Capsula de escape]\n"
              "[OPCION (B): Salida de emergencia]\n")
        if res == "A":
            print("Logras llegar hasta la sala de control, echas un vistazo y ves que esta los 3 pilotos estan\n"
                  "durmiendo, la nave se encuentra en piloto automatico, debes encontrar la capsula de escape\n"
                  "tu...\n")
            res = input("[OPCION (A): Entras a escondidas e investigas la sala de control sin despertar a los pilotos]\n"
                        "[OPCION (B): Aprovechas que los pilotos estan dormidos y amagas a uno para interrogarlo]\n")
            if res == "A":
                print("Haces mucho ruido al tirar la  taza favorita del capitan, te amagan entre todos y te criogenizan.\n"
                      "|FIN|\n")
                exit()
            elif res == "B":
                print("El piloto que interrogas dice ser un fan tuyo y que para llegar a la capsula debes presionar\n"
                      "el botón de despegue 3 veces seguidas.\n"
                      "¿Lo presionaras\n")
                res = input(
                    "[OPCION (A): Sí]\n"
                    "[OPCION (B): No]\n")
                if res == "A":
                    print("Resultó ser veridica la información, se abre la compuerta de la capsula de escape y sales disparado\n"
                          "en ella, ves los anillos de saturno mientras bebes de la dulce copa de la victoria.\n"
                          "|FIN|\n")
                    exit()
                elif res == "B":
                    print("Decides no creerle y lo golpeas para que diga la verdad, el ruido del interrogatorio despierta a\n"
                          "los demas pilotos, te encuentran y te verguean.\n"
                          "|FIN|\n")
                    exit()
                else:
                    print("Krnalito ya no fumes ingresaste alguna mamada las opciones solo son A o B")
                    exit()

            else:
                print("Krnalito ya no fumes ingresaste alguna mamada las opciones solo son A o B")
                exit()

        elif res == "B":
            print("La salida de emergencia siempre se encuentra custodiada, te congelan en carbonita y cobran tu recompensa.\n"
                  "|FIN|\n")
            exit()
        else:
            print("Krnalito ya no fumes ingresaste alguna mamada las opciones solo son A o B")
            exit()
    else:
        print("Krnalito ya no fumes ingresaste alguna mamada las opciones solo son A o B")
        exit()

elif res == "B":
    print("Ves a un tipo creando una nueva especie de pistola de rayos plasmaticos solares, los tubos de fisión que ocupa de\n"
          "cartuchos hacen el ruido que escuchaste, es ruidosa pero podría servirte ¿Quieres tomar el arma?\n")
    res = input(
        "[OPCION (A): Sí]\n"
        "[OPCION (B): No]\n")
    if res == "A":
        arma = True
        print("Te llevas la ruidosa arma, ojala el ruido no te dalate.\n")
    elif res == "B":
        arma = False
        print("No te llevas el arma, te parece muy ruidosa, puede ser lo mejor.\n")
    else:
        print("Krnalito ya no fumes ingresaste alguna mamada las opciones solo son A o B")
        exit()

    num_alea = random.randint(1,100)
    print("Sigues tu camino en busca de la salida, llegas al calabozo de la nave donde tienen a los individuos por los cuales\n"
          "cobraran su recompensa, uno de ellos te asegura que puede ayudarte a llegar a escapar sano y sano de la nave si lo\n"
          "liberas, lo liberas y te dice que antes de colaborar contigo debe hacer una comprobación rápida tipica de su\n"
          "planeta natal, adopata su verdadera forma saliendo desde su ano la cabeza de lo que parece ser un pulpo y formando con las demas extremidades sus tentaculos\n"
          "te pregunta que ¿Cual es el resultado de 27 * {}\n".format(num_alea))
    res = int(input("Ingresa tu respuesta\n"))
    if res == num_alea * 27:
        print("El pulpo te absorbe desde lo que anteriormente era su ano y mueres no sin antes comprobar por el aroma que si lo\n"
              "ocupaba para lo mismo que tu, resulta que no tolera a los cerebritos.\n"
              "|FIN|\n")
        exit()
    elif res != num_alea * 27:
        print("Orgalorg te muestra un mapa donde indica que la capsula de escape se encuentra en el centro de mando, memorizas la ruta más rápida\n"
              "y se separan, él ira a buscar venganza de quien lo atrapo. Tu subes al ducto de ventilación para pasar desapercibido pero\n"
              "despues de algunos minutos caes al centro de reciclaje gracias a un tornillo suelto en el ducto, dentro del centro de reciclaje\n"
              "encuentras los unicos horarios de apertura de puertas tu...\n")
        res = input(
            "[OPCION (A): Esperas pacientemente hasta que lo abran para huir]\n"
            "[OPCION (B): Forzar la puerta]\n")
        if res == "A:":
            print("Te enteras por qué solo abren a ciertas horas el centro de reciclaje, de la oscuridad comienzan a salir\n"
                  "skags tragabasura, disparas un par de veces pero es una plaga entera te comen hasta las entrañas.\n"
                  "|FIN|\n")
            exit()
        elif res == "B" and arma: #Aqui no es necesario pone el == True ya que es booleano, y python reconoce en automatico que nos referimos a la variable en positivo
            print("Tomas la pistola que tomaste antes y disparas a la puerta y descubres que funciona perfectamente para perforar las puertas\n"
                  "y paredes de la nave llegas a la habitacipon justo encima de la capsula de escape y disparas al suelo, caes justo enfrente\n"
                  "de la capsula de escape, los pilotos se dan cuenta pero es demasiado tarde, subes y logras escapar en el camino\n"
                  "ves los anillos de saturno mientras bebes de la dulce copa de la victoria.\n"
                  "|FIN|\n")
            exit()
        elif res == "B" and arma == False:
            print("Descubres que las puertas y paredes de la nave son muy delgadas, si tan solo tuvieras algún arma...\n"
                  "Pero no la tienes así que quedas atrapado.\n"
                  "de la oscuridad comienzan a salir skags tragabasura, es una plaga entera te comen hasta las entrañas.\n"
                  "|FIN|\n")
            exit()
        else:
            print("Krnalito ya no fumes ingresaste alguna mamada las opciones solo son A o B")
            exit()
    else:
        print("Krnalito ya no fumes ingresaste alguna mamada las opciones solo son A o B")
        exit()

else:
    print("Krnalito ya no fumes ingresaste alguna mamada las opciones solo son A o B")
    exit()
