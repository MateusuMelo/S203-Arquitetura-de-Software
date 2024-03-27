const express = require('express'),
  path = require('path'),
  bodyParser = require('body-parser'),
  cors = require('cors'),
  sqlite3 = require('sqlite3').verbose();

let port = process.env.PORT || 3000;
const app = express();
app.use(cors())

const quotesRouter = require('./routes/datafilm_route');

app.get('/', (req, res) => {
  res.json({message: 'alive'});
});

app.use('/films', quotesRouter);

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
