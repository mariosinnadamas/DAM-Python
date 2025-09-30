#Ej 1: Calculadora de salario
#Ej2: Añadir try/except y controlar la entrada
try:
    horas = int(input("Introduce las horas que trabajas: "))
    rate = int(input("Introduce el precio de trabajo: "))
except ValueError:
    print("ERROR")
    exit() #Sale del programa

if horas < 0 or rate < 0:
    print("ERROR: Los valores son negativos.")
    exit() #Sale del programa

if horas > 40:
    extra = (horas - 40) * (rate * 1.5)
    pago = 40 * rate + extra
    print(pago)
else:
    pago = horas * rate
    print(pago)


