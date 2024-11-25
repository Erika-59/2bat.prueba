class Coche: 
    """Decribe los coches y las cosas que pueden hacer"""
    n_ruedas = 4
    
    def __init__(self,DNI, marca, modelo ,color, matricula, v_maxima, v_inicial = 0):

        self.DNI = DNI
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.matricula = matricula
        self.v_inicial = v_inicial
        self.v_maxima = v_maxima
    #Metodos

    #Acelerar
    def acelerar(self, inc_velocidad):
        if self.v_inicial + inc_velocidad <= self.v_maxima:
            self.v_inicial = self.v_inicial + inc_velocidad
        print("La velocidad actual del ", self.marca, " ", self.modelo, " es:",self.v_inicial)
    #Frenar
    def frenar(self, des_velocidad):
        if self.v_inicial - des_velocidad >= 0:
            self.v_inicial = self.v_inicial - des_velocidad
        print("La velocidad actual del ", self.marca, " ", self.modelo, " es:",self.v_inicial)
    #pintar
    def pintar(self, nuevo_color):
        print("El color actual del ", self.marca, " ", self.modelo, " es:",self.color)  
        self.color = nuevo_color
        print("Ahora es de:", self.color)


class Persona:
    """Define caracteristicas de las personas"""

    def ___init___(self, dni,nombre, edad, sexo, direccion):
        if self.validar_dni(self, dni):
            self.dni = dni
        else:
            print("DNI no valido")
        
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.direccion = direccion

    def cambia_direccion(self, nueva_direccion):
        print("Cambiamos la direccion de:", self.direccion, " a", nueva_direccion)
        self.direccion = nueva_direccion

    def cumplir_anyos(self, aumento=1):
        self.edad = self.edad + aumento
        print("Ahora tienes", self.edad)

    #dni
    def validar_dni(self, nuevo_dni):
        if len(nuevo_dni) > 9:
            return False
        numero = nuevo_dni[:8]
        letra = nuevo_dni[8:]
        if numero.isnumeric():
            return False
        if not letra.isalpha():
            return False
        return True

    #mayor de edad
    def mayor_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

#Programa principal
coche_e = Coche("Ford","Fiesta", "Rojo", "555-HTF", 120, 23)
coche_p = Coche("Peugeot", "5008", "Gris", "5678-HGF", 150, 0)

coche_p.acelerar(30)
coche_e.acelerar(50)
coche_p.pintar("Azul")
coche_e.frenar(10)