import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(#Bajwa) until:2022-05-31 since:2022-05-24"
tweets = []
limit = 2


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username])
        
df = pd.DataFrame(tweets, columns=['Date', 'User' ])
print(df)


# JSON
# print(df.to_json(orient='records'))

# to save to csv
# df.to_csv('tweets.csv')