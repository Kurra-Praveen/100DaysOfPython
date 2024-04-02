with open("./emails/names.txt") as file:
    listOfNames = (file.read().replace('\n', "").split("."))
    listOfNames.pop()
print(listOfNames)
with open("./email.txt") as email:
    letter = email.read()

for name in listOfNames:
    nameLetter = letter.replace("name", name)
    with open(f"./output/{name} letter.txt", "w") as letter_sent:
        letter_sent.write(nameLetter)
