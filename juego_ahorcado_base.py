
# Juego que simula el ahorcado.
# Puedes cometer 6 fallos
# Importaciones
# ----------------------------------------------------------
import random
from os import system, name

# Constantes
# ----------------------------------------------------------
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

# Funciones
# ----------------------------------------------------------
def clear(): 
  
    # Para windows 
    if name == 'nt': 
        _ = system('cls') 
    # Para mac y linux(aquí, os.name es 'posix') 
    else: 
        _ = system('clear') 

def elijeLetra(letrasUtilizadas): 
    # Devuelve la letra que el jugador introdujo. Esta función hace que el jugador introduzca una letra y no cualquier otra cosa 
    while True: 
        print ('Adivina una letra:') 
        letra = input() 
        letra = letra.lower() 
        if len(letra) != 1: 
            print ('Introduce una sola letra.') 
        elif letra in letrasUtilizadas: 
            print ('Ya has elegido esa letra ¿Qué tal si pruebas con otra?') 
        elif letra not in 'abcdefghijklmnñopqrstuvwxyz': 
            print ('Elije una letra y no otro símbolo.') 
        else: 
            return letra 

def comprobar_letras(letra, l_l_palabra, l_l_falladas, l_l_acertadas, l_guiones):
    
    if letra in l_l_palabra:
    
        i = 0 
        for elemento in l_l_palabra:
            if elemento  == letra:
                l_guiones[i] = letra
            i = i+1

            l_l_acertadas.append(letra_elegida)

    else:
        l_l_falladas.append(letra_elegida)

def pintar_hud(l_l_falladas, l_guiones):

    print(AHORCADO[len(l_l_falladas)])
    print("Letras falladas:", " ".join(l_l_falladas))

    print("")
    print(" ".join(l_guiones))
    print(" ")

def comprobar_fin(l_guiones, l_l_falladas):

    if "_" not in l_guiones:
        print("Has ganado")
        return True
    elif len(l_l_falladas) >= 6:
        print("Has perdido")
        return True
    else:
        return False


# Variables
# ----------------------------------------------------------
palabras = ["caballo", "perro", "gato", "loro", "conejo", "pez"]

# Programa Principal
# ----------------------------------------------------------
clear()
print(AHORCADO[0])
# Pensar palabra
palabra_adivinar = palabras[random.randint(0,len(palabras)-1)]
#guiones
lista_guiones = []
lista_letras = list(palabra_adivinar)
for letra in lista_letras:
    lista_guiones.append("_")

print(" ".join(lista_guiones))

lista_letras_falladas = []
lista_letras_acertadas = []

parar = False
while not parar:
    
    letra_elegida = elijeLetra(lista_letras_acertadas + lista_letras_falladas)
    
    
    comprobar_letras(letra_elegida, 
                     lista_letras, 
                     lista_letras_falladas, 
                     lista_letras_acertadas, 
                     lista_guiones )
    
    pintar_hud(lista_letras_falladas, lista_guiones)

    parar = comprobar_fin(lista_guiones, lista_letras_falladas)