import tweepy
from textblob import TextBlob
auth = tweepy.OAuthHandler("credential 1", "credentials 2")
auth.set_access_token("credentials 3", "credentials 4")
api = tweepy.API(auth)
query=raw_input("enter any word or name ")
public_tweets = api.search(query)
for tweet in public_tweets:
    print tweet.text
    analysis=TextBlob(tweet.text)
    print analysis.sentiment
