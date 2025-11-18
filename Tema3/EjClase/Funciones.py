import math

def area_cuadrado(lado):
    if lado <= 0:
        raise ValueError("El lado debe ser un número positivo")
    return lado ** 2


def area_circulo(radio):
    if radio <= 0:
        raise ValueError("El radio debe ser un número positivo")
    return math.pi * (radio ** 2)


def area_triangulo(base, altura):
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser números positivos")
    return (base * altura) / 2