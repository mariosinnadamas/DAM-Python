'''
Crea una lista con 10 números y:
Muestra la suma de todos los elementos.
Muestra el número mayor y el menor.
'''
list = [1,2,3,4,5,6,7,8,9,10]
print(sum(list))
print(max(list))
print(min(list))

'''
Ordena la lista alfabéticamente.

Elimina el nombre "Pedro".

Agrega un nuevo nombre al final.
'''
nombres = ["Ana", "Luis", "Pedro", "Marta", "Juan"]
nombres.sort()
print(nombres)
for nombre in nombres:
    if nombre == "Pedro":
        nombres.pop()
nombres.append("Chocolatero")
print(nombres)

'''
Escribe un programa que cree una lista con los números pares del 1 al 50.
'''
numeros_pares = []
for i in range(1,50):
    if i % 2 == 0:
        numeros_pares.append(i)

print(numeros_pares)

'''
Dada una lista de números, crea una nueva lista con los números elevados al cuadrado.
'''
numeros_cuadrados = []
for i in numeros_pares:
    numeros_cuadrados.append(i**2)

print(numeros_cuadrados)