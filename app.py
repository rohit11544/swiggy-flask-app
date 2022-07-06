import os
from os.path import exists
from flask import Flask, request
from helper import download_file,sendMsz
from dotenv import load_dotenv
load_dotenv()

is_prod = os.environ.get('IS_HEROKU', None)

if is_prod:
    #here goes all your heroku config
    Token = os.environ.get('TOKEN', None)
    AccessToken = os.environ.get('ACCESS_TOKEN', None)
else:  
    Token = os.getenv("TOKEN")
    AccessToken = os.getenv("ACCESS_TOKEN")

app = Flask(__name__)


@app.route('/')
def intro1():
    if is_prod:
        return "<h1>Hello World from macOS and heroku and corrected!!</h1> <br/> Token <h2>"+Token+"</h2> <br/> Access_Token <h2>"+AccessToken+"</h2>"
    else:
        return "not working"


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
            print("media iddddd " + mid)
            file_path = download_file(AccessToken,mid)
            print('downloaded with file name : ok ', file_path)
            file_exists = exists(file_path)
            if file_exists:
                print("it worked man!!!!", file_exists)
                cart = "cart output will be stored here!!!"
                phone_id = rj['entry'][0]['changes'][0]['value']['statuses'][0]['recipient_id'] # phone number
                phone_number_id = rj['entry'][0]['changes'][0]['value']['metadata']['phone_number_id'] # phone number id
                sendMsz_res = sendMsz(AccessToken,phone_id,phone_number_id,cart)
                if sendMsz_res==200:
                    print("cart sent successifully!!!!")
                else:
                    print("try another code!")
            else:
                print("try another way man!!!", file_exists)
        else:
            print("its not an audio msz!!!")
        return "its a post request", 205


if __name__ == '__main__':
    app.run(debug=True)
