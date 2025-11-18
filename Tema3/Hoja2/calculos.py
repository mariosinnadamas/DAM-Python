from itertools import count

import math
'''
Crear un módulo (calculos.py) que contenga funciones para calcular el área de un círculo
areaCirculo(radio), cuadrado areaCuadrado(lado) y triángulo areaTriangulo(base,
altura). Hay que tener en cuenta que si no se ha introducido alguno de los valores
necesarios, tomará por defecto el 8
Desde otro fichero. usa las funciones del módulo para calcular el área de un círculo con
radio 5, un cuadrado de lado 10 y un triángulo de base 4 y altura 6.
'''

def areaCirculos(radio=8):
    return math.pi*(radio**2)

def areaCuadrado(lado=8):
    return lado**2

def areaTriangulo(base = 8, altura = 8):
    return (base*altura)/2
'''
Crea una función para calcular el precio de una entrada precioEntrada
sabiendo que para ello necesita conocer además del precio normal de la entrada (por
defecto 10), la edad del asistente y si es estudiante; ya que en caso de ser menor de 18 o
estudiante, tendría un descuento del 50% de descuento.
'''
def precioEntrada(edad:int, estudiante:bool, precio=10):
    if edad < 18 or estudiante == True:
        precio = precio * 0.5
    return precio

'''
Añade otra función multiplicar que reciba cualquier cantidad de números y
devuelva su producto.
'''
def multiplicar(*numeros):
    producto = 1
    for numero in numeros:
        producto *= numero
    return producto

'''
Añade una nueva función al módulo multiplicandoUnaSuma que reciba
cualquier cantidad de números y un parámetro multiplicador La función debe devolver la
suma de los números multiplicada por el valor del multiplicador.
'''

def multiplicandoUnaSuma(multiplicador,*numeros):
    suma = sum(numeros)
    return suma*multiplicador

'''
Crea una función contarArgumentos que reciba cualquier número de
argumentos y devuelva cuántos se han pasado.
'''
def contarArgumentos(*argumentos):
    return len(argumentos)