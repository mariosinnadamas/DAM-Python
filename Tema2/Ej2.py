try:
    n1 = int(input("Ingresa un numero: "))
    n2 = int(input("Ingresa otro numero: "))
    if n1 > n2:
        print(n1, " es mayor que ", n2)
    elif n1 < n2:
        print(n2, " es mayor que ", n1)
    else:
        print(n1, " es igual a ", n2)
except ValueError:
    print("Debes introducir un numero entero")