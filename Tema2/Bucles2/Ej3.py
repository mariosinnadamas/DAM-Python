def primer_numero():
    for i in range(0,200, 7):
        if 80 < i < 200:
            n = i
            break
    return n
print(primer_numero())