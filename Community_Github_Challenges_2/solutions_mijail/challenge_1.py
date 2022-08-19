##### Challenge 1 #####

import random



def generator(random_numbers=5):
    """ The generator function return a string of the
        amount of random numbers required in the input.
        If the function are called without parameters
        the default amount of random numbers will be 5. """

    # If the input are string, float or zero, return None
    if random_numbers == 0 or \
       isinstance(random_numbers, (float, str)):
        return

    numbers = ""
    count = 0

    while True:
        number = random.randint(1, 100)
        numbers += str(number)
        
        # Break when all numbers are counted.
        # This is another way to not add the comma
        # at the end. Just for practice.
        if count == random_numbers:
            break
        count += 1
        numbers += ","

    # Uncomment the next line if the output must be a list
    # numbers = list(map(int, numbers.split(",")))

    return numbers
