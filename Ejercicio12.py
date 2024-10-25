#Escribir un programa en el que se pregunte al usuario por una frase y una
#letra, y muestre por pantalla el número de veces que aparece la letra en la
#frase.
frase = input("Escribeme una frase: ")
letra = input("Dime de la frase una letra: ")
suma = 0
for i in frase:
    if i == letra:
        suma += 1
print("la letra", letra, "aparecece", suma, "veces")
    