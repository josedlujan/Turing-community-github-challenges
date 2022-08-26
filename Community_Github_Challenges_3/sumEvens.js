/**
 * SumEvens:
 * @param   {Array} numArray
 * @return  {Number}
 * @example sumEvens([2,1,3,5,6,10]) = 18
 * 
 * Returns the sum of all positive even numbers in the list.
 */
function sumEvens(numArray) {
  return numArray.reduce((sum, num) => {
    return num % 2 === 0 && num > 0 ? sum + num : sum
  }, 0)
}

console.log(sumEvens([2,1,3,5,6,10]))
console.log(sumEvens([1,2,3,4,5,6,7,8,9,10,12]))
console.log(sumEvens([2,2,2,5,4,2]))