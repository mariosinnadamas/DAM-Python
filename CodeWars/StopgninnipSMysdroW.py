def spin_words(sentence):
    newString = ""
    reverseWord = ""
    words = str(sentence).split()
    for i in words:
        if len(i) >= 5 and newString == "":
            reverseWord = i[::-1]
            newString = reverseWord
        elif len(i) >= 5:
            reverseWord = i[::-1]
            newString = newString + " " + reverseWord
        else:
            if newString == "":
                newString = i
            else:
                newString = newString + " " + i
    return newString

#Invertir las palabras que tengan más de 5 letras
print(spin_words("This sentence is a sentence"))