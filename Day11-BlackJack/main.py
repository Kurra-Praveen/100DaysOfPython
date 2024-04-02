import random

print("welcome to black jack")
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

user_cards += random.sample(cards, 2)
computer_cards += random.sample(cards, 2)

flag = True


def sumOfCards(cards):

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return sum(cards)


print(sumOfCards([11, 1, 11, 1]))

while flag:
    print(f"your cards are {user_cards} and your current score is {sum(user_cards)}")
    print(f"computer first card is {computer_cards[0]}")
    if sumOfCards(user_cards) == 21 and sumOfCards(computer_cards) < 21:
        print("hurrah!! you win the game ")
        flag = False
    elif sumOfCards(computer_cards) == 21 or sumOfCards(user_cards) > 21:
        print("sorry !! you loose the game ")
        print(f"computer cards are {computer_cards}")
        flag = False
    elif sumOfCards(user_cards) == sumOfCards(computer_cards):
        print("match drawn !!")
    else:
        choice = input("type 'y' for take another card or type 'n' for pass ").lower()
        if choice == "y":
            user_cards += random.sample(cards, 1)
        if sum(computer_cards) < 17 and sum(user_cards) < 21:
            computer_cards += random.sample(cards, 1)
