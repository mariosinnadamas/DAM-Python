'''
Crea un diccionario con el nombre y la edad de 5 personas.
- Muestra todas las claves.
- Muestra todos los valores.
'''

nombreEdad = {
    "Mario": 23,
    "Adrián": 25,
    "Jaime": 23,
    "Christian": 23
}
print(nombreEdad.keys())
print(nombreEdad.values())

'''
- Agrega un nuevo producto.
- Modifica el precio de un producto existente.
- Elimina un producto.
'''
productos = {"pan": 1.2, "leche": 0.9, "huevos": 2.5}
productos["azúcar"] = 2.0
productos["pan"] = 1.0
productos.pop("huevos")
print(productos)

'''
Escribe un programa que cuente cuántas veces aparece cada letra en una palabra y lo guarde en un diccionario.
'''
palabra = "supercalifragilistocuespialidoso"
cantidadLetras = {}

for letra in palabra:
    if letra in cantidadLetras:
        cantidadLetras[letra] += 1
    else:
        cantidadLetras[letra] = 1

print(cantidadLetras)

'''
Dado un diccionario de estudiantes y sus notas, muestra el nombre del estudiante con la nota más alta.
'''

estudiantes = {
    "Pedro": 2.0,
    "Jose": 9.0,
    "Carlos": 5.0
}

estudiante = max(estudiantes,key=estudiantes.get)
print(estudiante)

'''
Escribe un programa que cuente cuántas veces aparece cada palabra en una frase.
'''
frase = "Cuántas veces aparece cada palabra en una frase"
contador = {}
palabras = frase.split()
for i in palabras:
    if i in contador:
        contador[i]+=1
    else:
        contador[i]=1

print(contador)
'''
Crea un diccionario a partir de dos listas:
'''
nombres = ["Ana", "Luis", "Pedro"]
notas = [8, 7, 9]
combinacion = {}
for nombre, nota in zip(nombres,notas):
    combinacion[nombre] = nota
print(combinacion)

'''
Escribir un programa que cree un diccionario simulando una
cesta de la compra. El programa debe preguntar el artículo y
su precio y añadir el par al diccionario, hasta que el usuario
decida terminar. Después se debe mostrar por pantalla la lista de
la compra y el coste total, con el siguiente formato
'''

cesta_de_la_compra ={
    "manzana": 3,
    "kiwi": 7,
    "pera":2.5
}

coste = 0
for nombre, precio in cesta_de_la_compra.items():
    coste += precio

print(coste, "€")