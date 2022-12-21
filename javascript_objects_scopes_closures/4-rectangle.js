#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
     if (parseInt(w) > 0) {
      this.width = w;
    }
    if (parseInt(h) > 0) {
      this.height = h;
    }
  }
}

Rectangle.prototype.print = function () {
  let i = 0;
  for (i; i < this.height; i++) {
    console.log('X'.repeat(this.width));
  }
};

Rectangle.prototype.double = function () {
  this.width *= 2;
  this.height *= 2;
};

Rectangle.prototype.rotate = function () {
  const temp = this.height;
  this.width = temp;
  this.height = this.width;
};

module.exports = Rectangle;
