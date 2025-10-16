#Haz una pirámide de asteriscos pidiendo el número de lineas al usuario

try:
    n = int(input("Introduce el número de lineas de la pirámide: "))
    for i in range (1, n+1):
        espacios = " " * (n-i)
        asteriscos = "*" * (2*i-1)
        print(espacios + asteriscos)

except ValueError:
    print("ERROR: Introduce un número")