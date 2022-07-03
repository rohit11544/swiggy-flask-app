import os
from flask import Flask, redirect, request, url_for, render_template
from dotenv import load_dotenv
load_dotenv()
Token = os.getenv("TOKEN")

app = Flask(__name__)


@app.route('/')
def intro1():
    return "<h1>Hello World </h1>" + Token


@app.route('/webhook', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        args = request.args
        mode = args.get("hub.mode")
        token = args.get("hub.token")
        challenge = args.get("hub.challenge")
        print("request came")
        if mode and token:
            if mode == "subscribe" and token == Token:
                print("WEBHOOK_VERIFIED")
                return challenge, 205
            else:
                return "token not matching", 401
        else:
            return "mode or token is empty", 402
    if request.method == 'POST':
        print("its a post request and its working")
        print(request.json)
        print("request json printeddddddd!!!!!!!!!")
        return "its a post request", 205


if __name__ == '__main__':
    app.run(debug=True)
