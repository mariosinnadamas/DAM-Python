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

    # Obtengo las selecciones a partir de los números
    plato_sel = platos.get(plato)
    bebida_sel = bebidas.get(bebida)
    complemento_sel = complementos.get(complemento)
    metodo_sel = metodos_pago.get(metodo_pago)

    # Calculo el total
    total = plato_sel[1] + bebida_sel[1] + complemento_sel[1]

    # Muestro un resumen
    resultado = f"""
        **Resumen del pedido:**
        Plato: {plato_sel[0]} - ${plato_sel[1]:.2f}
        Bebida: {bebida_sel[0]} - ${bebida_sel[1]:.2f}
        Complemento: {complemento_sel[0]} - ${complemento_sel[1]:.2f}
        ----------------------------
        Total a pagar: ${total:.2f}
        Método de pago: {metodo_sel}
        """
    return resultado.strip()

plato = 1
bebida= 2
complemento= 1
metodo_pago = 2

print(menu_restaurante(plato, bebida, complemento, metodo_pago))