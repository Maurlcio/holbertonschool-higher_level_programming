#!/usr/bin/node

const FIRST_ARG = process.argv[2];

if (FIRST_ARG === undefined) {
  console.log('No argument');
} else {
  console.log(FIRST_ARG);
}
