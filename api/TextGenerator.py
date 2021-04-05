
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
import numpy as np
import tensorflow as tf
import os
import random
import string
from api.Model import Model
from api.ModelManager import ModelManager

class TextGenerator:

    def __init__(self):
        print("init text generatot")
        self.model_manager = ModelManager()

    def generate_more_text(self, lang):
        print("get more text")
        self.current_model = self.model_manager.models[lang]
        return self.complete_text(n_chars=100)

    def preprocess(self, texts):
        X = np.array(self.current_model.tokenizer.texts_to_sequences(texts)) - 1
        return tf.one_hot(X, self.current_model.max_id)
    
    def next_char(self, text, temperature=1):
        X_new = self.preprocess([text])
        y_proba = self.current_model.model.predict(X_new)[0, -1:, :]
        rescaled_logits = tf.math.log(y_proba) / temperature
        char_id = tf.random.categorical(rescaled_logits, num_samples=1) + 1
        return self.current_model.tokenizer.sequences_to_texts(char_id.numpy())[0]

    def complete_text(self, n_chars=150, temperature=1):
        text = random.choice(string.ascii_letters)
        for i in range(n_chars):
            text = f'{text}{self.next_char(text, temperature)}'
        return text

    

