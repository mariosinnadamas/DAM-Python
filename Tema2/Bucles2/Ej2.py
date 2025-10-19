try:
    n = int(input("Introduce un número entero positivo: "))
    if n <0:
        raise ValueError("El númeor debe ser positivo")

    cuenta_atras = ""
    for i in range(n,0, -1):
        cuenta_atras += str(i)
        if i > 1:
            cuenta_atras += ","

    print(cuenta_atras)
except ValueError as e:
    print(f"ERROR: {e}")