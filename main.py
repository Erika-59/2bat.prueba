from tienda import * 
from datetime import datetime
from os import system, name

def clear(): 
  
    # Para windows 
    if name == 'nt': 
        _ = system('cls') 
    # Para mac y linux(aquí, os.name es 'posix') 
    else: 
        _ = system('clear') 

def main():

    mi_tienda = Tienda(25,7,25,70)
    mi_cliente = Cliente()

    while True:
        print("-------TIENDA DE BICIS-------")
        print("1. Mostrar bicis disponibles")
        print("2. Alquilar bicis por horas a ", mi_tienda.preciohoras, "€")
        print("3. Alquilar bicis por días a ", mi_tienda.preciodias, "€")
        print("4. Alquilar bicis por semanas a ", mi_tienda.preciosemanas, "€")
        print("5. Devolver bicis en fecha actual" )
        print("6. Devolver bicis en fecha distinta" )
        print("7. Salir" )

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            mi_tienda.consultarStock()
        elif opcion == "2":
            mi_cliente.tipoAlquiler = 1
            mi_tienda.AlquilarPorHoras(mi_cliente.AlquilarBici())
        elif opcion == "3":
            mi_cliente.tipoAlquiler = 2
            mi_tienda.AlquilarPorDias(mi_cliente.AlquilarBici())
        elif opcion == "4":
            mi_cliente.tipoAlquiler = 3
            mi_tienda.AlquilarPorSemanas(mi_cliente.AlquilarBici())
        elif opcion == "5":
            mi_tienda.GenerarFactura(mi_cliente.DevolverBici(),datetime.now())

        elif opcion == "6":
            fecha_diferida = input("En que fecha quieres devolver las bicis? ")
            fecha_diferida = datetime.strptime(fecha_diferida, "%H:%M %d/%m/%Y")
            mi_tienda.GenerarFactura(mi_cliente.DevolverBici(),fecha_diferida)
        elif opcion == "7":
            break

        else: 
            print("No entiendo la orden, elige un numero del 1 al 7")
            clear()
            
    print("Gracias por unas nuestra sistema de alquiler de bicis")

#Programa
if __name__=="__main__":
    main()
        