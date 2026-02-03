'''
Crea un programa que lea un fichero datos.csv y muestre la frecuencia de cada palabra en el archivo.
'''

diccionario_palabras = {}

with open("../EjerciciosBasicos/fichero.txt","r") as fichero:
    linea = fichero.read()
    palabras = linea.split()
    for palabra in palabras:
        diccionario_palabras[palabra] = diccionario_palabras.get(palabra,0) + 1

print(diccionario_palabras)


