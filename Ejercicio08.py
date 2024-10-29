#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 
#al 10.
for i in range(1, 11):
    for x in range(1, 11):
        print(i * x, end="\t")
    print("")