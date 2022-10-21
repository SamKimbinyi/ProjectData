import os

import tweepy
from prefect import flow, task
import json
from scrapers.twitter import search_tweet, parse_tweet_json


@flow(name="Twitter")
async def get_twitter(search_term):
    raw_tweets = twitter_api_search(search_term)
    cleaned_tweets = parse_tweets(raw_tweets)
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
