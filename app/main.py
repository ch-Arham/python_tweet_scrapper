from flask import Flask
import snscrape.modules.twitter as sntwitter
import pandas as pd
from flask import request
from flask_cors import CORS, cross_origin


app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
@cross_origin()
def hello_world():

    if request.method == 'POST':
        print("POST")
        print(request.json)
    

    hashtag = request.json['hashtag']
    tweets = []
    limit = 1

    for tweet in sntwitter.TwitterSearchScraper(hashtag).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.user.username])
            
    df = pd.DataFrame(tweets, columns=['Date', 'User' ])
    print(df.to_json(orient='records'))

    return df.to_json(orient='records')
# from flask import Flask
# app= Flask(__name__)
# @app.route('/')
# def index():
#   return "<h1>Welcome to CodingX</h1>"