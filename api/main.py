import asyncio
from typing import Union

from fastapi import FastAPI
from transformers import AutoModelForSequenceClassification, AutoConfig, AutoTokenizer
import requests
from api.ml import process_tweet
from model import Tweet
import os
from orchestration.core import get_twitter

app = FastAPI()





@app.get("/search/twitter/{search_term}")
async def search_tweets(search_term: str):
    s = await get_twitter(search_term)
    return s
