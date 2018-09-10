'use strict';

let options = require('./config/requestOptions');

const rp = require('request-promise');
const request = require('request');
const {dialogflow} = require('actions-on-google')
const functions = require('firebase-functions');
const app = dialogflow({debug: true});

exports.dialogflowFirebaseFulfillment = functions.https.onRequest(app);

app.intent('Default Welcome Intent', (conv) => {
    conv.ask('Give me the lyrics.');
});

app.intent('Default Fallback Intent', (conv) => {
    conv.close('I\'m not having it');
})

app.intent('ask for song', (conv, {lyrics}) => {
    options.genius.qs = {q: lyrics}

    return new Promise((resolve, reject) => {
        request(options.genius, (err, res, body) => {
            if(err){
                reject(err);
            } else {
                let song = body.response.hits[0].result.title;
                let artist = body.response.hits[0].result.primary_artist.name;
                let result = conv.close("The song is " + song + " by " + artist);
                resolve(result);
            }
        })
    })
});