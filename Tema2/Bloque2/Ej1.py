'''
Escribe un programa que solicite al usuario un número entero positivo y determine si es
primo. El programa debe:
- Validar que el número sea entero y positivo.
- Lanzar una excepción si el valor no cumple con estas condiciones.
- Mostrar si el número es primo o no, explicando por qué (por ejemplo,
“No es primo
porque es divisible por 3”).
'''

import math

try:
    n = int(input("Introduce un número: "))

    # Validar que sea positivo
    if n <= 0:
        raise ValueError("El número debe ser positivo y mayor que 0.")

    # Casos especialesa
    if n == 1:
        print("No es primo porque el 1 solo tiene un divisor (él mismo).")
    elif n == 2:
        print("Es primo porque solo es divisible por 1 y por sí mismo.")
    else:
        es_primo = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                print(f"No es primo porque es divisible por {i}.")
                es_primo = False
                break
        if es_primo:
            print(f"Es primo porque solo es divisible por 1 y por sí mismo ({n}).")

except ValueError as e:
    print(f"Error: {e}")


