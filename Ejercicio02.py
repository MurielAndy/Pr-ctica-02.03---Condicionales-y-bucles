#Escribir un programa que pida al usuario dos números y muestre por pantalla
#su división. Si el divisor es cero el programa debe mostrar un error.
a = float(input("Dime un numero: "))
b = float(input("Dime un numero: "))
c = (a / b)
if c > 0:
    print(c)
elif c < 0:
    print("Error!")

