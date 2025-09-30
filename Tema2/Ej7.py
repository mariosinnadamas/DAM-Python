try:
    edad = int(input("Introduce tu edad: "))
    if edad<0:
        print("Tu edad no puede ser negativa")
    elif edad<14:
        print("No puede conducir")
    elif 14<= edad < 16:
        print("Moto de poca cilindrada")
    elif 16<= edad < 18:
        print("Moto de gran cilindrada")
    elif edad >=18:
        print("Coche")
except ValueError:
    print("ERROR: Introduce un numero entero")