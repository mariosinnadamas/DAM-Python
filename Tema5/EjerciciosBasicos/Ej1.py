'''
Escribe un programa que abra un fichero de texto llamado datos.csv,
 lea todo_ su contenido y lo muestre por pantalla.
'''

with open("fichero.txt", "r") as fichero:
    contenido = fichero.read()
    print(contenido)