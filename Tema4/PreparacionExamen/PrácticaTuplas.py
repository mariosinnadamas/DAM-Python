numeros = (1,2,3,4,5,6)
print(numeros[0])
print(numeros[-1]) #último
print(sum(numeros))
print(max(numeros))
print(min(numeros))
lista_numeros = list(numeros)
lista_numeros.append(6)
numeros = tuple (lista_numeros)
print(numeros)
contador = 0
for n in numeros:
    if n == 6:
        contador+=1
print("El 6 aparece ", contador)
