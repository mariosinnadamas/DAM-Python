#Condicionales
x = 5
y = 6
if x > y:
    print(x)
else:
    print(y)
#Decisiones de un camino
if x==5:
    print("X vale: ", x)

#For con if
if x>2:
    print("Mayor que 2")
print("Hecho con if")

for i in range(5):
    print(i)
    if i > 2:
        print("Mayor que 2")
    print("Hecho con Fori")

#Multiples caminos
if x < 2 :
    print('small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')

#Try/Except
astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1

print('Mal:', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Bien:', istr)