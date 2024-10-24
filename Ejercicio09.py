#Escribir un programa que pida al usuario un número entero y muestre por 
#pantalla un triángulo rectángulo que tenga tantas líneas como el número 
#introducido, como el triángulo de más abajo
num = int(input("dame un numero entero: "))
for i in range(num):
    for x in range(i+1):
        print(num, end="")
    print("")
