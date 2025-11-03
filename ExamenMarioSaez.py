def ej1():
    nombres1 = ["Jose", "Paco", "Infanta", "Tobias"]
    nombres2 = ["Elena", "Jaime", "Maria", "Jose"]
    contador = 0

    for i in nombres1:
        for j in nombres2:
            if i == j:
                print(f"No pueden ser dos nombres iguales: {i} {j}")
                continue  # salta a la siguiente combinación, no suma contador
            try:
                if i == "Infanta" and j == "Elena":
                    raise ValueError(f"{i} {j}: IES en Galapagar con estudios de formación profesional")
                # si no hay excepción, se imprime la combinación
                print(i, j)
            except ValueError as e:
                print("Error:", e)
            finally:
                # se suma el contador en todos los casos excepto nombres iguales
                contador += 1

    print("Número total de combinaciones realizadas:", contador)

def ej2():
    precios = []
    pre = 0
    count = 0
    suma = 0
    mayor = 0

    while pre != 9999.99:
        try:
            pre = float(input("Introduce precio del producto (9999.99 para finalizar): "))
            if pre == 9999.99:
                break
            elif pre < 0:
                print("No puedes poner un precio negativo.")
                continue
            else:
                precios.append(pre)
        except ValueError:
            print("Introduce un precio válido (número).")

    for i in precios:
        if i >= 10:
            print(i)
            suma += i
            count += 1
            if i > mayor:
                mayor = i

    try:
        print("Contador:", count)
        media = suma / count
        print("Media:", media)
    except ZeroDivisionError:
        print("No se puede dividir entre 0.")

    print("Precio más alto:", mayor)


def ej3():
    n1 = 0
    n2 = 0
    for i in range (0,10,1):
        if i == 0:
            n1 = i
            print(n1)
        elif i == 1:
            n2 = i
            print(n2)
        else:
            n3 = n1 +n2
            print(n3)
            n1 = n2
            n2 = n3

ej1()
ej2()
ej3()