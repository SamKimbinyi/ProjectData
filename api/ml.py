import requests
import pandas as pd
from transformers import pipeline
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import json




def process_tweet(tweet,model,tokenizer):
    sentiment_task = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    k2 = sentiment_task(tweet)
    return k2

