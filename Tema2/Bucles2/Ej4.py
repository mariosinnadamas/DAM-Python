inventario = {"manzanas":0, "peras":0,"plátanos":0}
while(True):
    try:
        print("MENÚ")
        print("1. Añadir stock (Manzanas, peras o plátanos)")
        print("2. Vender producto")
        print("3. Mostrar inventario")
        print("4. salir del inventario")
        dec = str(input()).strip()
        #Añadir cantidad
        if dec == '1':
            producto = input("Introduce el producto (manzanas, peras o plátanos)").lower().strip()
            if producto not in inventario:
                print("ERROR: Producto no válido")
                continue

            try:
                cantidad = int(input(f"Cantidad de {producto} a añadir: "))
                if cantidad <=0:
                    raise ValueError("ERROR: La cantidad debe ser positiva")
                inventario[producto] +=cantidad
                print(f"Cantidad añadida correctamente")
            except ValueError as e:
                print(e)

        elif dec == '2':
            producto = input("Introduce el producto a vender (manzanas, peras, plátanos): ").lower().strip()
            if producto not in inventario:
                print("Producto no válido.")
                continue

            try:
                cantidad = int(input(f"Cantidad de {producto} a vender: "))
                if cantidad <= 0:
                    raise ValueError("La cantidad debe ser positiva.")
                if cantidad > inventario[producto]:
                    raise ValueError(f"No hay suficiente stock de {producto}. Stock actual: {inventario[producto]}")
                inventario[producto] -= cantidad
                print(f" Se vendieron {cantidad} {producto}. Quedan {inventario[producto]}")
            except ValueError as e:
                print(f" Error: {e}")
        elif dec == '3':
            for producto,cantidad in inventario.items():
                print(f"-{producto.capitalize()}: {cantidad}")
        elif dec == '4':
            break
        else:
            raise ValueError("Opción no válida")
    except ValueError as e:
        print(e)