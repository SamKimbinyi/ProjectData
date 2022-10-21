import tweepy
import os

bearer_token = os.environ["BEARER_TOKEN"]
# print(bearer_token)
auth = tweepy.OAuth2BearerHandler(bearer_token)

api = tweepy.API(auth)

user = api.get_user(screen_name='twitter')
result = api.search_tweets("Apple")
print(result[0])
