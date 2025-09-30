print("MENU")
print("1. Ver Perfil")
print("2. Editar perfil")
print("3. Salir")
try:
    eleccion = int(input("Introduce un numero: "))

    if eleccion == 1:
        print("Ver perfil")
    elif eleccion == 2:
        print("Editar perfil")
    elif eleccion == 3:
        print("Salir")
    else:
        print("Opcion invalida")
except ValueError:
    print("Introduce un numero entero")
