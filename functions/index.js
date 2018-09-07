let options = require('./config/requestOptions');
const request = require('request');

const {dialogflow} = require('actions-on-google');

const functions = require('firebase-functions');

const app = dialogflow({debug: true});

app.intent('find song', (conv, lyrics) => {
	options.genius.qs = {q: lyrics};

  request(options.genius, (err, res, body) => {
  	let song = body.hits[0].result.title;
  	let artist = body.hits[0].result.primary_artist.name

  	conv.close("The song is ${song} by ${artist}");
  });
})

exports.dialogflowFirebaseFulfillment = functions.https.onRequest(app);