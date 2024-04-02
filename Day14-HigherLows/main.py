import random
from gameData import data as data


def randomData():
    return random.choice(data)


def formatData(account):
    accountName = account['name']
    accountDesc = account['description']
    accountCountry = account['country']
    return f"{accountName}, a {accountDesc}, from {accountCountry}"


def checkAnswer(guess, afollowerCount, bfollowerCount):
    if afollowerCount > bfollowerCount:
        return guess == "a"
    else:
        return guess == "b"


choice1 = randomData()
isGameOn = True
score = 0
while isGameOn:
    choice2 = randomData()
    while choice1 == choice2:
        choice2 = randomData()
    count1 = choice1['followers_count']
    count2 = choice2['followers_count']
    print(f"Compare A : {formatData(choice1)}")
    print(" ")
    print("vs")
    print(" ")
    print(f"Compare B: {formatData(choice2)}")
    userGuess = input("Who has more followers ? Type 'A' or 'B' ").lower()

    isGameOn = checkAnswer(userGuess, count1, count2)
    if isGameOn:
        score += 1
        print(f"Nice Guess..your score is {score}")
        choice1 = choice2

    else:
        print(f"Game over !!.your final score is {score}")

