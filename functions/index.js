'use strict';

let options = require('./config/requestOptions');

const rp = require('request-promise');
const {dialogflow} = require('actions-on-google')
const functions = require('firebase-functions');
const app = dialogflow({debug: true});

app.intent('Default Welcome Intent', (conv) => {
    conv.ask('Tell me some lyrics');
});

app.intent('Default Fallback Intent', (conv) => {
    options.genius.qs = {q: conv.input.raw}

    return rp(options.genius).then((body) => {
        let song = body.response.hits[0].result.title;
        let artist = body.response.hits[0].result.primary_artist.name;

        conv.close("The song is " + song + " by " + artist);
        return Promise.resolve();
    });
});

exports.dialogflowFirebaseFulfillment = functions.https.onRequest(app);