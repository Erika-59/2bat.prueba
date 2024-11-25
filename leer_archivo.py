ruta = "animales.txt"
with open (ruta, mode="r", encoding="utf-8") as fichero1:
    for linea in fichero1:
        print(linea.strip())