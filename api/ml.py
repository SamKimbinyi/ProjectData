import requests
import pandas as pd
from transformers import pipeline
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import json

def initialize_model():
    MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
    tokenizer2 = AutoTokenizer.from_pretrained(MODEL)
    config = AutoConfig.from_pretrained(MODEL)
    model1 = AutoModelForSequenceClassification.from_pretrained(MODEL)
    return model1, tokenizer2

def process_tweet(tweet):
    response = requests.get('http://127.0.0.1:8000/tweets/'+tweet)
    k = response.json()
    k_out = list(k.values())
    sentiment_task = pipeline("sentiment-analysis", model = model1, tokenizer = tokenizer2)
    k2 = sentiment_task(k_out)
    z = k | k2[0]
    json_object = json.dumps(z) 
    return json_object

model1, tokenizer2 = initialize_model()