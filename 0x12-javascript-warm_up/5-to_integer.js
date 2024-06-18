#!/usr/bin/node
const args = process.argv.slice(2);
const result = parseInt(args[0]);
if (isNaN(result)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + result);
}
