'''
Ejercicio 3: Adivina el número
El programa genera un número aleatorio entre 1 y 100. El usuario debe adivinarlo. Después
de cada intento, el programa indica si el número es mayor o menor. Usa try-except para
validar que la entrada sea numérica. El juego termina cuando el usuario acierta.
'''
import random
random = random.randrange(1,101)
while (True):
    try:
        n = int(input("Introduce un número: "))
        if n < random:
            print("El numero introducido es más pequeño")
        elif n > random:
            print("El numero introducido es mayor")
        else:
            print("Has ganado")
            break
    except ValueError:
        print("ERROR: Introduce un numero entero")
