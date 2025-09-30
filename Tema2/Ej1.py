try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0:
        print("ERROR: Debes introducir un numero positivo")
    elif edad >= 18:
        print("Mayor de edad")
    else:
        print("Menor de edad")
except ValueError:
    print("Debes introducir un numero entero")
    exit()