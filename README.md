# Lyricflow

## Contributors

* Chintip Winn
* Henry Jetmundsen
* Michael Jimenez
* Jonathan Gilbert 
## About Lyricflow

### What will the product do

Lyricflow is a third party app integrated with Google Assistant. Lyricflow allows users to talk to Google Assistant and have it parse their input using natural language queries powered by Google’s Dialogflow and return the song title and artist.

### Our approaches

We started with regular regex searching, which worked on small datasets (<5000 songs), but then became unfeasible with more realistic (read: larger) datasets.

Currently we are working on two approaches to solve the problem:

* **I: Machine Learning // Neural Network**
We gather huge datasets, and work with the data to train our machine learning model using the Tensorflow python ML library. After training for 10 Epochs with a vocabulary size of 15000 (9,000,000+ pieces of data to analyze), the model can accurately (>90%) predicts an artist to a song just from lyrics. Improvements are pending, and the model will gradually become smarter and efficient.

* **II: Sentiment Analysis**
Using Google's Natural Language API, we can retrieve sentiment data of input text. The sentiment data includes a score in range (-1,1) that indicates the overall emotion of the text, and a magnitude that indicates how much emotional content is present within the document. By filling our lyric dataset with these values for each song, we hope to find a correlation between the sentiment analysis of text to the entire song. This information will be usefull in shrinking the set of songs we need to search from. For example, if lyrics have a sentiment score of 0.4, we expect the song to lie in some range (0.4+x, 0.4-x), where x is the ideal threshold. Through analysis and training we can determine the best threshold where the song we are looking for falls into our subset.

### Why are you creating this particular product?

Many times I find myself hearing something on the radio or over the speakers in public and I really wanna find out what song is playing. However later when I go to try and find the song, I realize the only thing I have is a few main lyrics and the hook in my head but it’s not enough to track down the song. This app will fill that need and allow users to find songs that are on the tip of the tongue. 

### Who will benefit from this product?

Apple Music, Tidal, Soundcloud, Spotify Music, Pandora, Shazam and many other music corporations that would benefit from a natural language processing application that will allow the user to be able to look up lyrics and link that to an individual song. This will simplify the song look up process for the user and also solve the problem of being able to look up a song and play it, without knowing the song’s name. This application may have further uses in fields other than music loop up.

### How does the product compare against similar products already on the market?

The only somewhat similar product on the market is Shazam and that only works if the song is actively playing and you clear audio to play to the app. Our product only requires that the user know some of the lyrics so this eliminates the need for clean audio and having your phone on you at all times to open shazam when you hear a song you wanna know the name of.Our application gives the user a better chance of finding out a song that they do not know the name of, by providing a string of lyrics instead of finding the audio of the song. This gives the overall consumer a higher probability of finding music that they are not aware of. Our application also makes searching music handsfree a much more simplified and enjoyable experience.
