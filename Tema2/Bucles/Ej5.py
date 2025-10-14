'''
Ejercicio 5: Números primos hasta N
Solicita al usuario un número entero positivo N y muestra todos los números primos desde 2
hasta N. Usa un bucle for para recorrer los números y otro bucle while para verificar si son
primos. Maneja errores si el usuario introduce un valor no válido.
'''

try:
    n = int(input("Introduce un número entero positivo: "))

    if n < 2:
        print("Debes introducir un número mayor o igual a 2.")
    else:
        print(f"Números primos entre 2 y {n}:")

        # Recorro los números desde 2 hasta N
        for num in range(2, n + 1):
            es_primo = True  # Supongo que es primo
            divisor = 2

            # Verificamos si el número tiene divisores
            while divisor < num:
                if num % divisor == 0:
                    es_primo = False
                    break  # No es primo, salimos del bucle
                divisor += 1

            if es_primo:
                print(num)

except ValueError:
    print("Error: Debes introducir un número entero válido")
