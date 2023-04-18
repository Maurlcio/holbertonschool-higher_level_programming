#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const URL = request(process.argv[2]);

fs.createWriteStream(process.argv[3], URL);
