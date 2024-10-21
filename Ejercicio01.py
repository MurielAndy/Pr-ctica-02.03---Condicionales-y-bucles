#Escribir un programa que almacene la cadena de caracteres contraseña en una
#variable, pregunte al usuario por la contraseña e imprima por pantalla si la
#contraseña introducida por el usuario coincide con la guardada en la variable
#sin tener en cuenta mayúsculas y minúsculas
contra = input("Escribe tu contraseña: ")
contra_nueva = input("Confirmar contraseña: ")
if contra == contra_nueva:
    print("Contraseña correcta")
elif contra != contra_nueva:
    print("No son iguales")

     
