'''
Crea una función llamada `filtrar_pares' que reciba una lista de números enteros y devuelva
una nueva lista solo con los números pares.
'''

def filtrar_pares(numeros:list[int]) -> list[int]:
    return [n for n in numeros if n%2 ==0]

numeros = [1,2,3,4,5,6,7,8,9,10]

print(filtrar_pares(numeros))