#!/usr/bin/node
exports.converter = function (base) {
  if (base < 2) {
    return;
  }

  return function convertToBaseN (number) {
    if (number < base) {
      if (number < 10) {
        return String(number);
      } else {
        return String.fromCharCode(87 + number);
      }
    } else {
      return convertToBaseN(number / base | 0) + convertToBaseN(number % base);
    }
  };
};
