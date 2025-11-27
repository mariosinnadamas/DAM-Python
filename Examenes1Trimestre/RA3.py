from operaciones import info_argumentos

import operaciones as op
#Ejercicio 1
print(info_argumentos(1,2,3,4,5,6,7)) #Solo numeros
#print(info_argumentos(1,2,3,4,5,6,"a")) #Con letras dice que error en el argumento (porque solo admite int)
print(op.divisibles3(1,2,3,4,5,6,7)) #Solo numeros
#print(op.divisibles3(1,2,3,4,5,6,"a")) #Con letras salta un error (porque solo admite int)
print(op.histograma(4,9,7))

#Ejercicio 2
print(op.coste_envio(0.5)) #Si pesa menos de 1 kilo no tiene incremento de precio
print(op.coste_envio(0.5, urgente = True)) #Si pesa menos de 1 kilo y es urgente
print(op.coste_envio(2)) #Si pesa más de un 1 kilo tiene un incremento de 2 euros por kilo
print(op.coste_envio(2,urgente=True)) #Si pesa más de un 1 kilo y es urgente

#Ejercicio3
try:
    horas = int(input("Introduce las horas: "))
    minutos = int(input("Introduce los minutos: "))
    segundos = int(input("Introduce los segundos: "))
    print(op.convertir_segundos(horas,minutos,segundos))
except ValueError:
    print("El valor ingresado no es valido")


