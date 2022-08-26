/********************** Helper Functions *********************/
/**
 * arrayFromRange:
 * @param lowEnd : Number
 * @param highEnd: Number
 * @return       : Array of Numbers
 * @example      : arrayFromRange(34, 39) -> [34, 35, 36, 37, 38, 39]

 * Returns an array of numbers from a range.
 * The range is represented by the two arguments.
 */
function arrayFromRange(lowEnd, highEnd) {
  return Array.from(
    {
      length: (highEnd - lowEnd) + 1
    },
    (_, i) => lowEnd + i
  )
}
/*************************************************************/

/**
 * rangeEvens:
 * @param lowEnd : Number
 * @param highEnd: Number
 * @return       : Array (of numbers)
 * @example      : rangeEvens(10,20) -> 10,12,14,16,18
 * 
 * Assumes that lowEnd is a positive integer greater than 0.
 * Checks that highEnd is positive integer greater that lowEnd.
 * Returns all even numbers within the range of lowEnd and highEnd.
 */
function rangeEvens(lowEnd, highEnd) {
  if (lowEnd > highEnd) return []
  return arrayFromRange(lowEnd, highEnd)
    .filter(num => num % 2 == 0)
}

console.log(rangeEvens(10, 20))
console.log(rangeEvens(57, 80))