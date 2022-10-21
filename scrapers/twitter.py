import tweepy
import os
import re

bearer_token = os.environ["BEARER_TOKEN"]
auth = tweepy.OAuth2BearerHandler(bearer_token)

api = tweepy.API(auth)


def search_tweet(search_term, api):
    result = api.search_tweets(search_term,locale='en',count=1000)
    return result


def parse_tweet_json(tweet_json):
    return {
        "tweet": clean_tweet(tweet_json["text"]),
        "tweet_id": tweet_json["id"],
        "tweeter": tweet_json["user"]["name"],
        "retweet_count": tweet_json["retweet_count"],
        "location": tweet_json["user"]["location"]
    }


def clean_tweet(text):
    text = text.lower()
    text = re.sub(r'@[A-Za-z0-9_]+', '', text)
    text = re.sub(r'#[A-Za-z0-9_]+', '', text)
    text = re.sub(r"http\S+", '', text)
    text = re.sub(r"www.\S+", '', text)
    text = re.sub(r'[()!?]', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'[^a-z0-9]', ' ', text)
    text = text.strip()
    return text


output = []
