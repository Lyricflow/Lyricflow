# Jonathan Gilbert
# sentimentSearch.py

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
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
	document = types.Document(
	    content=text,
	    type=enums.Document.Type.PLAIN_TEXT)

	# Detects the sentiment of the text
	sentiment = client.analyze_sentiment(document=document).document_sentiment

	#print('Text: {}'.format(text))
	#print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

	return sentiment

def checkLyrics(text, lyrics):
	if lyrics in text:
		return True
	else:
		return False

def getThreshold(score, threshold):
	return score + threshold, score - threshold

def searchNoThreshold():
	for index, row in reader.iterrows():
		if checkLyrics(row["text"], lyrics):
			print("Song found out of threshold")
			print(row["song"], row["score"])
			return row["song"], row["artist"]
	print("Song not found")
	return [], []

def search(threshold):
	print("Threshold: ", threshold)
	for index, row in reader.iterrows():
		if (row["score"] <= threshold[0] and row["score"] >= threshold[1]): 
			if checkLyrics(row["text"], lyrics):
				print(row["song"], row["score"])
				return row["song"], row["artist"]
	print("Song not found in threshold range")
	return searchNoThreshold()

lyrics = sys.argv[1]
print("Lyrics: ", sys.argv[1])
lyricSentiment = getSentiment(lyrics)
print('Lyric Sentiment: {}, {}'.format(lyricSentiment.score, lyricSentiment.magnitude))
reader = getCSV("songdataS.csv")

song, artist = search(getThreshold(lyricSentiment.score, 0.4))
if (song != []):
	print("".join(str(x) for x in song), "by", "".join(str(x) for x in artist))

