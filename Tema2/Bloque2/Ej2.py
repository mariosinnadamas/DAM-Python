'''
Crea un programa que convierta una cantidad en euros a otra divisa (USD, GBP o JPY). El
usuario debe introducir:
- La cantidad en euros.
- La divisa destino.
El programa debe:
- Validar que la cantidad sea un número positivo.
- Validar que la divisa esté entre las permitidas.
- Manejar excepciones si el usuario introduce datos incorrectos.
'''
import sys

try:
    n = float(input("Introduce la cantidad en euros: "))
    if n < 0:
        print("Introduce un numero mayor que 0")
        sys.exit()

    divisa = input("Introduce a que moneda quieres cambiar (USD, GBP o JPY): ")
    if divisa.lower() == "usd":
        resultado = n * 1.16
        print("Dolares Estadounidenses: " f'{resultado:.2f}')
    elif divisa.lower() == "gbp":
        resultado = n * 0.87
        print("Libras esterlinas: " f'{resultado:.2f}')
    elif divisa.lower() == "jpy":
        resultado = n * 176.73
        print("Yenes: " f'{resultado:.2f}')
    else:
        print("No has introducido una moneda válida")
        sys.exit()

except ValueError:
    print("Introduce un numero")