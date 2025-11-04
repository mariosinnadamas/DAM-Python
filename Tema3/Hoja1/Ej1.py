'''
Crea una función llamada saludar que reciba dos argumentos por palabra clave:
- nombre (str)
- saludo (str), con valor por defecto "Hola"
La función debe devolver una cadena con el saludo seguido del nombre.
'''
def saludar(nombre, saludo):
    cadena = saludo + " " +  nombre
    return cadena

print(saludar("paco", "hola"))