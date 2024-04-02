import pandas

data_f = pandas.read_csv("nato_phonetic_alphabet.csv")

list_of_data = {row.letter: row.code for (index, row) in data_f.iterrows()}


def alpha():
    name = input("enter your name").upper()
    try:
        natoAlpha = [list_of_data[letter] for letter in name]
    except KeyError:
        print("sorry,only Alphabets are allowed")
        alpha()
    else:
        print(natoAlpha)

alpha()

# for char in name:
#     for index, row in data_f.iterrows():
#         if row.letter == char:
#             list_of_data[row.letter] = row.code
