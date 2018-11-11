# Sample python integration with HTTP program
import numpy as np
import pandas as pd
import re as regex
import string
import json
import sys

# sanitize the input string
def sanitize(snippet):
  remove_punctuation = str.maketrans('', '', string.punctuation)
  snippet = snippet.lower().translate(remove_punctuation).split()
  return snippet

# regex search courtesy of Henry
def find_song(snippet):
  pattern = "([a-z]+ ){0,2}"
  maxScore = 0
  song_name = ""
  artist = ""

  for index in range(len(snippet) - 1):
    snippet[index] = "{} {}".format(snippet[index], pattern)

  snippet = "".join(snippet)

  music = pd.read_csv("billboard.csv")

  for index, song in music.iterrows():
    lyrics = song[4]

    if type(lyrics) is float:
      continue

    score = len(regex.findall(snippet, lyrics.lower()))
    if score > maxScore:
      maxScore = score
      song_name = song[1]
      artist = song[2]

  print("{} by {}".format(song_name, artist))

dialogflow_json = json.loads(sys.argv[1])
lyrics = dialogflow_json['queryResult']['queryText']
snippet = sanitize(lyrics)
find_song(snippet)


