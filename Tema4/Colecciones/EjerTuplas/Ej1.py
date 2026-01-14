'''Crea una función calcular_estadisticas(numeros) que reciba una lista de números y devuelva una tupla con:
- El valor mínimo.
- El valor máximo.
- La media aritmética
'''
import math

def calcular_estadistica(numeros):
    minimo = min(numeros)
    maximo = max(numeros)
    media = sum(numeros) / len(numeros)
    return minimo,maximo,media

numeros = (1,2,3,4,5)
print(calcular_estadistica(numeros))

'''
Crea una función distancia(p1, p2) que reciba dos tuplas representando
puntos en el plano (x, y) y devuelva la distancia entre ellos usando la fórmula:
'''

def distancia(p1,p2):
    x1,y1 = p1
    x2, y2 = p2
    dist = math.sqrt((x2 - x1)**2 + (y2-y1)**2)
    return dist

punto1 = (1,2)
punto2 = (4,6)
print(distancia(punto1, punto2))

'''
Crea una función analizar_texto(texto) que devuelva una tupla con:
- Número total de caracteres.
- Número de palabras.
- Primera palabra del texto.
'''

def analizar_texto(texto):
    caracteres = len(texto)
    palabras = texto.split()
    num_palabras = len(palabras)
    prim_palabra = palabras[0]
    return caracteres,num_palabras,prim_palabra

texto = "Hola mundo esto es una prueba"
print(analizar_texto(texto))

'''
Crea una función convertir_temperatura(celsius) que reciba una
temperatura en grados Celsius y devuelva una tupla con:
- La temperatura en Fahrenheit.
- La temperatura en Kelvin.
'''

def convertir_temparatura(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.5
    return fahrenheit, kelvin

print(convertir_temparatura(25))


'''
Crea una función analizar_numeros(numeros) que reciba una lista de
enteros y devuelva una tupla con:
- El número de elementos pares.
- El número de elementos impares.
- La suma total.
'''

def analizar_numeros(numeros):
    pares = 0
    impares = 0
    suma_total = 0

    for n in numeros:
        suma_total += n
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares, suma_total

enteros = [1,2,3,4,5]
print(analizar_numeros(enteros))

'''
Crea una función procesar_cadena(cadena) que devuelva una tupla con:
- La cadena en mayúsculas.
- La cadena en minúsculas.
- La longitud de la cadena.
'''

def procesar_cadena(cadena):
    mayusculas = cadena.upper()
    minusculas = cadena.lower()
    longitud = len(cadena)
    return mayusculas,minusculas,longitud

print(procesar_cadena("Esto es una cadena"))