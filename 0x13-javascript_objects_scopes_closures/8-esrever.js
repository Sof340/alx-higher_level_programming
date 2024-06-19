#!/usr/bin/node
exports.esrever = function (list) {
  const temp = [];
  for (let x = 0; x < list.length; x++) {
    temp[x] = list[list.length - x - 1];
  }
  return temp;
};
