import pandas as pd
import textwrap

def splice(st) :
	st = st.lower()
	spliced = textwrap.wrap(st, 50)

	return spliced

df = pd.read_csv('data/new_billboard_trimmed.csv')

df = df.drop(['Unnamed: 0'], axis=1)

df = df.fillna('asdf')


to_add = []

for i in range(0, 2000) :
	artist = df.loc[i]['artist']
	song = df.loc[i]['title']
	full_lyrics = df.loc[i]['lyrics']

	spliced_list = splice(full_lyrics)

	for x in spliced_list :
		row = []

		row.append(song + ' by ' + artist)
		row.append(song + ' by ' + artist)
		row.append(x)

		to_add.append(row)


columns = ['title', 'artist', 'lyrics']
output = pd.DataFrame(to_add, columns=columns)

output.to_csv('new_spliced_billboard.csv')

print()