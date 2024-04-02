listOfAlphabets=[chr(i)  for i in range(97,123)]
direction = input("type 'encode' to encrypt ,type 'decode' to decrypt \n ")
text = input("enter the text you want \n").lower()
shift = int(input("type shift amount "))

newMesage = []


def encrypt(message, shiftamount):
    starting = 97
    for letter in message:
        position = ord(letter) + shiftamount
        if position > 122:
            newPosition = (position - 122)-1
            updatedLetter = chr(starting+newPosition)
            newMesage.append(updatedLetter)
        else:
            updatedLetter = chr(ord(letter) + shiftamount)
            newMesage.append(updatedLetter)


encrypt(text, shift)
print(''.join(newMesage))

# number = int(input("enter a number to check prime number:"))
# print(round(number / 2))
#
#
# def primeNumber(n):
#     coumt = 0
#     for i in range(2, round(n / 2)):
#         print(i)
#         if n % i == 0:
#             coumt += 1
#
#     if coumt > 0:
#         print("its a not prime number")
#     else:
#         print("its  a prime number")
#
#
# primeNumber(number)
