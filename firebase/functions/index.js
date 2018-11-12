'use strict';

let options = require('./config/requestOptions');

// const rp = require('request-promise');
const request = require('request');
const {dialogflow} = require('actions-on-google')
const functions = require('firebase-functions');
const app = dialogflow({debug: true});

exports.dialogflowFirebaseFulfillment = functions.https.onRequest(app);

app.intent('Default Welcome Intent', (conv) => {
  conv.ask('Give me the lyrics.');
});

app.intent('Default Fallback Intent', (conv) => {
  conv.close('Idek what you\'re asking me to do dude');
});

app.intent('ask for song', (conv, {lyrics}) => {
  options.localAPI.qs.q = lyrics;

  const getSong = () => new Promise((resolve, reject) => {
    request(options.localAPI, (err, res, body) => {
      if(err){
        reject(err);
      } else {
        resolve(body);
      }
    });
  });

  return getSong().then((body) => {
    let result = conv.close(body);
    return result;
  });
});