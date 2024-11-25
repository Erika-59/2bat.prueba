from datetime import *

#----------------------------------------------------------------------------------------------------
class Cliente():

    numBicis = 0
    tipoAlquiler = 0 #1. Alquiler por horas 2.Alquiler por dias 3. Alquiler por semanas
    tiempoAlquiler = 0

    def __init__(self,tipo= 0):
        self.tipoAlquiler = tipo

    def AlquilarBici(self):
        numero = input("¿Cuantas bicis quieres alquilar?\n")
        try: 
            el_numero = int(numero)
            if el_numero < 1:
                print("el nº de bicis debe ser un nº positivo,mayor a 0")
            else:
                self.numBicis = el_numero
                self.tiempoAlquiler = datetime.today()
        except ValueError:
            print(numero, "No es un nº entero")
        return self.numBicis
    def DevolverBici(self):
        print("Va usted a devolver", self.numBicis)
        return self.numBicis,self.tipoAlquiler, self.tiempoAlquiler
    
#----------------------------------------------------------------------------------------------------
class Tienda():

    stock = 0
    preciohoras = 0
    preciodias = 0
    preciosemanas = 0
    descuento = 0

    #creamos la tienda con el stock inicial, precio y descuentos
    def __init__(self, stock_inicial, ph=5, pd=20, ps=60, desc=30):
        self.stock = stock_inicial
        self.preciohoras = ph
        self.preciodias = pd
        self.preciosemanas = ps
        self.descuento = desc

    #Alquilar Bicis por horas
    def AlquilarPorHoras(self,bicis):
        if self.stock >= bicis:
            print("Has alqulado", bicis, "por horas. Se cobrará a ", self.preciohoras, "cada bici.")
            print("Espero que disfrute con nuestros productos.")
            self.stock = self.stock - bicis
        else:
            print("No hay sufucientes bicis disponibles, disculpe las molestias")

    #Alquilar Bicis por dias
    def AlquilarPorDias(self,bicis):
        if self.stock >= bicis:
            print("Has alqulado", bicis, "por días. Se cobrará a ", self.preciodias, "cada bici.")
            print("Espero que disfrute con nuestros productos.")
            self.stock = self.stock - bicis
        else:
            print("No hay sufucientes bicis disponibles, disculpe las molestias")

    #Alquilar Bicis por semanas
    def AlquilarPorSemanas(self,bicis):
        if self.stock >= bicis:
            print("Has alqulado", bicis, "por semanas. Se cobrará a ", self.preciosemanas, "cada bici.")
            print("Espero que disfrute con nuestros productos.")
            self.stock = self.stock - bicis
        else:
            print("No hay sufucientes bicis disponibles, disculpe las molestias")

    #Devolver las bicis y generar las facturas
    def GenerarFactura(self, tupla,fecha_actual):
        #Mirar el alquiler
        if tupla[1] == 1:
            total_factura = tupla[0] * self.preciohoras * (int((fecha_actual - tupla [2]).total_seconds()//3600))
        elif tupla[1] == 2:
            total_factura = tupla[0] * self.preciodias * (fecha_actual - tupla [2]).days
        elif tupla[1] == 3:
            total_factura = tupla[0] * self.preciosemanas * ((fecha_actual - tupla [2]).days//7)
        else:
            print("No reconozco ese tipo de alquiler")
            return
        #Aplicar descuento
        if tupla[0] >= 3 and tupla[0] <= 5:
            print("Le aplicaremos un descuernto en su factura del ", self.descuento, "%")
            total_factura = total_factura - (total_factura * self.descuento / 100)

        #Reponer stock
        self.stock = self.stock + tupla[0]
        print("El importe a pagar es de", round(total_factura,2),"€")
        return total_factura 

        
    def consultarStock(self):
        print("El stock actual es de", self.stock, "bicis.")
    