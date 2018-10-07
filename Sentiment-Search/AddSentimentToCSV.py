# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six
#Imports for pandas to read/write csv
import csv
import sys
import pandas as pd

def getCSV(csv):
	return pd.read_csv(csv)

def getSentiment(lyrics):
	# Instantiates a client
	client = language.LanguageServiceClient()

	# The text to analyze
	text = lyrics

	# Detects the sentiment of the text
	try:
		document = types.Document(
	    	content=text,
	    	type=enums.Document.Type.PLAIN_TEXT)
		sentiment = client.analyze_sentiment(document=document).document_sentiment
	except:
		print("Exception occured")
		document = types.Document(
	    	content="",
	    	type=enums.Document.Type.PLAIN_TEXT)
		sentiment = client.analyze_sentiment(document=document).document_sentiment

	#print('Text: {}'.format(text))
	#print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

	return sentiment

def addSentiment(df) :
	score = []
	mag = []
	i = 0
	for index, row in reader.iterrows() : 
		s = getSentiment(row["text"])
		score.append(s.score)
		mag.append(s.magnitude)
		print(index, row["song"], row["artist"])
	df['score'] = score
	df['magnitude'] = mag
	print(df)
	return df


reader = getCSV("billboard_edit.csv")
#songs = reader["text"]
#lyricSentiment = getSentiment("Look at her face, it's a wonderful face And it means something special to me")
#songSentiment = getSentiment(songs[0])
#add sentiment to csv test
info = addSentiment(reader)
info.to_csv("billboardSet.csv", encoding='utf-8', index=False)



# The score of a document's sentiment indicates the overall emotion of a document.

# The magnitude of a document's sentiment indicates how much emotional content is present within the document, 
# and this value is often proportional to the length of the document.

	# Interpreting score and magnitude
	# Clearly Positive*	"score": 0.8, "magnitude": 3.0
	# Clearly Negative*	"score": -0.6, "magnitude": 4.0
	# Neutral	"score": 0.1, "magnitude": 0.0
	# Mixed	"score": 0.0, "magnitude": 4.0