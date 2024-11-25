ruta = input("Dime un fichero a cambiar: ")
palabra1 = input("Dime una palabra que aparezca dentro el texto: ")
palabra2 = input("Dime una palabra para sustituir: ")
nueva_ruta = ruta + "_modificado.txt"

cuenta = 0

with open (ruta, mode="r", encoding="utf-8") as fichero1:
    with open (nueva_ruta, mode="w", encoding="utf-8") as fichero2:
        for linea_leida in fichero1:
            cuenta = cuenta + linea_leida.count(palabra1)
            nueva_linea = linea_leida.replace(palabra1, palabra2)
            print(nueva_linea.rstrip(), file=fichero2)
print("Se ha sustituido: ", cuenta, "veces la palabra.")