import os

import tweepy
from prefect import flow, task
import json
from scrapers.twitter import search_tweet, parse_tweet_json


@flow(name="Twitter")
async def get_twitter(search_term):
    return [parse_tweet_json(x._json) for x in twitter_api_search(search_term)]


@task(name="Search Tweet")
def twitter_api_search(search_term):
    bearer_token = os.environ["BEARER_TOKEN"]
    auth = tweepy.OAuth2BearerHandler(bearer_token)

    api = tweepy.API(auth)

    tweets = search_tweet(search_term, api)
    print(tweets)
    return tweets
