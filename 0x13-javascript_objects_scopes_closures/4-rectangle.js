#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!(h <= 0 || w <= 0 || !w || !h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let mes = '';
    for (let x = 0; x < this.width; x++) {
      mes += 'X';
    }

    for (let x = 0; x < this.height; x++) {
      console.log(mes);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
