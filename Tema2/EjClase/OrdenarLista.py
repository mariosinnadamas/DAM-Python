numeros = []

for n in range(0,5):
    n = int(input("Introduce un numero: "))
    numeros.append(n)

#Orden de manera manual
for i in range(len(numeros)):
    for j in range(i+1,len(numeros)):
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]
print(numeros)


#Orden de manera automática
numeros.sort()
print(numeros)
