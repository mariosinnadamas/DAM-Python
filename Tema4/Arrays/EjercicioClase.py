# Ordenar una lista
palabras = ['python', 'java', 'c', 'javascript', 'go']
palabras_ordenadas = sorted(palabras, key=len) #orden por longitud de las palabras
print(palabras_ordenadas)

numeros = [-5, 3, -1, 2, -4]
numeros_ordenados = sorted(numeros,key=abs) # orden por valor absoluto
print(numeros_ordenados)


#Ordenar los numeros de una lista introduciendo primero los pares, ordenados
def ordenar_lista(lista):

    return lista

my_list = [2,3,5,1,7,9,6]
print(ordenar_lista(my_list))