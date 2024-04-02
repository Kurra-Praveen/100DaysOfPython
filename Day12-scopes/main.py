import random

print("Welcome to number Game!! by guessing between 1 and 100")

userChoice = input("choose the difficulty level.Type 'easy' or 'hard' ").lower()


def level(lev):
    if lev == "easy":
        return 10
    elif lev == "hard":
        return 5
    else:
        return 0


Userattempts = level(userChoice)
randomNumber = random.randint(1, 100)


def playGame():
    attempts = Userattempts
    while attempts != 0:
        print(f"you have {attempts} attempts remaining to guess the number  ")
        guess = int(input("make a guess.."))
        if randomNumber == guess:
            print("hurray you make a correct guess")
            break
        elif guess > randomNumber:
            print("too high")
            print("guess again")
        elif guess < randomNumber:
            print("too low")
            print("guess again")
        attempts -= 1


playGame()
