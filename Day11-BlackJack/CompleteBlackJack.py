import random


def dealCards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculateScore(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    return sum(cards)


def compare(userScore, computerScore):
    if userScore == computerScore:
        return "Draw"
    elif computerScore == 0:
        return "Loose,Opponent has black jack"
    elif userScore == 0:
        return "you win the game with BlackJack"
    elif userScore > 21:
        return "you went over ,You loose the game "
    elif computerScore > 21:
        return "opponent went over..you win the game"
    elif userScore > computerScore:
        return "you wins"
    else:
        return "you loose"


userCards = []
computerCard = []
isGameOver = False

for _ in range(2):
    userCards.append(dealCards())
    computerCard.append(dealCards())
userScore = calculateScore(userCards)

computerScore = calculateScore(computerCard)
while not isGameOver:
    userScore = calculateScore(userCards)

    print(f"your cards are {userCards} and your score is {userScore}")

    print(f"computer first card are {computerCard[0]} ")

    if userScore == 0 or computerScore == 0 or userScore > 21:
        isGameOver = True
    else:
        choice = input("type 'y' to get another card ,or type 'n' to pass").lower()
        if choice == "y":
            userCards.append(dealCards())
        else:
            isGameOver = True
while computerScore != 0 and computerScore < 17:
    computerCard.append(dealCards())
    computerScore = calculateScore(computerCard)
print(f"your crads are {userCards} and your score is {userScore}")
print(f"computer cards are  {computerCard} and computer score is {computerScore}")

print(compare(userScore, computerScore))
