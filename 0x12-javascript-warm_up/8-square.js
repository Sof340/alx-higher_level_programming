#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0])) {
  console.log('Missing size');
} else {
  let mes = '';
  for (let x = 0; x < args[0]; x++) {
    mes += 'X';
  }
  for (let x = 0; x < args[0]; x++) {
    console.log(mes);
  }
}
