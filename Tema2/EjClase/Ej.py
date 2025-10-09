while(True):
    n = int(input("Introduce un numero positivo: "))

    #Si el numero es negativo se detiene el programa
    if n < 0:
        print("Programa finalizado")
        break

    #Recorro
    for i in range (1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)