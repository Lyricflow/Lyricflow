import pandas as pd
import numpy as np
import pickle
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout
from sklearn.preprocessing import LabelBinarizer
from keras.models import load_model

model = load_model('my_model.h5')

data = pd.read_csv('data/billboard.csv')

data = data.drop(['Rank', 'Year', 'Source'], axis=1)

data = data.replace(np.nan, 'asdfg', regex=True)

train_size = int(len(data))

test_lyrics = data['Lyrics'][:train_size]
test_artists = data['Artist'][:train_size]
test_song_names = data['Song'][:train_size]

tokenizer = Tokenizer(num_words=15000)
tokenizer.fit_on_texts(test_lyrics)

df_modified = data.groupby(['Artist'], sort=False).size().reset_index(name='Count')
df_list = df_modified['Artist'].tolist()

labels = np.array(df_list)

song1 = 'may i have your attention please may i have your attention please will the real slim shady please stand up i repeat will the real slim shady please stand up were going to have a problem hereyall act like you never seen a white person before jaws all on the floor like pam and tommy just burst in the door started whoopin her ass worse than before they first get divorced throwing her over furniture its the return of the oh wait no way your kidding he didnt just say what i think he did did he and dr dre said nothing you idiots dr dres dead hes locked in my basement ha ha feminist women love eminem chicka chicka chicka slim shady im sick of him look at him walking around grabbing his you know what flippin the you know who yeah but hes so cute though yea i probably got a couple of screws up in my head loose but no worse than whats going on in your parents bedrooms sometimes i want to get on tv and just let loose but cant but its cool for tom green to hump a dead moose my bum is on your lips my bum is on your lips and if im lucky you might just give it a little kiss and thats the message that we deliver to little kids and expect them not to know what a womens clitoris is of course they gonna know what intercourse is by the time they hit 4th grade they got the discovery channel dont they we aint nothing but mammals well some of us cannibals who cut other people open like cantaloupes but if we can hump dead animals and antelopes then theres no reason that a man and another man cant elope but if you feel like i feel i got the antidote women wave your pantyhose sing the chorus and it goesim slim shady yes im the real shady all you other slim shadys are just imitating so wont the real slim shady please stand up please stand up please stand up cause im slim shady yes im the real shady all you other slim shadys are just imitating so wont the real slim shady please stand up please stand up please stand upwill smith dont gotta cuss in his raps to sell records well i do so fuck him and fuck you too you think i give a damn about a grammy half of you critics cant even stomach me let alone stand me but slim what if you win wouldnt it be weird why so you guys can just lie to get me here so you can sit me here next to britney spears shit christina aguilera better switch me chairs so i can sit next to carson daly and fred durst and hear em argue over who she gave head to first little bitch put me on blast on mtv yeah hes cute but i think hes married to kim he he i should download her audio on mp3 and show the whole world how you gave eminem vd im sick of you little girl and boy groups all you do is annoy me so ive been sent here to destroy you and theres a million of us just like me who cuss like me who just dont give a fuck like me who dress like me walk talk and act like me it just might be the next best thing but not quite mecause im slim shady yes im the real shady all you other slim shadys are just imitating so wont the real slim shady please stand up please stand up please stand up cause im slim shady yes im the real shady all you other slim shadys are just imitating so wont the real slim shady please stand up please stand up please stand upim like a head trip to listen to cause im only giving you things you joke about with your friends inside your living room the only difference is i got the balls to say it in front of yall and i dont gotta be false or sugar coat it at all i just get on the mic and spit it and whether you like to admit it rip i just shit it better than 90 percent of you rappers out there then you wonder how can kids eat up these albums like valiums its funny cause at the rate im going when im thirty ill be the only person in the nursing home flirting pinching nurses asses when im jackin off with jergens and im jerking but this whole bag of viagra isnt working and every single person is a slim shady lurkin he could be workin at burger king spitten on your onion rings or in the parking lot circling screaming i dont give a fuck with his windows down and system up so will the real shady please stand up and put one of those fingers on each hand up and to be proud to be outta your mind and outta control and one more time loud as you can how does it goim slim shady yes im the real shady all you other slim shadys are just imitating so wont the real slim shady please stand up please stand up please stand up cause im slim shady yes im the real shady all you other slim shadys are just imitating so wont the real slim shady please stand up please stand up please stand upcause im slim shady yes im the real shady all you other slim shadys are just imitating so wont the real slim shady please stand up please stand up please stand up cause im slim shady yes im the real shady all you other slim shadys are just imitating so wont the real slim shady please stand up please stand up please stand uphaha i guess theres a slim shady in all of us fuck it lets all stand up'
song2 = 'i was so high i did not recognize the fire burning in her eyes the chaos that controlled my mind whispered goodbye as she got on a plane never to return again but always in my heart ohthis love has taken its toll on me she said goodbye too many times before and her heart is breaking in front of me and i have no choice cause i wont say goodbye anymorewhoa oh oh whoa oh oh whoa oh ohi tried my best to feed her appetite keep her coming every night so hard to keep her satisfied oh kept playing love like it was just a game pretending to feel the same then turn around and leave againbut oh ohh this love has taken its toll on me she said goodbye too many times before and her heart is breaking in front of me and i have no choice cause i wont say goodbye anymorewhoa oh oh whoa oh oh whoa oh ohbridge ill fix these broken things repair your broken wings and make sure everythings alright its alright its alright my pressure on your hips sinking my fingertips into every inch of you because i know thats what you want me to dothis love has taken its toll on me she said goodbye too many times before her heart is breaking in front of me and i have no choice cause i wont say goodbye anymorethis love has taken its toll on me she said goodbye too many times before and my heart is breaking in front of me and she said goodbye too many times beforethis love has taken its toll on me she said goodbye too many times before her heart is breaking in front of me and i have no choice cause i wont say goodbye anymore '
song3 = 'help i need somebody help not just anybody help you know i need someone help when i was younger so much younger than today i never needed anybodys help in any way but now these days are gone im not so selfassured now i find ive changed my mind and opened up the doors help me if you can im feeling down and i do appreciate you being round help me get my feet back on the ground wont you please please help me and now my life has changed in oh so many ways my independence seems to vanish in the haze but every now and then i feel so insecure i know that i just need you like ive never done before help me if you can im feeling down and i do appreciate you being round help me get my feet back on the ground wont you please please help me when i was younger so much younger than today i never needed anybodys help in any way but now these days are gone im not so selfassured now i find ive changed my mind ive opened up the doors help me if you can im feeling down and i do appreciate you being round help me get my feet back on the ground wont you please please help me help me help me ooo'

# song4 = 'in california with my toes in the sand'

# song1 = 'help'
# song2 = 'sam the sham'
# song3 = 'when i woke up'

x_data = []
x_data.append(song1)
x_data.append(song2)
x_data.append(song3)

x_data_series = pd.Series(x_data)

print(x_data_series)

x_tokenized = tokenizer.texts_to_matrix(x_data_series, mode='tfidf')

x_test = tokenizer.texts_to_matrix(test_lyrics, mode='tfidf')

encoder = LabelBinarizer()
encoder.fit(test_artists)

y_test = encoder.transform(test_artists)

text_labels = encoder.classes_

i=0
for x_t in x_tokenized:
    prediction = model.predict(np.array([x_t]))
    # print(prediction)
    predicted_label = text_labels[np.argmax(prediction[0])]
    print("Predicted label: " + predicted_label)
    i += 1