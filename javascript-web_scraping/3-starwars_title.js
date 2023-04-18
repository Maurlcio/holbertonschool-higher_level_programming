#!/usr/bin/node

const request = require('request');

const URL = 'https://swapi-api.hbtn.io/api/films/:' + process.argv[2];
request(url, function (error, response, body) {
  console.error('error:', error);
  console.log(JSON.parse(body).title);
});
