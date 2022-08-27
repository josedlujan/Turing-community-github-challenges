/**
 * Map.prototype.filter:
 * @param   {Function} predicate 
 * @returns {Map}
 * @example new Map([['a', 1], ['b', 2]]).filter((key, value) => value === 1) -> Map { 'a' => 1 }
 * 
 * Applies the predicate function to each entry of the map.
 * Returns a map with entries for which the predicate function returns true.
 */
Map.prototype.filter = function(predicate) {
  const results = new Map()

  this.forEach((value, key) => {
    if (predicate(key, value, map=this)) {
      results.set(key, value)
    }
  })

  return results
}

/**
 * leftKeys:
 * @param   {Map} map1
 * @param   {Map} map2
 * @return  {Map}
 * @example leftKeys({'a':1,'b':2,'c':3},{'a':1,'b':2,'d':9}) -> Map { 'c' => 3 }
 * 
 * Returns a map of all the keys of map1 that are not found in map2.
 */
function leftKeys(map1, map2) {
  return map1.filter((key, _) => !map2.has(key))
}

const map1 = new Map([['a', 1], ['b', 2], ['c', 3]])
const map2 = new Map([['a', 1], ['b', 2], ['d', 9]])
console.log(leftKeys(map1, map2))
