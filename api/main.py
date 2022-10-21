from typing import Union

from fastapi import FastAPI

from orchestration.core import get_twitter

app = FastAPI()


@app.get("/search/twitter/{search_term}")
async def search_tweets(search_term: str):
    s = await get_twitter(search_term)
    return s
