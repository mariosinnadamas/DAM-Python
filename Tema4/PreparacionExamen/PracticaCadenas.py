from itertools import count


def calcular_cadena(cad):
    return len(cad),cad.upper(),cad.lower()

def calcular_vocales(cad):
    contador = 0
    for c in cad:
        if c == 'a' or c == 'e' or c == 'i'or c == 'o' or c == 'u':
            contador+=1
    return contador

def invertir_cadena(cad):
    return cad[::-1]

def es_palindromo(cad):
    return cad == cad [::-1]

def sustituir_letras(cad):
    return cad.replace("a","o")

cadena = input("Introduce una cadena: ")
print(calcular_cadena(cadena))
print("Cantidad de vocales : ", calcular_vocales(cadena))
print("Cadena invertida: ", invertir_cadena(cadena))
print("Es un palíndromo? ", es_palindromo(cadena))
print("Sustituir letras: ", sustituir_letras(cadena))