# Author : Genuino, Jose Mari Victorio G. 
# Date Created : 28 February 2023
# Purpose : ALTDSI - JRIG

import snscrape.modules.twitter as sntwitter 
import pandas as pd 

query = " " # insert query / search from Twitter web app 
tweets = []
limit = 4999

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    # print (vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])

df = pd.DataFrame(tweets, columns = ['Date', 'User', 'Tweet'])
print(df)

# to save to csv
df.to_csv(' --- .csv') # insert name of csv file here
