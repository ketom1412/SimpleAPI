from flask import Flask, request #Flask module
import requests #python library also add into requirements.txt
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
import os
import json
import unirest
from random import randint
app=Flask(__name__)

@app.route("/cats", methods = ["GET", "POST"]) #allows the get and post method
def cats():
    account_sid = os.environ["Twiliosid"]
    auth_token = os.environ["Twiliotoken"]
    query = request.values.get("Body", None) #None is to check bounds
    
    
    #if query == None:
    #   query = "You+Mad+Bro" #fail safe if there isnt a body

    print query
    
    gifResp = requests.get("http://api.giphy.com/v1/gifs/search?q="+query+"&api_key=dc6zaTOxFJmzC")
    
    gifDict = json.loads(gifResp.text) #creates Json library
    
    data = gifDict.get("data")
    
    datalen = len(data)
    
    URLlist = []
    
    for x in range(0, datalen):
        singleGif = data[x]
        bitly_url = singleGif.get("bitly_gif_url")
        #URL = "<a href=" + bitly_url + ">My Gif </a><br />"
        URL = "Enjoy your gif! " + bitly_url
        URLlist.append(URL)
        #print URLlist
        #print URL
        #print bitly_url
        #print (x)
        
    Strin = URLlist[0]
    

    for y in range(1,datalen):
        Strin = Strin + "\n" + URLlist[y]

    #Your Account Sid and Auth Token from twilio.com/user/account
    #account_sid = "AC8ef789a8ae2e2e16b014cc1867a8cc3f"
    #auth_token  = "4920b01dfb7c159c6744f44e01f35f48"
    client = TwilioRestClient(account_sid, auth_token)

    try:
        message = client.messages.create(body=URLlist[randint(0,datalen)],
                                    to=request.values.get("From",None),
                                    from_="(415)915-7384")
    except TwilioRestException as e:
        print e
    
    print message.sid

    #print Strin

    return Strin
    print gifResp.status_code

@app.route("/article", methods = ["GET", "POST"]) #allows the get and post method
def article():
    
    articleResp = requests.get("https://www.reddit.com/api/v1/authorize?client_id=CLIENT_ID&response_type=TYPE&state=RANDOM_STRING&redirect_uri=URI&duration=DURATION&scope=SCOPE_STRING")


if __name__ == '__main__':
    app.run()