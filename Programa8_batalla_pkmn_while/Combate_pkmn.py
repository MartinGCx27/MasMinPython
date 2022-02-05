from random import randint
import os

#En Python como las constantes no tienen tanto peso ni definición en sí, la nomenclatura para manejar un valor constante
#es escribir el nombre de la variable en mayusculas.
VIDA_TOTAL_RAYQUAZA = 40
VIDA_TOTAL_CHARIZARD = 80

vida_rayquaza = VIDA_TOTAL_RAYQUAZA
vida_charizard = VIDA_TOTAL_CHARIZARD

barra_rayquaza = (vida_rayquaza / VIDA_TOTAL_RAYQUAZA)*10
barra_charizard = (vida_charizard / VIDA_TOTAL_CHARIZARD)*10


#Mientra alguno de los 2 pkmns tenga vida, se desenvuelve el combate
while vida_rayquaza > 0 and vida_charizard > 0:
    #Forma de hacer la barra que a mi se me ocurrio                 Es importante meter las operaciones entre parentesis
    print("\nLa vida de Rayquaza es:  [" + "#" * int(barra_rayquaza) + " " * (10 - int(barra_rayquaza)) + "] ({}/{})"
          .format(vida_rayquaza, VIDA_TOTAL_RAYQUAZA))

    #Forma más optimizada (del curso)
    print("La vida de Charizard es: [{}{}] ({}/{}".format("#" * int(barra_charizard), " " * (10 - int(barra_charizard)),
                                                          vida_charizard, VIDA_TOTAL_CHARIZARD))
    #Turno Rayquaza
    print("\n###Turno Rayquaza###")
    ataque_rayquaza = randint(1, 2)
    if ataque_rayquaza == 1:
        #Corte aereo
        print("Rayquaza ataca con Corte aereo")
        vida_charizard -= 10

    else:
        # Cola dragon
        print("Rayquaza ataca con Cola dragon")
        vida_charizard -= 11

    if vida_charizard < 0:
        vida_charizard = 0

    if vida_rayquaza < 0:
        vida_rayquaza = 0

    barra_charizard = (vida_charizard / VIDA_TOTAL_CHARIZARD) * 10
    print("La vida de Charizard es: [{}{}] ({}/{}".format("#" * int(barra_charizard), " " * (10 - int(barra_charizard)),
                                                          vida_charizard, VIDA_TOTAL_CHARIZARD))

    input("Enter para continuar...")
    os.system("cls")

    if (vida_rayquaza <= 0 or vida_charizard <= 0) and vida_rayquaza > vida_charizard:
        print("Rayquaza Gana!")
        exit()

    elif(vida_rayquaza <= 0 or vida_charizard) <= 0 and vida_rayquaza < vida_charizard:
        print("Charizard Gana!")
        exit()

    ataque_charizard = None

    #La primera es la forma más optima, implementando la estructura de listas [] sin ser una variable, abajo esta otra forma de hacerlo más primitiva
    while ataque_charizard not in ["S", "A", "M", "N"]: # No ocupamos operadores logicos ya que en automatico entiende que si la operación logica es True se ejecutará y como Ciertamente ataque_charizard no es niguno de la lista procede a ejecutar el código que pregunta
    # while ataque_charizard != "S" and ataque_charizard != "A" and ataque_charizard != "M" and ataque_charizard != "N":
        print("\n###Turno Charizard###")
        ataque_charizard = input("Selecciona el ataque de Charizard:\n"
                                 "[S]ofoco.\n"
                                 "[A]taque ala.\n"
                                 "[M]ovimiento aismico.\n"
                                 "[N]ada\n")
        if ataque_charizard == "S":
            #Sofoco
            print("Charizard ataca con Sofoco")
            vida_rayquaza -= 12
            barra_rayquaza = (vida_rayquaza / VIDA_TOTAL_RAYQUAZA) * 10

        elif ataque_charizard == "A":
            #Ataque ala
            print("Charizard ataca con Ataque ala")
            vida_rayquaza -= 10
            barra_rayquaza = (vida_rayquaza / VIDA_TOTAL_RAYQUAZA) * 10

        elif ataque_charizard == "M":
            #Movimiento sismico
            print("Charizard ataca con Movimiento sismico")
            vida_rayquaza -= 11
            barra_rayquaza = (vida_rayquaza / VIDA_TOTAL_RAYQUAZA) * 10


        elif ataque_charizard == "N":
            print("Charizard no hace nada...")

        else:
            print("Selecciona un ataque valido")

        if vida_charizard < 0:
            vida_charizard = 0

        if vida_rayquaza < 0:
            vida_rayquaza = 0

        print("La vida de Rayquaza es:  [" + "#" * int(barra_rayquaza) + " " * (10 - int(barra_rayquaza)) +
              "] ({}/{})".format(vida_rayquaza, VIDA_TOTAL_RAYQUAZA))



if vida_rayquaza > vida_charizard:
    print("Rayquaza Gana!")
else:
    print("Charizard Gana!")