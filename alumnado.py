#Inicio
apellido = input("Dime tu primer apellido: ").lower()
sexo = input("Dime el sexo (H)Hombre O (M)Mujer: ").upper()
if sexo == "M" and (apellido[0] <= "m"):
    print ("Grupo A")
elif sexo == "M" and (apellido[0] > "m"):
    print ("Grupo B")
elif sexo == "H" and (apellido[0] <= "n"):
    print ("Grupo B")
elif sexo == "H" and (apellido[0] > "n"):
    print ("Grupo A")

