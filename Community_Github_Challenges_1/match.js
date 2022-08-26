/**
 * match:
 * @param str1: String
 * @param str2: String
 * @return    : Boolean
 * @example   : match("Jose", "JoSe") -> true
 * 
 * Validates whether the two strings are identical.
 */
function match(str1, str2) {
    return str1.toLowerCase() === str2.toLowerCase()
}

console.log(match("Jose", "JoSe"))
console.log(match("water", "wait"))
console.log(match("JOHN", "JOHn"))
console.log(match("ElEmEnTs", "eLeMeNtS"))