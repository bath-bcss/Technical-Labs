const express = require('express');
const path = require('path');

const app = express();

app.use(express.json());
app.use(express.urlencoded());


const port = 3000;

var counter = 0;
let user = {};

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
});

app.get('/example1', (req, res) => {
  res.sendFile(path.join(__dirname + '/public/example1.html'));
});

app.get('/example2', (req, res) => {
  res.sendFile(path.join(__dirname + '/public/example2.html'));
});


app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname + '/public/index.html'));
});

app.get('/api/getVal', (req, res) => {
  let retVal = {count: counter};
  res.send(JSON.stringify(retVal));
});

app.post('/api/increment', (req, res) => {
  counter += parseInt(req.body.count);
  res.send(JSON.stringify({count: counter}));
});

app.post('/api/userdata', function(req, res){
  user = {first: req.body.first, second: req.body.second, business: req.body.business}
  res.send(JSON.stringify(user))
});

app.get('/api/userdata', function(req, res){
  res.send(JSON.stringify(user))
});

app.use(express.static('public'));//This makes the public folder accessible to anyone
