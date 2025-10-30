def cuenta_atras(n):
    cuenta_atras = ""
    for i in range(n,0, -1):
        cuenta_atras += str(i)
        if i > 1:
            cuenta_atras += ","
    return cuenta_atras

try:
    n = int(input("Introduce un número entero positivo: "))
    if n <0:
        raise ValueError("El número debe ser positivo")
except ValueError as e:
    print(f"ERROR: {e}")

print(cuenta_atras(n))