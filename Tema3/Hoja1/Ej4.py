'''
Crea una función llamada `formatear_nombre` que reciba:
- nombre (str)
- apellido (str)
- orden (str), con valor por defecto "nombre_apellido" (el otro valor que podría tomar sería apellido_nombre)
La función debe devolver el nombre completo en el orden indicado.
'''

def formatear_nombre (nombre:str,apellido:str,orden:str="nombre_apellido" or "apellido_nombre"):
    if orden == "apellido_nombre":
        return apellido+ " " + nombre
    else:
        return nombre + " " + apellido

print(formatear_nombre(nombre="Mario", apellido="Saez", orden="apellido_nombre"))
print(formatear_nombre(nombre="Carlos", apellido="García"))