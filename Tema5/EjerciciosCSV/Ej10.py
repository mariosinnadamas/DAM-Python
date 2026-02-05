'''
Crea un programa que elimine una fila de un archivo CSV llamado
inventario.csv basándose en el nombre de un producto que proporcione el usuario.
'''
import csv

producto_a_eliminar = input("Introduce el nombre del producto a eliminar: ")
filas_filtradas = []

# Leer el archivo original y guardar filas que no coincidan con el producto a eliminar
with open('inventario.csv', 'r') as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for fila in lector:
        if fila['Producto'] != producto_a_eliminar:
            filas_filtradas.append(fila)

# Sobrescribir el archivo CSV con las filas filtradas
with open('inventario.csv', 'w', newline='') as archivo_csv:
    campos = ['Producto', 'Precio', 'Cantidad']
    escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(filas_filtradas)

print(f"El producto '{producto_a_eliminar}' ha sido eliminado del inventario.")