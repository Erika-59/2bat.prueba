import random

class Carta():
    valores = [None, None, 2,3,4,5,6,7,8,9,10,11,12,13]
    palos = ["oros", "bastos", "copas", "espadas"]

    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def mayor_que(self, otra_carta):
        if self.valor > otra_carta.valor:
            return True
        else:
            return False
        
    def menor_que(self, otra_carta):
        if self.valor < otra_carta.valor:
            return True
        else:
            return False
    
    def igual_que(self, otra_carta):
        if self.valor == otra_carta.valor:
            return True
        else:
            return False
        
    #Descripcion de la carta
    def __repr__(self):
        d = str(self.valor) + " de " + str(self.palo)
        return d

class Baraja():
    
    def __init__(self):
        self.mazo = []
        for i in range(2,14):
            for j in range(4):
                nueva_carta = Carta(i, Carta.palos[j])
                self.mazo.append(nueva_carta)

    def barajar(self):
        random.shuffle(self.mazo)

    def quitar_carta(self):
        una_carta = self.mazo.pop()
        return una_carta


#Clase jugador
class Jugador():

    rondas = 0

    def __init__(self):
        self.nombre = input("Dime tu nombre: ")

    def gana_ronda(self):
        self.rondas = self.rondas + 1
        print("El jugador", self.nombre, "lleva ganadas", str(self.rondas))

#Clase  juego
class Juego():

    def __init__(self):
        #Crear Baraja
        self.la_baraja = Baraja()
        #Barajar
        self.la_baraja.barajar()
        #Jugador
        self.jugador1 = Jugador()
        print("Primer jugador creado, vamos con el siguiente...")
        #Jugador
        self.jugador2 = Jugador()
        print("Segundo jugador creado, vamos a jugar")

    def jugar(self):
        #para cada ronda
        while len(self.la_baraja.mazo) > 0:
            #jugador 1 coge una carta
            self.carta_j1 = self.la_baraja.quitar_carta()
            #jugador 2 coge una carta
            self.carta_j2 = self.la_baraja.quitar_carta()
            print("El jugador", self.jugador1.nombre, "ha cogido la carta", self.carta_j1)
            print("El jugador", self.jugador2.nombre, "ha cogido la carta", self.carta_j2)
            #comparar cartas
            if self.carta_j1.mayor_que(self.carta_j2):
                #Gana jugador1
                print("Gana la ronda el jugador", self.jugador1.nombre)
                self.jugador1.gana_ronda()
            elif self.carta_j1.menor_que(self.carta_j2):
                print("Gana la ronda el jugador", self.jugador2.nombre)
                self.jugador2.gana_ronda()
                #Gana jugador2
            else:
                print("Ha habido un empate")

        if self.jugador1.rondas > self.jugador2.rondas:
            print("Gana el juego", self.jugador1.nombre, "con", str(self.jugador1.rondas))
        elif self.jugador1.rondas < self.jugador2.rondas:
            print("Gana el juego", self.jugador2.nombre, "con", str(self.jugador2.rondas))
        else:
            print("hay un empate entre", self.jugador1.nombre, 
                  "y", self.jugador2.nombre, "con",  str(self.jugador2.rondas))
        #parar cuando no quedan cartas
        #Decir que jugador a ganado mas rondas


#Programa principal
mi_juego = Juego()
mi_juego.jugar()