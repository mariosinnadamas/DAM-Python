def find_it(seq):
    for i in seq:
        count = seq.count(i)
        if count % 2 !=0:
            n = i
    return n

#Tiene que devolver 3, porque es el número que aparece un número impar de veces
seq = [1,2,2,3,3,3,4,3,3,3,2,2,1]

print(find_it(seq))