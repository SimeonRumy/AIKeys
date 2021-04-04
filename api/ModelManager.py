from api.Model import Model
from api.ModelFetcher import ModelFetcher
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
import numpy as np
import tensorflow as tf
import os
import random
import string

class ModelManager: 

    models = {
        "python" : Model(model="model", max_id="max_id", tokenizer="tokenizer"),
        "swift": Model(model="model", max_id="max_id", tokenizer="tokenizer"),
    }

    def __init__(self):
        print("intialising text generator")
        model_fetcher = ModelFetcher()
        for key in self.models.keys(): 
            tokenizer = model_fetcher.getTokenizer(key)
            model = model_fetcher.getModel(key)
            print("key")
            print(key)
            max_id = len(tokenizer.word_index)
            self.models[key] = Model(model=model, max_id=max_id, tokenizer=tokenizer)
