'''
Crea una función llamada `crear_usuario`que reciba los siguientes argumentos por palabra clave:
- nombre (str)
- email (str)
- activo (bool), con valor por defecto True
La función debe devolver una lista sólo de los usuarios activos con los datos del usuario en
el orden: [nombre, email, activo].
'''
def crear_usuario(*, nombre: str, email: str, activo: bool = True):
    if activo:
        return [nombre, email, activo]
    else:
        return []

print(crear_usuario(nombre = "Mario",email = "mario@gmail.com",activo = True))
print(crear_usuario(nombre = "Carlos",email = "carlos@gmail.com",activo = False))
print(crear_usuario(nombre = "Jose",email = "jose@gmail.com",activo = False))
print(crear_usuario(nombre = "Joshua",email = "joshua@gmail.com",activo = True))