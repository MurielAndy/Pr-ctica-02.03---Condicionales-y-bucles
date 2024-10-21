#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener
#unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa
#que pregunte al usuario su edad y sus ingresos mensuales y muestre por
#pantalla si el usuario tiene que tributar o no.
a = int(input("Dime tu edad: "))
if a > 16:
    c = float(input("tus inglesos mensuales: "))
    if c > 1000:
        print("Tibutarias")
    else:
        print("No tributarias")
else:
    print("No tributarias")
