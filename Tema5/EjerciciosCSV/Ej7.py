'''
Crea un programa que añada nuevas filas de datos a un archivo CSV llamado inventario.csv.
Las nuevas filas deben incluir los datos de productos adicionales.
'''
import csv

with open("inventario.csv","w",newline="") as fichero:
    writer = csv.writer(fichero)
    writer.writerow(['Grapadora',12.99,50])
    writer.writerow(['Bolígrafo',0.99,500])
