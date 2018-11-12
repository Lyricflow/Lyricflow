import pandas as pd
import random
import numpy as np

df = pd.read_csv('new_billboard_edited.csv')

for i in range(0, 1000) :
	num = np.random.randint(0, 6500)
	df = df.drop(df.index[num])

for i in range(0, 1000) :
	num = np.random.randint(0, 5500)
	df = df.drop(df.index[num])

for i in range(0, 1000) :
	num = np.random.randint(0, 4500)
	df = df.drop(df.index[num])

for i in range(0, 1000) :
	num = np.random.randint(0, 3500)
	df = df.drop(df.index[num])

for i in range(0, 1000) :
	num = np.random.randint(0, 2500)
	df = df.drop(df.index[num])

for i in range(0, 500) :
	num = np.random.randint(0, 2000)
	df = df.drop(df.index[num])

df.to_csv('new_billboard_trimmed.csv')

# print(df)