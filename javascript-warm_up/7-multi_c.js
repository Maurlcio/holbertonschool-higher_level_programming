#!/usr/bin/node

let C_TIMES = Math.floor(Number(process.argv[2]));

if (isNaN(C_TIMES) === true) {
  console.log('Missing number of occurrences');
} else {
  for (; C_TIMES > 0; C_TIMES--) {
    console.log('C is fun');
  }
}
