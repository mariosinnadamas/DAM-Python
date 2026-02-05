'''
Crea un programa que escriba varios registros de estudiantes en un
archivo CSV llamado estudiantes.csv utilizando csv.DictWriter().
'''
import csv

campos = ['Nombre', 'Edad', 'Grado']

estudiantes = [
    {'Nombre': 'Juan', 'Edad': '20', 'Grado': 'A'},
    {'Nombre': 'Ana', 'Edad': '22', 'Grado': 'B'},
    {'Nombre': 'Luis', 'Edad': '21', 'Grado': 'A'}
]

with open('estudiantes.csv', 'w', newline='') as archivo_csv:
    escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
    escritor.writeheader()  # Escribir cabecera
    escritor.writerows(estudiantes)  # Escribir múltiples filas

print("Datos escritos en estudiantes.csv")