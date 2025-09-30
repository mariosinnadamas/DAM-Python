try:
    n = int(input("Introduce un numero: "))
    if n<0:
        print("Introduce un numero positivo")
    elif n%2 == 0:
        print("Par")
    else:
        print("Impar")
except ValueError:
    print("Introduce un numero entero")