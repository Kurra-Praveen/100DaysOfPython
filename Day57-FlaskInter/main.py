import random

from flask import Flask, render_template
import time
import requests

AGE_API = 'https://api.agify.io'
GENDER_API = 'https://api.genderize.io'

app = Flask(__name__)


@app.route("/guess/<name>")
def guess(name):
    parameter = {"name": name}
    ageAPi = requests.get(url=AGE_API, params=parameter)
    genderApi = requests.get(url=GENDER_API, params=parameter)
    age = ageAPi.json()['age']
    gender = genderApi.json()['gender']
    return render_template('index.html', age=age, gender=gender, name=name)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/guess')
def sample():
    return "Hello world"


if __name__ == "__main__":
    app.run(debug=True)
