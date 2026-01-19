'''
Muestra la longitud de la tupla
Comprueba si el número 3 está en la tupla.
'''
numeros = (1,2,3,4,5,6)
print("Longitud de la tupla: ", len(numeros))
for i in numeros:
    if i == 3:
        print(True)

'''
Crea una tupla con 10 números y cuenta cuántos son mayores que 5.
'''
numeros2 = (1,2,3,4,5,6,7,8,9,10)
contador = 0
for i in numeros2:
    if i > 5:
        contador+=1
print("Números mayores de 5: ", contador)

'''
Dada una tupla de números, crea una nueva tupla solo con los números pares.
'''
numeros_pares = []
for i in numeros2:
    if i % 2 == 0:
        numeros_pares.append(i)

tupla_pares = tuple(numeros_pares)
print(tupla_pares)

'''
Escribe un programa que reciba una tupla de palabras y devuelva la palabra más larga.
'''
tupla_palabras = ("esto", "es", "una", "nueva", "tupla")
palabra_mas_larga = tupla_palabras[0]
for palabra in tupla_palabras:
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra

print("La palabra más larga es: ", palabra_mas_larga)

'''
Dada una tupla con valores repetidos
Cuenta cuántas veces aparece cada número (usa un diccionario).
'''
t = (1, 2, 2, 3, 4, 4, 4, 5)
conteo = {}

for numero in t:
    if numero in conteo:
        conteo[numero] += 1
    else:
        conteo[numero] = 1

print(conteo)
