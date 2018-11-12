import pandas as pd
import numpy as np
import pickle
import sys
import os

# Hide useless keras information 
stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')
from keras.models import load_model
sys.stderr = stderr
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from sklearn.preprocessing import LabelBinarizer


model = load_model('model.h5')

data = pd.read_csv('../neural-network/data/new_spliced_billboard.csv')

test_size = int(len(data))

test_artists = data['artist'][:test_size]

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


song1 = sys.argv[1]

x_data = []
x_data.append(song1)

x_data_series = pd.Series(x_data)

x_tokenized = tokenizer.texts_to_matrix(x_data_series, mode='tfidf')

encoder = LabelBinarizer()
encoder.fit(test_artists)

text_labels = encoder.classes_

for x_t in x_tokenized:
	prediction = model.predict(np.array([x_t]))

	predicted_label = text_labels[np.argmax(prediction[0])]
	print(predicted_label)


