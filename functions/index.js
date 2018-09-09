'use strict';

let options = require('./config/requestOptions');
const request = require('request');

const {dialogflow} = require('actions-on-google');

const functions = require('firebase-functions');

const app = dialogflow({debug: true});

const fetch = require('node-fetch');
global.Headers = fetch.Headers;

var myHeaders = new Headers({
	'Authorization' : 'Bearer U88QBBKT4Q3r46h6EnIgrXyvDt8J_LnYBQvpayFS9js9a1yo9W1NhWh2oHeFDGZS'
});

// fetch('https://api.genius.com/search?q='+"Eminem", {headers: myHeaders}).then(function(response) {
// 	response.json().then(function(results) {
// 		console.log(results.response.hits[0].result.title);
// 	})
// })



app.intent('Default Welcome Intent', (conv) => {
	conv.ask('Gimme lyrics');
});

app.intent('ask for song', (conv, {lyrics}) => {
	// var songName;
	// fetch('https://api.genius.com/search?q='+lyrics, {headers: myHeaders}).then(function(response) {
	// 	response.json().then(function(results) {
	// 		console.log(results.response.hits[0].result.title);
	// 		songName = results.response.hits[0].result.title;
	// 	});
	// }).then(conv.close('Song is: ' + songName));

	conv.close(lyrics);
	// conv.close('Song is: ' + songName);
	// .then(function(callback) {
	// 	conv.close('Song is'+songName);
	// });
});



// app.intent('Default Welcome Intent', (conv) => {
// 	conv.ask('Tell me some lyrics');
// });

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


exports.dialogflowFirebaseFulfillment = functions.https.onRequest(app);


