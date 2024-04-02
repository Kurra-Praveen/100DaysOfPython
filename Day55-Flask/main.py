import random

from flask import Flask

app = Flask(__name__)
random_choice = random.randint(0, 9)
print(random_choice)


@app.route('/')
def home_page():
    return '<h1>Guess a number Between 0-9 ' \
           '<br />' \
           '<img src=" https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif ">'


@app.route('/<int:guess>')
def checking(guess):
    if guess == random_choice:
        return "<h1 style='color: purple'>You found me!!<h2>" \
               "<br />" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif guess > random_choice:
        return "<h3>Too High" \
               "<br />" \
               "<img src= 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif guess < random_choice:
        return "<h3>Too Low" \
               "<br />" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' >"


if __name__ == "__main__":
    app.run(debug=True)
