#Los alumnos de Hogwarts se han dividido en dos casas, Gryffindor y Slytherin,
#de acuerdo al sexo y el nombre. Gryffindor está formado por las mujeres con
#un nombre anterior a la M y los hombres con un nombre posterior a la N y
#Slytheryn por el resto. Escribir un programa que pregunte al usuario su
#nombre y sexo, y muestre por pantalla el grupo que le corresponde.
nombre = input("Cómo te llamas? ")
sexo = input("Cuál es tu sexo (M o H)? ")
if sexo == "M":
    if nombre.lower() < "m":
        grupo = "Gryffindor"
    else:
        group = "Slytherin"
else:
    if nombre.lower() > "n":
        group = "Gryffindor"
    else:
        group = "Slytherin"
print("Tu grupo es " + group)
