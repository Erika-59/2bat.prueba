ruta = "frases.txt"
with open (ruta, mode="r+", encoding="utf-8") as fichero1:
    for linea in fichero1:
        print("\n", linea.rstrip())
    for i in range (0, 5):
        frase = input("Dime una frase:\n")
        print(frase, file=fichero1)