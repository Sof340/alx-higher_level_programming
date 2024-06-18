#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0])) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < args[0]; x++) {
    console.log('C is fun');
  }
}
