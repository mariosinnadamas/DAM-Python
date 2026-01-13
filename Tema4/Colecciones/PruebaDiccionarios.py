
# Crear vacío
personas = {}

# Con elementos
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}

# Acceder a valores
print(persona["nombre"])   # Ana
print(persona["edad"])     # 25

#Si una clave no existe da error, para evitarlo:
print(persona.get("pais", "No definido"))

#Modificar un valor:
persona["edad"] = 26

#Modificar una clave:
persona["pais"] = "España"

# Eliminar elementos
del persona["ciudad"]
persona.pop("edad")

#Recorrer claves:
for clave in persona:
    print("Clave: " + clave)

#Recorrer valores
for valor in persona.values():
    print("Valor: " + valor)

#Recorrer claves y valores:
for clave, valor in persona.items():
    print(clave, ":", valor)

#Ejemplo práctico
texto = "hola hola python diccionarios python"
palabras = texto.split()

contador = {}

for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

print(contador)

#Funciones útiles
len(persona)          # Número de elementos
"nombre" in persona   # True si existe la clave
persona.keys()        # Todas las claves
persona.values()      # Todos los valores
persona.items()       # Claves y valores

