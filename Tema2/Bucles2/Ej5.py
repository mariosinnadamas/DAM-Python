def menu_restaurante(plato, bebida, complemento, metodo_pago):
    # Menús de opciones y precios
    platos = {
        1: ("Pizza", 8.50),
        2: ("Hamburguesa", 7.00),
        3: ("Ensalada", 6.00)
    }

    bebidas = {
        1: ("Agua", 1.50),
        2: ("Refresco", 2.00),
        3: ("Cerveza", 2.50)
    }

    complementos = {
        1: ("Patatas", 2.50),
        2: ("Ensalada pequeña", 2.00),
        3: ("Pan de ajo", 3.00)
    }

    metodos_pago = {
        1: "Efectivo",
        2: "Tarjeta"

    }

plato = 1
bebida= 2
complemento= 1
metodo_pago = 2
print(menu_restaurante(plato, bebida, complemento, metodo_pago))