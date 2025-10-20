'''
Escribes dos números y te devuelve la suma en binario
'''

#Esto es lo que se me ocurrió a mi
def add_binary(a,b):
    suma = a + b
    nBinario = ""
    while suma >0:
        resto = suma % 2
        cociente = suma // 2
        suma = cociente
        nBinario += str(resto)
    return nBinario[::-1]

#Esto es la respuesta más dada xd
def add_binary2(a,b):
    return bin(a+b)[2:]

print(add_binary(5,5))
print(add_binary2(5,5))