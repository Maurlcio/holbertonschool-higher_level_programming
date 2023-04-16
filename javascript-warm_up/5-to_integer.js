#!/usr/bin/node

const NUM = Math.floor(Number(process.argv[2]));

if (isNaN(NUM) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + NUM);
}
