# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def helo_world():
#     return "hello world"

def decorator(function):
    def delay():
        print("Hello Byee")
        x = function()
        print(x)

    return delay()


@decorator
def message():
    return "before"



