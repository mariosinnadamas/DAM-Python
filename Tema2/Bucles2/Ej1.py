#Ejercicio de inversión por interes y año

try:
    inv = float(input("Introduce la cantidad a invertir: "))
    if inv < 0:
        raise ValueError("No puedes introducir una cantidad inferior a 0 euros")

    interes = float(input("Introduce el interés anual en %: "))

    anio = int(input("Introduce el número de años: "))
    if anio < 1:
        raise ValueError("No puedes introducir menos de un año")

    #Conversión del interes de porcnetaje
    interes = interes * 0.01

    for i in range(0,anio):
        interesObtenido = inv * interes
        inv += interesObtenido

        print(f"Interés obtenido en año {i}: ", interesObtenido)
    print("Capital total: ", inv)


except ValueError:
    print("ERROR: Introduce un número")