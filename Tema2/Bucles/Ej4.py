'''
Ejercicio 4: Comprobar si un número es primo
Solicita al usuario un número entero positivo y comprueba si es primo. Usa un bucle while
para verificar si tiene divisores y muestra el resultado. Valida la entrada con try-except.
'''
import math

while(True):
    try:
        n = int(input("Introduce un número entero positivo, negativo si quieres terminars: "))
        if n < 0:
            raise ValueError("ERROR: Introduce un número positivo")

        if n == 1:
            print("No es primo porque el 1 solo tiene un divisor (él mismo).")
        elif n == 2:
            print("Es primo porque solo es divisible por 1 y por sí mismo.")
        else:
            esPrimo = True
            for i in range (2, int(math.sqrt(n)) + 1):
                if n%i == 0:
                    print("No es Primo")
                    esPrimo = False

            if esPrimo:
                print("Es primo")
    except ValueError:
        print("ERROR: Introduce un número entero positivo")
        break