/**
 * generatort:
 * @param n: Number(optional, defaults to 5)
 * @yield  : n numbers
 * @return : undefined
 * @example: generatort(2) -> 130,38
 * @example: generatort() -> 0,29,82,1,39
 * 
 * Recursive generator function.
 * Generates n random numbers in the range (1 - 100)
 * If n is not provided, it genetates 5 random numbers.
 */
function* generatort(n=5) {
  if (n === 0) return
  yield Math.floor(Math.random(100)*100)
  yield* generatort(n-1)
}

for (const random of generatort()) {
  console.log(random)
}
