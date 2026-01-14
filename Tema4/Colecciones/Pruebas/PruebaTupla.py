# Es una estructura de datos ordenada e inmutable que se usa para almacenar varios valores en una sola variable
#Características principales
# Ordenada: los elementos tienen una posición
# Inmutable: no se pueden modificar después de crearse
# Puede contener distintos tipos de datos

# Creación
dupla = (1, 2, 3)
otra_dupla = "a", "b", "c"

# Acceder a elementos
colores = ("rojo", "verde", "azul")
print(colores[0])  # rojo

# Distintos tipos de datos
persona = ("Ana", 25, True)

# Desempaquetado de duplas
x, y = (10, 20)
print(x)  # 10
print(y)  # 20

# Uso común: devolver varios valores
def operaciones(a, b):
    return a + b, a * b

suma, producto = operaciones(3, 4)

# Para actualizar una dupla lo más común es convertirla en lista, agregar o modificar y luego volver a convertir en tupla
dupla2 = (1, 2, 3)
lista = list(dupla2)
lista[0] = 10
dupla2 = tuple(lista)
print(dupla2)

# También se puede modificar concatenando duplas
dupla3 = (1, 2)
dupla3 += (3, 4)
print(dupla3)
print(type(dupla3))

# Las tuplas son convenientes de usar cuando queremos tener colecciones de datos que no queremos que se modifiquen

# Ejercicio de lista pasado a duplas, consiste en ordenar en función de la cantidad de letras que tenga la palabra

palabras = ['python', 'java', 'c', 'javascript', 'go']
duplas4 = [(palabra, len(palabra)) for palabra in palabras] # Crear duplas (palabra,longitud)
print(duplas4)

duplas_ordenadas = sorted(duplas4, key=lambda x: x[1]) #Ordenar la dupla
print(duplas_ordenadas)

palabras_ordenadas = [palabra for palabra, _ in duplas_ordenadas] # Me quedo solo con las palabras
print(palabras_ordenadas)

