'''
Escribe un programa que lea un archivo CSV llamado clientes.csv y
busque un cliente específico por su nombre, mostrando todos los detalles de dicho cliente.
'''
import csv

nombre_buscado = input("Introduce el nombre del cliente: ")

with open("clientes.csv","r") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for fila in lector:
        if fila ['Nombre'] == nombre_buscado:
            print(fila)
