# import only system from os
from os import system, name


# define our clear function
def limpiar():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
#pedir pizza
lista_ingredientes_vegetarianos = ["Pimiento", "Tofu"]
lista_ingredientes_normales = ["Peperoni", "Jamón", "Salmón"]
lista_ingredientes = ["Tomate", "Queso"]
lista_a_usar = []
#¿Pizza vegatariana?
#mostrar menú
print("¿Qué tipo de pizza prefieres?")
print("1. (V)egetariana")
print("2. (N)ormal")
tipo_pizza = input().lower
limpiar()

if tipo_pizza == "N" or tipo_pizza == "2":
    lista_a_usar = lista_ingredientes_normales
else:
    lista_a_usar = lista_ingredientes_vegetarianos

#Mostrar ingredientes
i = 1
print("Elija un ingrediente de los siguientes:")
for elemento in lista_a_usar:
    print(i, ". ", elemento)
    i = i + 1

#Eligir ingredientes
ingredientes_eligidos = int(input())

limpiar()

#Mostrar todos
print("Su pizza lleva los siguientes ingredientes:")
for elemento in lista_ingredientes:
    print(elemento)
print(lista_a_usar[ingredientes_eligidos-1])