


#Funcion nueva
def cuenta(nombre_fichero):
    with open (nombre_fichero, mode="r", encoding="utf-8") as fichero1:
        lineas = fichero1.readlines()
        return len(lineas)
f = input("dime el nombre del fichero: ")
print ("El fichero",f, "tiene" ,cuenta(f), " lineas")