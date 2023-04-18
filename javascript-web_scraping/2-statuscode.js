#!/usr/bin/node

const request = require('request');

request.get(process.argv[2]).on('status', function (status) {
  console.log(`code: ${status.statusCode}`);
});
