/**
 * highestDigit:
 * @param num: Number
 * @return   : Number (single digit)
 * @example  : highestDigit(12899) -> 9
 * 
 * Receives a number as an argument.
 * Returns the highest digit in that number.
 */
function highestDigit(num) {
  // return Math.max(...num.toString()) -- shorter solution that I don't prefer 
  return Array.prototype.reduce.call(
    num.toString(),
    (max, digit) => {
      return digit > max ? digit : max
    }
  )
}

console.log(highestDigit(12899))
console.log(highestDigit(8123))
console.log(highestDigit(193))
console.log(highestDigit(1))
