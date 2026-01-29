'''
Escribe un programa que cree un fichero nuevo.txt y
escriba en él varias líneas de texto introducidas por el usuario.
'''
with open ("fichero2.txt","w") as fichero:
    while True:
        linea = input("Escribe una línea (o introduce fin para terminar): ")
        if linea.lower() == "fin":
            break
        fichero.write(linea+"\n")