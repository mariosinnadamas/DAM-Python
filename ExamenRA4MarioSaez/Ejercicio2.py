#n es el número a buscar
#Versión 1
def calculaPosicion(n,datos):
    posiciones_de_n=[]
    for i in datos:
        if i == n:
            posiciones_de_n.append(datos.index(i))


    if len(posiciones_de_n) == 0:
        return -1

    return posiciones_de_n

#Version 2
def calculaPosicionAniade(n,datos):

    for i in datos:
        if i != n:
            datos.append(n)
            return datos
    return -1


datos=[1,1,3,3,7,5,4,2,5,10]
print(calculaPosicion(2,datos))