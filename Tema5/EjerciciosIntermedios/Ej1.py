'''
Escribe un programa que lea un fichero datos.csv y cuente cuántas palabras contiene en total.
'''

with open("../EjerciciosBasicos/fichero.txt","r") as fichero:
    lineas = fichero.read()
    palabras = lineas.split()
    print(len(palabras))