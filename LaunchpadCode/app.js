const express = require('express');
const path = require('path');

const app = express();

app.use(express.json());
app.use(express.urlencoded());


const port = 3000;

var counter = 0;

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
});

app.get('/test', (req, res) => {
  res.sendFile(path.join(__dirname + '/public/test.html'));
});

app.get('/', (req, res) => {
  res.send("Hello World! :)");
});

app.get('/api/getVal', (req, res) => {
  let retVal = {count: counter};
  res.send(JSON.stringify(retVal));
});

app.post('/api/increment', (req, res) => {
  counter += parseInt(req.body.count);
  res.send(JSON.stringify({count: counter}));
});

app.use(express.static('public'));
