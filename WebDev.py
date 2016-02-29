from flask import Flask, request #Flask module
import requests #python library also add into requirements.txt
import json
import unirest
from jinja2 import Environment, PackageLoader
app=Flask(__name__)

@app.route("/cats")
def cats():
    query = request.values.get("Body", None) #None is to check bounds
    
    gifResp = requests.get("http://api.giphy.com/v1/gifs/search?q="+query+"&api_key=dc6zaTOxFJmzC")
    
    gifDict = json.loads(gifResp.text) #creates Json library
    
    data = gifDict.get("data")
    
    datalen = len(data)
    
    URLlist = []
    
    for x in range(0, datalen):
        sin
        bitly_url = singleGif.get("bitly_gif_url")
        URL = "<a href=" + bitly_url + ">My Gif </a><br />"
        URLlist.append(URL)
        #print URLlist
        #print URL
        #print bitly_url
        #print (x)
        
    Strin = URLlist[0]

    for y in range(1,datalen):
        Strin = Strin + "\n" + URLlist[y]

    #print Strin

    return Strin
    print gifResp.status_code

@app.route("/yoda")
def yoda():
    query = request.values.get("Body", None)
    response = unirest.get("https://yoda.p.mashape.com/yoda?sentence="+query+".",headers={"X-Mashape-Key": "OsaIJALh2lmshUqtlN7b4GQpJnU3p1C58RqjsnNGJW5f7pfNEQ",
                       "Accept": "text/plain"})
                       
    print response.code
    print response.body
    return response.body

@app.route("/weather")
def weather():
    env = Environment(loader=PackageLoader('WebDev', 'WebProject'))
    template = env.get_template('Weather.html')

    query = request.values.get("Location", None)
    response = unirest.get("https://george-vustrey-weather.p.mashape.com/api.php?location="+query,headers={"X-Mashape-Key": "OsaIJALh2lmshUqtlN7b4GQpJnU3p1C58RqjsnNGJW5f7pfNEQ",
                           "Accept": "application/json"})
                           
    #print response.body
    WeatherGeneral=[]
    
    for y in range (0,7):
        WeatherDic = {
            "day": response.body[y].get("day_of_week"),
            "conditions": response.body[y].get("condition"),
            "high": response.body[y].get("high"),
            "low": response.body[y].get("low")
        }
        WeatherGeneral.append(WeatherDic)
    
    #print WeatherDay
    #print WeatherCond
    #print response.body
    return template.render(WeatherGen = WeatherGeneral, Body=query) # Variables you can use in the html
    #return response.body[1].get("condition")


if __name__ == '__main__':
    app.run()