# Anagrama
def anagrama(cadena1, cadena2):
    diccionario1 = {}
    diccionario2 = {}
    for letra in cadena1.lower().replace(" ", ""):
        diccionario1[letra] = cadena1.count(letra)
    for letra in cadena2.lower().replace(" ", ""):
        diccionario2[letra] = cadena2.count(letra)
    if diccionario1 == diccionario2:
        return True
    else:
        return False

print(anagrama("agua", "gua a"))