#Ejercicio1
def info_argumentos(*args: int):
    contador = 0
    for arg in args:
        contador += 1
        print("Argumento: " + str(arg))
    return "Contador total: " + str(contador)

def divisibles3(*args: int):
    numeros = []
    for arg in args:
        if arg % 3 == 0:
            numeros.append(arg)
    return "Numeros divisibles entre 3: " + str(numeros)

def histograma(*args: int):
    for arg in args:
        print("*" * arg)

#Ejercicio2
def coste_envio(peso: float,*,tarifa: int = 5,urgente: bool = False):
    recargo = 0.30

    if peso >=1:
        tarifa = tarifa + (peso * 2)
    if urgente:
        tarifa = tarifa + (tarifa * recargo)
    return "Precio: " + str(tarifa) + "€"

def convertir_segundos(horas: int, minutos: int, segundos: int):
    minutos = minutos + (horas * 60)
    segundos = segundos + (minutos * 60)
    return "Total en segundos: " + str(segundos)

