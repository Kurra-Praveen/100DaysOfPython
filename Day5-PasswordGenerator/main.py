import random

small = list(map(chr, range(97, 123)))
capital = list(map(chr, range(65, 91)))
numbers = [i for i in range(0, 10)]
specialCharacters = ["!", "@", "#", "$", "%", "^", "&", "*", "{", "}"]
noOfLetters = int(input("how many letters you want "))
noOfNumbers = int(input("how many numbers you want "))
noOfSpecialChar = int(input("how many special you want "))
string = ""
for i in range(noOfLetters):
    smallChar = random.choice(small)
    capitalChar = random.choice(capital)

    string += smallChar
    string += capitalChar

for i in range(noOfNumbers):
    string += str(i)

for i in range(noOfSpecialChar):
    specialc = random.choice(specialCharacters)
    string += specialc
listOfChar = list(string)
random.shuffle(listOfChar)
password = ''.join(listOfChar)
print(password)
