#Constantes
print(123)
#Variables, misma nomenclatura que en java
x = 12.2
#Expresiones (** es potencia)
x = x + 2
x = x - 2
x = x * 2
x = x / 2
x = x ** 2
#Existe el orden de de operadores
# () -> ** -> * -> +
y = 1
y = 1+2*3-4/5**6
print(y)
#Concatenar strings
eee = "Hello"
eee = eee + "there"
#Ver el tipo de dato que es una variable
print(type(eee))
print(type(1.0))
print(type(1))
#Las divisiones de tipo Int generan resultados de float
print(10/2)
#Entradas del usuario
nam = input("Who are you? ")
print("Welcome", nam)
#Casteo de datos
cadenaN = "123"
print(type(cadenaN))
# print(sval + 1) esto daría error
num = int(cadenaN)
print(type(num))
print(num+1)
