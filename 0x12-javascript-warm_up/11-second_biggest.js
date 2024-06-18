#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0]) || args.length === 1) {
  console.log(0);
} else {
  let first = args[0];
  let second;
  for (let x = 1; x < args.length; x++) {
    if (first < args[x]) {
      second = first;
      first = args[x];
    }
  }
  if (isNaN(second)) {
    second = args[1];
    for (let x = 2; x < args.length; x++) {
      if (second < args[x]) {
        second = args[x];
      }
    }
  }
  console.log(second);
}
