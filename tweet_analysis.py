import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#get the Json
tweetFile = open("./tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

#


for tweet in tweetData:
    #print(tweet["text"])
    tweet_polarity = TextBlob(tweet["text"])
    print(tweet_polarity.sentiment)
    print(tweet_polarity.polarity)



    #tb = TextBlob(".polarity")
    #print(tb.polarity)
