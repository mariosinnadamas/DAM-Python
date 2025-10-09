try:
    nota = float(input("Introduce tu nota: "))
    if 0 <= nota <= 4.9:
        print("SUSPENSO")
    elif 5 <= nota <= 6.9:
        print("APROBADO")
    elif 7 <= nota <= 8.9:
        print("NOTABLE")
    elif 9 <= nota <= 10:
        print("SOBRESALIENTE")
    else:
        print("No puede ser una nota negativa o mayor que 10")

except ValueError:
    print("ERROR: Introduce un numero entero")