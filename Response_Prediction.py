from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import random
import string
import numpy as np

model = keras.models.load_model('Models/chatbox_model.h5')

data = pickle.load(open("Models/chatbox_model.pkl", "rb"))
encoder = data['encoder']
tokenizer = data['tokenizer']
responses = data['responses']
input_shape = data['input_shape']

def response(msg):
    texts_p = []
    prediction_input = msg

    #removing punctuation and converting to lowercase
    prediction_input = [letters.lower() for letters in prediction_input if letters not in string.punctuation]
    prediction_input = ''.join(prediction_input)
    texts_p.append(prediction_input)

    #tokenizing and padding
    prediction_input = tokenizer.texts_to_sequences(texts_p)
    prediction_input = np.array(prediction_input).reshape(-1)
    prediction_input = pad_sequences([prediction_input],input_shape)

    #getting output from model
    output = model.predict(prediction_input)
    output = output.argmax()

    #finding the right tag and predicting
    response_tag = encoder.inverse_transform([output])[0]
    final_output = random.choice(responses[response_tag])
    
    return response_tag, final_output
