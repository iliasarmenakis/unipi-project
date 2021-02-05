file = input("give an ascii file ")
for i in range(len(file)):
    letter = file[len(file)-i -1] #taking the characters from back to front
    number = ord(letter) # translating 
    number2 = 128 - number # finding the specular number 
    ascii = chr(number2) # Retranslation
    print(ascii , end ="") # print result