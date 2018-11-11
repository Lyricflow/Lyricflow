import pandas as pd
import numpy as np
import pickle
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout
from keras.models import load_model
from sklearn.preprocessing import LabelBinarizer
import matplotlib.pyplot as plt
import itertools
from sklearn.metrics import confusion_matrix
from pathlib import Path

# for reproducibility
np.random.seed(42069)

# Data preparation

training_csv_df = pd.read_csv('data/new_spliced_billboard.csv')

data = training_csv_df 

# some important numbers
num_labels = 1991
vocab_size = 15000
batch_size = 100
num_epochs = 30

train_size = int(len(data))


train_lyrics = data['lyrics'][:train_size]
train_artists = data['artist'][:train_size]
train_song_names = data['title'][:train_size]

test_lyrics = data['lyrics'][:train_size]
test_artists = data['artist'][:train_size]
test_song_names = data['title'][:train_size]

# tokenizes the lyrics

tokenizer = Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(train_lyrics)

x_train = tokenizer.texts_to_matrix(train_lyrics, mode='tfidf')
x_test = tokenizer.texts_to_matrix(test_lyrics, mode='tfidf')

encoder = LabelBinarizer()
encoder.fit(train_artists)

y_train = encoder.transform(train_artists)
y_test = encoder.transform(test_artists)

# functions

def train():

	# intiates the model and adds layers
	model = Sequential()
	model.add(Dense(512, input_shape=(vocab_size,)))
	model.add(Activation('relu'))
	model.add(Dropout(0.3))
	model.add(Dense(512))
	model.add(Activation('relu'))
	model.add(Dropout(0.3))
	model.add(Dense(num_labels))
	model.add(Activation('softmax'))
	model.summary()

	model.compile(loss='categorical_crossentropy',
	              optimizer='adam',
	              metrics=['accuracy'])

	history = model.fit(x_train, y_train,
	                    batch_size=batch_size,
	                    epochs=num_epochs,
	                    verbose=1,
	                    validation_split=0.1)

	# saves the model
	model.model.save('model.h5')

	# saves the tokenizer
	with open('tokenizer.pickle', 'wb') as handle:
	    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

	return model

def test(model, *args, **kwargs):

	randomize = kwargs.get('randomize', None)

	if randomize == True:
		idx_start = np.random.randint(1, 2000)
	else:
		idx_start = 1500

	text_labels = encoder.classes_

	correct_count = 0

	print('index_start: {}'.format(idx_start))
	for i in range(idx_start, idx_start+100):
	    to_predict = x_test[i]
	    # print(to_predict)
	    prediction = model.predict(np.array([x_test[i]]))
	    predicted_label = text_labels[np.argmax(prediction[0])]

	    if predicted_label == test_artists.iloc[i]:
	   		correct_count += 1

	    print('Actual label:' + test_artists.iloc[i])
	    print('Predicted label: ' + predicted_label)

	print('Score: {}/100'.format(correct_count))

# def score(model):
# 	score = model.evaluate(x_test, y_test,
# 	                       batch_size=batch_size, verbose=1)

# 	print('Test accuracy:', score[1])
# 	return score[1]


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()

my_model = train()

test(my_model, randomize=True)

print(y_pred)

# Compute + plot confusion matrix
cnf_matrix = confusion_matrix(np.argmax(y_test_sliced, axis=1), np.argmax(y_pred, axis=1))

print(cnf_matrix)

np.set_printoptions(precision=2)

class_names = ['1,', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names,
                      title='Confusion matrix, without normalization')

# Plot normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names, normalize=True,
                      title='Normalized confusion matrix')

plt.show()