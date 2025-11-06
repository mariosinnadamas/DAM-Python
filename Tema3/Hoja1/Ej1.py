'''
Crea una función llamada saludar que reciba dos argumentos por palabra clave:
- nombre (str)
- saludo (str), con valor por defecto "Hola"
La función debe devolver una cadena con el saludo seguido del nombre.
'''
# El asterisco obliga a que sean argumentos clave
def saludar(*, nombre:str, saludo: str = "hola"):
    cadena = saludo + " " +  nombre
    return cadena

print(saludar(nombre = "paco"))