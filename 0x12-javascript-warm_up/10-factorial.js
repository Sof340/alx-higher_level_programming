#!/usr/bin/node
const args = process.argv.slice(2);
function fact (a) {
  if (isNaN(a)) {
    return 1;
  } else if (a === 0) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}
console.log(fact(parseInt(args[0])));
