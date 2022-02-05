print("Voy a la cocina")
print("Abro el refri")

hay_leche = input("¿Hay leche? (S/N)")
hay_colacao = input("¿Hay colacao? (S/N)")

if hay_leche != "S" or hay_colacao != "S":
    print("Voy al gualmart")
    if hay_leche != "S":
        print("Compro leche")
    if hay_colacao != "S":
        print("Compro culoprestas")

print("Ponemos el culoprestas en el vaso")
print("Vaciamos leche en el vaso")
print("Mezclamos")
