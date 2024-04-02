with open("./emails/name.txt") as names_file:
    names = names_file.readlines()
names = [name.strip() for name in names]

with open("email.txt") as letter_file:
    letter = letter_file.read()

for name in names:
    letter_with_name = letter.replace("name", name)
    with open(f"./output/letter_for_{name}.txt", mode="w") as new_letter:
        new_letter.write(letter_with_name)
