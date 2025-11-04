'''
Crea una función llamada `calcular_descuento' que reciba:
- precio_original (float)
- descuento (float), como argumento por palabra clave, con valor por defecto 10
La función debe devolver el precio final tras aplicar el descuento.
'''

def calcular_descuento(precio_original:float, *, descuento:float = 10):
    return precio_original*(1-descuento/100)

print(calcular_descuento(200))
print(calcular_descuento(150, descuento=20))