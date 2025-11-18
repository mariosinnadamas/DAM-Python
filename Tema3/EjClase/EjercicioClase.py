def saludar_amigos(*nombres):
    for nombre in nombres:
        print(f"¡Hola {nombre}!")

# Lista de amigos
mis_amigos = ["Ana", "Carlos", "Maria","Jose","Jimmy"]

# Usar * para pasar la lista como argumentos separados
saludar_amigos(*mis_amigos)