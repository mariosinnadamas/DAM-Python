'''
Escribe un programa que abra un fichero datos.csv
y permita al usuario añadir nuevas líneas de texto al final.
'''

with open("fichero2.txt", "a") as fichero:
    while True:
        linea = input("Escribe una línea (introduce fin para terminar): ")
        if linea.lower() == "fin":
            break
        fichero.write(linea+"\n")