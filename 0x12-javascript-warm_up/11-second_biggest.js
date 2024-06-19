#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(parseInt(args[0])) || args.length === 1) {
  console.log(0);
} else {
  let first = parseInt(args[0]);
  let second;
  for (let x = 1; x < args.length; x++) {
    if (first < parseInt(args[x])) {
      second = first;
      first = parseInt(args[x]);
    } else if (second < parseInt(args[x])) {
      second = parseInt(args[x]);
    }
  }
  if (isNaN(second)) {
    second = parseInt(args[1]);
    for (let x = 2; x < args.length; x++) {
      if (second < parseInt(args[x])) {
        second = parseInt(args[x]);
      }
    }
  }
  console.log(second);
}
