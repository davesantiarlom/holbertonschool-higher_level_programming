#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], function (err, data) {
  if (err) throw err;

  fs.appendFile(process.argv[4], data, function (err) {
    if (err) throw err;
  });
});

fs.readFile(process.argv[3], function (err, data) {
  if (err) throw err;

  fs.appendFile(process.argv[4], data, function (err) {
    if (err) throw err;
  });
});
