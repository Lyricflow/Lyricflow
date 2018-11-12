const express = require('express');
const fs = require('fs-extra');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
    const lyrics = req.query.q;
    const spawn = require("child_process").spawn;
    const pythonProcess = spawn('python3',["./regex_search.py", lyrics]);
    result = "";

    pythonProcess.stdout.on('data', (data) => {
        result += data.toString();
    });

    pythonProcess.stdout.on('end', () => {
        res.send(result);
    })
})

app.listen(port, () => console.log(`App listening on port ${port}!`));