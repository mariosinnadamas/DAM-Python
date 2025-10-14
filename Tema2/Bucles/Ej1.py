'''
Ejercicio 1: Calculadora de operaciones básicas
Crea un programa que simule una calculadora. El usuario debe introducir dos números y
seleccionar una operación: suma, resta, multiplicación o división. El programa debe
repetirse hasta que el usuario decida salir. Debe manejar errores como división por cero y
entrada de datos no numéricos.
'''
try:
    while(True):
        print("Menu")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        dec = int(input())

        if dec == 1:
            resultado = 0
            n1 = int(input("Introduce el n1: "))
            n2 = int(input("Introduce el n2: "))
            resultado = n1+n2
            print(resultado)
        elif dec == 2:
            resultado = 0
            n1 = int(input("Introduce el n1: "))
            n2 = int(input("Introduce el n2: "))
            resultado = n1 - n2
            print(resultado)
        elif dec == 3:
            resultado = 0
            n1 = int(input("Introduce el n1: "))
            n2 = int(input("Introduce el n2: "))
            resultado = n1 * n2
            print(resultado)
        elif dec == 4:
            resultado = 0
            n1 = int(input("Introduce el n1: "))
            n2 = int(input("Introduce el n2: "))
            try:
                resultado = n1 / n2
            except ArithmeticError:
                print("ERROR: No puedes dividir entre 0")
            print(resultado)
        elif dec == 5:
            break
        else:
            print("ERROR: Opción no válida")
except ValueError:
    print("ERROR: Introduce un numero entero")