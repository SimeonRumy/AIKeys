import pickle5 as pk
from keras.models import model_from_json
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
import numpy as np
import tensorflow as tf
import os
import random
import string

model_url_dict = {
    "python" : ["Python-0002-NC-statefull.h5", "Python-0002-NC.json", "tokenizer-python-NC.pickle"],
    "swift": ["LTSM-swift0001.h5", "LTSM-swift0001.json", "tokenizer-swift.pickle"],
}

class ModelFetcher:

    base_url = "api/ml_models/"

    def getURL(self, filename):
        return f"{self.base_url}{filename}"

    def getModel(self, lang):
        json_url = self.getURL(model_url_dict[lang][1])
        print(json_url)
        model_url = self.getURL(model_url_dict[lang][0])
        print(model_url)
        json_file = open(json_url, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights(model_url)
        print("Loaded model from disk")
        loaded_model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return loaded_model

    def getTokenizer(self, lang):
        tokenizer_url = self.getURL(model_url_dict[lang][2])
        # load tokenizer
        with open(tokenizer_url, 'rb') as handle:
            tokenizer = pk.load(handle)
            return tokenizer