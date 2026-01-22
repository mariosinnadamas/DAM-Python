def cuenta_vocales(cadena):
    contador_a=cadena.count('a')
    contador_e=cadena.count('e')
    contador_i=cadena.count('i')
    contador_o=cadena.count('o')
    contador_u=cadena.count('u')
    
    if contador_a == 1:
         print('La vocal a aparece ',contador_a, "vez")
    else:
        print('La vocal a aparece ',contador_a, "veces")

    if contador_e==1:
        print('La vocale e aparece ',contador_e, "vez")
    else:
        print('La vocale e aparece ',contador_e, "veces")

    if contador_i==1:
        print('La vocale i aparece ', contador_i, "vez")
    else:
        print('La vocale i aparece ', contador_i, "veces")

    if contador_o==1:
        print('La vocale o aparece ', contador_o, "vez")
    else:
        print('La vocale o aparece ', contador_o, "veces")

    if contador_u==1:
        print('La vocale o aparece ', contador_u, "vez")
    else:
        print('La vocale o aparece ', contador_u, "veces")
    return

#Cadena de prueba
cadena = "me duele el esternocleidomastoideo"

print(cuenta_vocales(cadena))