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
