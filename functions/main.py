import numpy as np
import pandas as pd
import re
import sys
import json

snippet = sys.stdin.readlines()
snippet = snippet[0]
snippet = snippet.split()

for index in range(len(snippet)):
  snippet[index] = "(" + snippet[index] + ")"

snippet = "(.*)".join(snippet)
maxScore = 0
song_name = ""
artist = ""

music = pd.read_csv("billboard.csv")

for index, song in music.iterrows():
  lyrics = song[4]

  if type(lyrics) is float:
    continue

  score = len(re.findall(snippet, lyrics.lower()))
  if score >= maxScore:
    maxScore = score
    song_name = song[1]
    artist = song[2]

print("{} by {}".format(song_name, artist))