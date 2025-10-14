'''
Ejercicio 2: Tabla de multiplicar
Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10. Usa un bucle for
para generar la tabla. Si el usuario introduce un valor no numérico, muestra un mensaje de
error usando try-except.
'''
try:
    n = int(input("Introduce un número: "))
    for i in range (1, 11):
        print(n ,"x",i,"=",n*i)

except ValueError:
    print("ERROR: Introduce un número entero")