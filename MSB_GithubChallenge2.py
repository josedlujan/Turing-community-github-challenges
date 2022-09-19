# -*- coding: utf-8 -*-
"""
@author: Martin Baudino

Generate random numbers Challenge 1

Create a generator function that allows us to obtain an n number of random
numbers.

The generator must meet the following requirements. The generator must have 
random names. It will be possible to indicate to the generator the amount of 
random numbers to obtain. This of course in the function call. If the number 
of random numbers is not indicated, the default will be 5. The random numbers 
to be returned will range from 1 to 100.
Example

    generatort() -> 0,29,82,1,39 without numbers 5 by default
    generatort(2) -> 130,38 or put the N value

Notes

    No notes

"""

import numpy as np

def generator(amount=5):
    # Random number generation within desired range and amount
    nums = np.random.randint(1, 100, amount)
    return list(nums)


print(generator())
print(generator(2))
print(generator(9))



"""
Even numbers within a sequence Challenge 2

Develop a program which allows us to know all the even numbers that are 
within the range of x and y. The program must meet the following requirements. 
Define a function called range_pairs. The function must have two parameters, x 
and y. the function must receive as arguments the values ​​for x and y. where x 
is a positive number greater than 0 given by the user. where y is a positive 
number greater than x given by the user. The function must return a list with 
all the even numbers that exist between the range x and y. To test the 
programming you can ask the user for the values ​​of x and y via the keyboard. 
The values ​​must be requested outside the function.
Example

    range(10,20) = 10,12,14,16,18
    range(57,80) = 58,60,62,64,66,68,70,72,74,76,78

Notes

    We need to validate the second number need to be higher

"""

def range_pairs(x, y):
    # Numbers validation, fails silently
    if 0 < x < y:
        # List comprehension generates values in one line
        return [num for num in range(x, y) if num % 2 == 0]
    return None

# Testing with user input    
x, y = [int(value) for value in input("Insert two positive numbers: ").split()]
print(range_pairs(x, y))
        


