'''
Crea una función llamada `tabla_multiplicar` que reciba:
- numero (int)
- hasta (int), como argumento por palabra clave, con valor por defecto 10
La función debe devolver una lista con la tabla de multiplicar del número hasta el valor indicado.
'''

def tabla_multiplicar(numero:int, *,hasta:int = 10) -> list[int]:
    return [numero * i for i in range(1,hasta+1)]

print(tabla_multiplicar(10))