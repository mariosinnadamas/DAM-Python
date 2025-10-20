'''
Crea una calculadora que permita al usuario introducir dos números y una operación (+,
/). El programa debe:
- Validar que los números sean válidos.
- Manejar la división por cero.
- Manejar operaciones no reconocidas.
- Usar try-except con múltiples bloques para capturar distintos errores.
'''
try:
    n1 = float(input("Introduce n1: "))
    n2 = float(input("Introduce n2: "))
    op = input("Introduce la operación que quieras realizar (+ o /): ")
    if op == "+":
        print(n1+n2)
    elif op == "/":
        try:
            resultado = n1/n2
            print(resultado)
        except ZeroDivisionError:
            print("ERROR: No se puede dividir entre 0")
        else:
            print("Operación no válida")
except ValueError:
    print("ERROR: Número introducido no válido")
