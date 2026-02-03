'''
Escribe un programa que copie el contenido de un
fichero datos.csv a un nuevo fichero llamado copia.txt.
'''

with open("fichero.txt", "r") as original:
    with open("copia.txt", "w") as copia:
        for linea in original:
            copia.write(linea)
