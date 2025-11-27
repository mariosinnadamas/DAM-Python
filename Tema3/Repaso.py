
def saludar (*, nombre: str, saludo: str = "Hola"):
    return saludo + " " + nombre

def tabla_multiplicar(numero: int,*,hasta:int=10) -> (list[int]):
    return [numero * i for i in range (1,hasta+1)]

def filtrar_pares(lista: list[int]):
    pares = []
    for i in lista:
        if i%2 == 0:
            pares.append(i)
    return pares

try:
    numero = int(input("Introduce un numero"))
except ValueError as e:
    print(e)