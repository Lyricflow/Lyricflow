const express = require('express');
const fs = require('fs-extra');
const app = express();
const port = 3000;

// app.get('/', (req, res) => res.send('Hello World!'));

let df_json = fs.readFileSync('df-request.json');

app.get('/', (req, res) => {
    const spawn = require("child_process").spawn;
    const pythonProcess = spawn('python3',["./regex_search.py", df_json]);
    result = "";

    pythonProcess.stdout.on('data', (data) => {
        result += data.toString();
    });

    pythonProcess.stdout.on('end', () => {
        console.log(result);
        res.send(result);
    })
})

app.listen(port, () => console.log(`App listening on port ${port}!`));