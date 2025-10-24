'''
Pasas una cadena, cada letra representa un color y debe usarse colores de la a la m.
Debe devolver la tasa de error
'''
import re


def printer_error(s):
    letters = []
    for i in s:
        if 'a' <= i <= 'm' and i is not letters:
            letters.append(i)

    error = len(s) - len(letters)
    cadena = str(error) + "/" + str(len(s))
    return cadena

print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))