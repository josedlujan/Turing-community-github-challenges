// Turing Community GitHub Challenge 2
// Eduardo Aire Torres @eduairet
'use-strict';

// Generate random numbers Challenge 1
const generator = (len = 5) =>
  Array.from({ length: len > 0 ? len : 0 }, () =>
    Math.round(Math.random() * 100)
  );
// Test data
console.log(generator(2)); // len = 2
console.log(generator()); // len = 5
console.log(generator(10)); // len = 10
console.log(generator(-1)); // len = 0

// Even numbers within a sequence Challenge 2
const range_pairs = (x, y) =>
  x > 0 && y > x
    ? Array.from(
        { length: Math.trunc((y - x) / 2) },
        (_, i) => (x % 2 == 0 ? x : x + 1) + i * 2
      )
    : 'x is a positive number greater than 0\ny is a positive number greater than x';
// Test Data
console.log(range_pairs(1, 2)); // []
console.log(range_pairs(10, 20)); // [ 10, 12, 14, 16, 18 ]
console.log(range_pairs(57, 80)); // [ 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78 ]
// Fails
console.log(range_pairs(20, 15));
console.log(range_pairs(-5, 15));
/*
x is a positive number greater than 0
y is a positive number greater than x
*/
