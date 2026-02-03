'''
Escribe un programa que lea un archivo CSV llamado datos.csv y muestre
su contenido en la consola, fila por fila.
'''
import csv

#Forma 1
with open("datos.csv","r")as fichero:
    datos = csv.reader(fichero)
    for i in datos:
        print(i)

