import string

numeros_introducidos = None #String que recibimos del usuario como cadena de texto
lista_numeros = [] #Lista de elementos ya separados pero siguen siendo strings
lista_numeros_casteados = []

numeros_introducidos = input("Introduce los números que deseas añadir separados por coma: ")
lista_numeros = numeros_introducidos.split(",")

#Esta forma nos implica crear una nueva lista para almacenar los datos convertidos en enteros y es más rudimentaria
# for numero in lista_numeros:
#     lista_numeros_casteados.append(numero) #Itera sobre cada string ya separada, lo conviente en int y lo guarda

#Esta forma aplica un List Comprehension
numeros_introducidos = [int(numero) for numero in lista_numeros]
#Lo que hace esta sentencia es que a cada iteración del for, le va a aplicar el código que se encuentra antes del for
#y  procederá a guardarla en la lista

#Otra forma aún más compacta sería la siguiente donde directamente itera sobre los numeros introducidos, separados por comas
# numeros_introducidos = [int(numero) for numero in numeros_introducidos.split(",")]
#Ahorrandonos así, tambien la creación de otra lista

numero_pequeño = numeros_introducidos[0]
numero_grande = numeros_introducidos[0]

for numero in numeros_introducidos:
    if numero_pequeño > numero:
        numero_pequeño = numero

    if numero_grande < numero:
        numero_grande = numero

print(f"La lista es: {numeros_introducidos}")
print(f"El numero más grande es: {numero_grande}")
print(f"El numero más pequeño es: {numero_pequeño}")
