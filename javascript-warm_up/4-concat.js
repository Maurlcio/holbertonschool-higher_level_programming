#!/usr/bin/node

const TWO_ARGS = [process.argv[2], process.argv[3]];

if (TWO_ARGS[0] === undefined) {
  console.log('No arguments found');
} else if (TWO_ARGS[1] === undefined) {
  console.log('You need 2 arguments for this bozo');
} else {
  console.log(TWO_ARGS[0] + ' is ' + TWO_ARGS[1]);
}
