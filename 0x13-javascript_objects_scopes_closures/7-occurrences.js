#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  for (let x = 0; x < list.length; x++) {
    if (list[x] === searchElement) {
      occ++;
    }
  }
  return occ;
};
