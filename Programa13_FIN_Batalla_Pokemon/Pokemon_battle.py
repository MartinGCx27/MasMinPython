import os
import random
import sys

import readchar



def batallaPokemon(dict_pokemons, clave_pkmn):
    from random import randint
    import os

    VIDA_TOTAL_PKM = 40
    VIDA_TOTAL_CHARIZARD = 50

    vida_pkm = VIDA_TOTAL_PKM
    vida_charizard = VIDA_TOTAL_CHARIZARD

    barra_pkm = (vida_pkm / VIDA_TOTAL_PKM)*10
    barra_charizard = (vida_charizard / VIDA_TOTAL_CHARIZARD)*10


    #Mientra alguno de los 2 pkmns tenga vida, se desenvuelve el combate
    while vida_pkm > 0 and vida_charizard > 0:
        #Forma de hacer la barra que a mi se me ocurrio                 Es importante meter las operaciones entre parentesis
        print("\nLa vida de ",clave_pkmn, "es:  [" + "#" * int(barra_pkm) + " " * (10 - int(barra_pkm)) + "] ({}/{})"
            .format(vida_pkm, VIDA_TOTAL_PKM))

        #Forma más optimizada (del curso)
        print("La vida de Charizard es: [{}{}] ({}/{}".format("#" * int(barra_charizard), " " * (10 - int(barra_charizard)),
                                                            vida_charizard, VIDA_TOTAL_CHARIZARD))
        #Turno PKM
        print("\n###Turno ", clave_pkmn, "###")
        ataque_pkmn = randint(0, 3)
    
        print(clave_pkmn, " ataca con ", dict_pokemons[clave_pkmn][ataque_pkmn],"\n")
        vida_charizard -= 10

        if vida_charizard < 0:
            vida_charizard = 0

        if vida_pkm < 0:
            vida_pkm = 0

        barra_charizard = (vida_charizard / VIDA_TOTAL_CHARIZARD) * 10
        print("La vida de Charizard baja a: [{}{}] ({}/{}".format("#" * int(barra_charizard), " " * (10 - int(barra_charizard)),
                                                            vida_charizard, VIDA_TOTAL_CHARIZARD))

        input("Enter para continuar...")
        os.system("cls")
        #os.system("clear")

        if (vida_pkm <= 0 or vida_charizard <= 0) and vida_pkm > vida_charizard:
            print(clave_pkmn, " Gana!")
            exit()

        elif(vida_pkm <= 0 or vida_charizard) <= 0 and vida_pkm < vida_charizard:
            print("Charizard Gana!")
            exit()

        ataque_charizard = None

        #La primera es la forma más optima, implementando la estructura de listas [] sin ser una variable, abajo esta otra forma de hacerlo más primitiva
        while ataque_charizard not in ["S", "A", "M", "N"]: # No ocupamos operadores logicos ya que en automatico entiende que si la operación logica es True se ejecutará y como Ciertamente ataque_charizard no es niguno de la lista procede a ejecutar el código que pregunta
        # while ataque_charizard != "S" and ataque_charizard != "A" and ataque_charizard != "M" and ataque_charizard != "N":
            os.system("cls")
            print("\n###Turno Charizard###")
            ataque_charizard = input("Selecciona el ataque de Charizard:\n"
                                    "[S]ofoco.\n"
                                    "[A]taque ala.\n"
                                    "[M]ovimiento aismico.\n"
                                    "[N]ada\n")
            if ataque_charizard == "S":
                #Sofoco
                print("Charizard ataca con Sofoco")
                vida_pkm -= 12
                barra_pkm = (vida_pkm / VIDA_TOTAL_PKM) * 10

            elif ataque_charizard == "A":
                #Ataque ala
                print("Charizard ataca con Ataque ala")
                vida_pkm -= 10
                barra_pkm = (vida_pkm / VIDA_TOTAL_PKM) * 10

            elif ataque_charizard == "M":
                #Movimiento sismico
                print("Charizard ataca con Movimiento sismico")
                vida_pkm -= 11
                barra_pkm = (vida_pkm / VIDA_TOTAL_PKM) * 10


            elif ataque_charizard == "N":
                print("Charizard no hace nada...")

            else:
                print("Selecciona un ataque valido")

            if vida_charizard < 0:
                vida_charizard = 0

            if vida_pkm < 0:
                vida_pkm = 0

            print("La vida de ", clave_pkmn," baja a:  [" + "#" * int(barra_pkm) + " " * (10 - int(barra_pkm)) +
                "] ({}/{})".format( vida_pkm, VIDA_TOTAL_PKM))
            

            

    if vida_pkm > vida_charizard:
        input("\n",clave_pkmn," Gana!\nPresiona Enter para continuar...\n")

    else:
        input("\n Charizard Gana!\nPresiona Enter para continuar...\n")
    
    os.system("cls")
        #os.system("clear")


#Primero definimos constantes con el nombre de la variable en mayuscula
POS_X = 0
POS_Y = 1

# MAP_WIDTH = 20
# MAP_HEIGHT = 15

NUM_OF_MAP_OBJECTS = 4

#DEFINIMOS (SUBIMOS) LOS OBSTACULOS DEL MAPA.
                        # la diagonal inverdita (backslash) es para que omita el salto de linea
obstacle_definition = """\
###     ########     ####
    ##   #####  ###   ###
#  #####        #       #
    ###             #    
   ######   #  ##     #  
#        #         ##   #
    ##  ###  ####        
   #     #    ##   ###   
####    ###   ##  #     #
#    ##             #####
###      ######    ##    
        #####            
#        #####        ###
     ##   ######         
###      #######    #####\
"""

#DESCOMPONEMOS LOS OBSTACULOS DE UN SOLO STRING A UNO POR CADA FILA (\n)
""" obstacle_difinition = obstacle_difinition.split("\n") #Así solo nos entrega una lista con cada fila como un elemento """
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
# print(type(obstacle_difinition)) #Así nos entrega una lista de listas que contienen una fila de nuestros obstaculos cada una
# print (obstacle_difinition)

#Despues defininimos nuestras variables
my_position = [19, 14]
map_objects = [] #Guarda las posiciones de los entrenadores a enfrentar
died = False
win = False

#Hacemos que el tamaño del mapa este definido por el tamaño de los obstaculos que subamos
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

pokemons_contrincantes = {
    "Lapras": ["Golpe cabeza", "Cascada", "Hidrobomba", "Cola Ferrea"],
    "Gengar": ["Lenguetazo", "Bomba lodo", "Bola Sombra", "Puño dinamico"],
    "Scyther": ["Corte", "Ala de acero", "Tajo aereo", "Tijera X"],
    "Salamance": ["Cola dragon", "Hiperrayo", "Llamarada", "Dragoaliento"]
}

lanzar_batalla = False

# GENERATE MAP OBJECTS ON THE MAP RANDOMLY EVER CONTAINS 4 PIECES
while len(map_objects) < NUM_OF_MAP_OBJECTS:
    new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

    if new_position not in map_objects and new_position != my_position and obstacle_definition[new_position[POS_Y]] [new_position[POS_X]] != "#":
        map_objects.append(new_position)


while not died and not win:
    # DRAW MAP
    #Pinta el borde superior del mapa
    print("+" + "-" * (MAP_WIDTH * 2) + "+")
    #Pinta los bordes en cada columna
    for columns in range(MAP_HEIGHT):
        print("|", end="")
        #Encadenamos el for para que dentro de cada columna pinte los espacios dandole la anchura y haciendo filas
        for rows in range(MAP_WIDTH):
            char_to_draw = "  " #Manda el espacio para que imprima al final (Mapa)
            object_in_cell = None #Reinicializa la variable a cada iteración
    
            for map_object in map_objects: #Ciclo que pinta objetos en el mapa
                if map_object[POS_X] == rows and map_object[POS_Y] == columns:#Revisa si en la posición a pintar hay objeto de acuerdo al arreglo con las coordenadas previamente definidas (map_objects)
                    char_to_draw = " *"#Manda el * para que imprima al final (Objeto)
                    object_in_cell = map_object #Guarda la coordenada actual donde se encontró que va un objeto

                if obstacle_definition[columns][rows] == "#":
                    char_to_draw = " #"

            #Comprobamos si el ciclo esta en nuestras cordenadas para que pinte nuestro caracter y ya no pinte espacio
            if rows == my_position[POS_X] and columns == my_position[POS_Y]:
                char_to_draw = " @" #Manda el arroba para que imprima al final (jugador)

                if object_in_cell: #Si existe valor en objects_in_cell, lo borra de nuestra lista principal map_objects
                    map_objects.remove(object_in_cell)#Cuando pasamos por un objeto nos sobreponemos y lo eliminamos
                    lanzar_batalla = True

            #else:
            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * (MAP_WIDTH * 2) + "+")

    if lanzar_batalla:
        #os.system("clear")
        os.system("cls")
        if len(map_objects) == 3:
            batallaPokemon(pokemons_contrincantes, "Lapras")
        elif len(map_objects) == 2:
            batallaPokemon(pokemons_contrincantes, "Gengar")
        elif len(map_objects) == 1:
            batallaPokemon(pokemons_contrincantes, "Scyther")
        elif len(map_objects) == 0:
            batallaPokemon(pokemons_contrincantes, "Salamance")
        #os.system("clear")
        os.system("cls")

    lanzar_batalla = False
    if len(map_objects) == 0:
        win = True
        print("Felicidades haz Ganado el juego!!!")

    # print("La cola: {}".format(tail))
    # print("Mi posición: {}".format(my_position))

    #MOVEMENT

    # ASK USER WHERE HE WANTS TO MOVE
    #direction = input("¿Donde te quieres mover? [WASD]: ")
                #Libreria para que en automatico lea el caracter que insertamos, sin necesidad de dar al enter
                #solo funciona en el terminal, y nos devuelve lo capturado como byte por eso necesita el .decode

    #direction = readchar.readchar()
    direction = readchar.readchar().decode()
    new_position = None
    if direction == "W":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]
        # tail.insert(0, my_position.copy()) #Agrega una copia de nuestra posición actual a la cola
        # tail = tail[0:tail_length]  # Muestra la cola de acuerdo a cuanto a comido
        # my_position[POS_Y] -= 1
        # my_position[POS_Y] %= MAP_HEIGHT
        # # ESTO NO FUNCIONÓ PORQUE DEJA LA COLA DONDE SE COMIO LA COMIDA: tail.append([my_position[POS_X], my_position[POS_Y]]) #Agrega la coordenada a la cola
        # # if my_position in tail:#Valida a cada movimiento si no nos hemos comido nuestra cola, para en su caso terminar el juego
        # #     sys.exit("G A M E - O V E R"
        # #              "\nMAMAWEBO!")
        # Se quito porque no era la mejor opción repetir la validación 4 veces la corrección esta en la linea 42, 53 y 63
    elif direction == "S":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == "A":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "D":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "Q":
        died = True

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            # my_position[POS_Y] += 1 #Estas 2 lineas ahora se calculan en el new_ppsition de cada movimiento
            # my_position[POS_Y] %= MAP_HEIGHT
            # if my_position in tail:#Valida a cada movimiento si no nos hemos comido nuestra cola, para en su caso terminar el juego
            #     sys.exit("G A M E - O V E R"
            #              "\nMAMAWEBO!")
            my_position = new_position
    #FORMA BASICA QUE SE ME OCURRIO AUNQUE FUNCIONA AUNQUE CAMBIEMOS EL TAMAÑO DEL MAPA
    #SE IMPLEMENTARIA EN LUGAR DE LA OPERACIÓN CON MODULO (my_position[POS_X] %= MAP_WIDTH)
    # if my_position[POS_X] < 0:
    #     my_position[POS_X] = MAP_WIDTH - 1
    # elif my_position[POS_X] > MAP_WIDTH - 1:
    #     my_position[POS_X] = 0
    # elif my_position[POS_Y] < 0:
    #     my_position[POS_Y] = MAP_HEIGHT - 1
    # elif my_position[POS_Y] > MAP_HEIGHT - 1:
    #     my_position[POS_Y] = 0

    os.system("cls")
    #os.system("clear")

if died:
    sys.exit("G A M E - O V E R")
    #print("Has muerto")