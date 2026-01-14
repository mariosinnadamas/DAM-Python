'''
Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable. Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:

El caballero tiene el doble de vida y defensa que un guerrero.
El guerrero tiene el doble de ataque y alcance que un caballero.
El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.
Muestra como quedan las propiedades de los tres personajes.
'''

estadistica_base = 2;

caballero = { #Doble de vida y defensa que un guerrero
    "Vida" :estadistica_base,
    "Defensa" : estadistica_base,
    "Alcance":estadistica_base,
    "Ataque":estadistica_base
}

guerrero = {
    "Ataque" : estadistica_base, #Doble de ataque y alcance que un caballero
    "Alcance" : estadistica_base,
    "Vida": estadistica_base,
    "Defensa" : estadistica_base
}

arquero = {
    "Vida": estadistica_base, #Misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de alcance
    "Ataque": estadistica_base,
    "Defensa" : estadistica_base,
    "Alcance": estadistica_base
}

caballero ["Vida"] = guerrero["Vida"]*2
caballero ["Defensa"] = guerrero["Defensa"]*2

guerrero["Ataque"] = caballero["Ataque"]*2
guerrero["Alcance"] = caballero["Alcance"]*2

arquero["Vida"] = guerrero ["Vida"]
arquero["Ataque"] = guerrero ["Ataque"]
arquero["Defensa"] = guerrero ["Defensa"]/2
arquero["Alcance"] = guerrero ["Alcance"]*2

print("Caballero:", caballero)
print("Guerrero:", guerrero)
print("Arquero:", arquero)
