#Escribir un programa que almacene la cadena de caracteres contraseña en 
#una variable, pregunte al usuario por la contraseña hasta que introduzca la
#contraseña correcta.
correcta = "Contraseña"
while True:
    x = input("Dime la contraseña: ")
    if x == correcta:
        print("Contraseña correcta")
        break
    else:
        print("Vuelve a escribir la contraseña: ")
