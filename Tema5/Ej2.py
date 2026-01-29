'''
Escribe un programa que abra un fichero datos.txt y cuente cuántas líneas tiene el archivo.
'''

with open ("fichero.txt","r") as fichero:
    lineas = fichero.readlines()
    print(f"Número de lineas: {len(lineas)}")