import os
from flask import Flask, request
import requests
from dotenv import load_dotenv
load_dotenv()
Token = os.getenv("TOKEN")

app = Flask(__name__)


@app.route('/')
def intro1():
    return "<h1>Hello World from macOS and heroku!!</h1>" + Token


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
                return challenge, 200
            else:
                return "token not matching", 401
        else:
            return "mode or token is empty", 402
    if request.method == 'POST':
        print("its a post request and its working")
        print(request.json)
        rj = request.json
        mtype = rj['entry'][0]['changes'][0]['value']['messages'][0]['type']
        if(mtype == 'audio'):
            mid = rj['entry'][0]['changes'][0]['value']['messages'][0]['audio']['id']
        else:
            mid = 'no mid due to its a text msz!!!!'
        print("media iddddd " + mid)
        print("media type "+ mtype)
        print("request json printeddddddd!!!!!!!!!")
        return "its a post request", 205


if __name__ == '__main__':
    app.run(debug=True)
