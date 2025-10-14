'''
Crea un programa que almacene en una lista las notas de un grupo de alumnos. Utiliza un
bucle for para recorrer la lista y:
1. Contar cuántos alumnos han aprobado (nota ≥ 5).
2. Calcular la nota media del grupo.
3. Mostrar la nota más alta y la más baja.
'''

notas = [3.6,9,5,3.4,7]
aprobado = 0
media = 0
alta = 0
baja = 10
for i in notas:
    if i >= 5:
        aprobado+=1
    if i > alta:
        alta = i
    if i < baja:
        baja = i

    media = (media+i)

media = media/len(notas)

print("Cantidad de aprobados: ", aprobado)
print("Media: ",media)
print("Nota más alta: ", alta)
print("Nota más baja: ", baja)
