import os
from flask import Flask, redirect, request, url_for, render_template
from dotenv import load_dotenv
load_dotenv()
Token = os.getenv("TOKEN")

app = Flask(__name__)


@app.route('/')
def intro1():
    return "<h1>Hello World </h1>"


@app.route('/webhook', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        print(request)
        return "", 200
    else:
        return "", 400


if __name__ == '__main__':
    app.run(debug=True)
