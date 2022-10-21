import os

import tweepy
import requests
from prefect import flow, task
import json
from scrapers.twitter import search_tweet, parse_tweet_json


@flow(name="Twitter")
async def get_twitter(search_term):
    raw_tweets = twitter_api_search(search_term)
    cleaned_tweets = parse_tweets(raw_tweets)

    futures = add_sentiment.map(cleaned_tweets)

    for index, tweet in enumerate(cleaned_tweets):
        print(f"Index: {index}/ Total:{len(cleaned_tweets)}")
        print(tweet["tweet"])
        tweet["sentiment"] = add_sentiment(tweet["tweet"])

    return cleaned_tweets



@task(name="Search Tweet")
def twitter_api_search(search_term):
    bearer_token = os.environ["BEARER_TOKEN"]
    auth = tweepy.OAuth2BearerHandler(bearer_token)

    api = tweepy.API(auth)

    tweets = search_tweet(search_term, api)
    return tweets

@task(name="Parse Tweets")
def parse_tweets(tweets):
   return [parse_tweet_json(x._json) for x in tweets]


@task(name="Add Sentiment")
def add_sentiment(text):
    API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
    headers = {"Authorization": f"Bearer {os.environ['HUG_TOKEN']}"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": text,
    })
    return output

