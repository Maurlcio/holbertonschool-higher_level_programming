#!/usr/bin/node

const ARGV = process.argv.length;

if (ARGV === 2) {
  console.log('No argument');
} else if (ARGV === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
