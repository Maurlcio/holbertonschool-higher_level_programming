#!/usr/bin/node

let SIZE = Math.floor(Number(process.argv[2]))

if (isNaN(SIZE) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < SIZE; i++) {
    let row = '';
    for (let j = 0; j < SIZE; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
