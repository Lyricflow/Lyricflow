'use strict';

let options = require('./config/requestOptions');
const request = require('request');

const {dialogflow} = require('actions-on-google');

const functions = require('firebase-functions');

const app = dialogflow({debug: true});

exports.dialogflowFirebaseFulfillment = functions.https.onRequest(app);

app.intent('Default Welcome Intent', (conv) => {
	conv.ask('Tell me some lyrics');
});

app.intent('Default Fallback Intent', (conv) => {
	options.genius.qs = {q: conv.input.raw}

	const getSong = () => new Promise((resolve) => {
		request(options.genius, (err, res, body) => {
			resolve(body);
		})
	});

	return getSong().then((body) => {
		let song = body.response.hits[0].result.title;
		let artist = body.response.hits[0].result.primary_artist.name;

		conv.close("The song is " + song + " by " + artist);
	});
});