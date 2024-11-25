ruta = "frases.txt"
with open(ruta, mode="w", encoding="utf_8") as fichero2:
    for i in range (0, 5):
        frase = input("Dime una frase: ")
        print(frase, file=fichero2)