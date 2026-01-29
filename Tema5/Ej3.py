'''
Crea un programa que lea el fichero datos.txt y cuente
cuántas veces aparece una palabra específica que el usuario introduce
'''

palabra = input("Introduce una palabra que contar en el fichero si existe: ")
with open ("fichero.txt","r") as fichero:
    contenido = fichero.read()
    ocurrencias = contenido.count(palabra)
    print(f"La palabra {palabra} aparece {ocurrencias} veces")