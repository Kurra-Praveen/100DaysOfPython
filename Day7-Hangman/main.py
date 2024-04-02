import random

words = ["mouse", "key", "mobile", "book"]
randomWord = random.choice(words)
print(randomWord)
blankSpaces = ["_" for i in randomWord]
print(blankSpaces)
endGame = False
lives = 6
while not endGame:
    userGuess = input("guess a character in the word").lower()
    if userGuess in randomWord:
        print("its in the word")
        blankSpaces[randomWord.index(userGuess)] = userGuess
    else:
        lives -= 1

    if lives == 0:
        endGame = True

    print(blankSpaces)
    if "_" not in blankSpaces:
        endGame = True
        print(f"{''.join(blankSpaces)}")
        print("Hurrah!! you win")
