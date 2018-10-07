'use strict';

let options = require('./config/requestOptions');
let spawn = require('child_process').spawn;

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
  const getSong = () => new Promise((resolve, reject) => {
    let py = spawn('python', ['main.py']);
    
    py.stdout.on('data', (data) => {
      resolve(data.toString());
    });

    py.stdin.write(lyrics);
    py.stdin.end();
  });

  return getSong().then((body) => {
    let result = conv.close(body);
    return result;
  })
});