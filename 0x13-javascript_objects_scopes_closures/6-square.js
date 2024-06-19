#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c) {
    const caracter = c || 'X';
    let mes = '';

    for (let x = 0; x < this.height; x++) {
      mes += caracter;
    }
    for (let x = 0; x < this.width; x++) {
      console.log(mes);
    }
  }
}

module.exports = Square;
