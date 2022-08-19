##### Challenge 2 #####


class Even:
    def __init__(self):
        print("Welcome!")
        print("The program returns all even numbers in range you choose.")
    

    def range_pairs(self, start, end):
        """ The function returns a list of all even numbers in range x and y. """

        # If the second parameter is less than the first then the values ​​​​will be inverted.
        if start > end:
            start, end = end, start

        pairs = []
        for number in range(start, end):
            # Checks if the number is pair with bitwise AND.
            if number & 1 == 0:
                pairs.append(number)

        # Uncomment the next line if the output must be a string.
        # return ",".join(str(pair) for pair in pairs) 

        # Comment or delete the next line if the output must be a string like: 10,12,14,16,18.
        return pairs



def run():
    """ Checks if there are valid values in the input. """

    try:
        x, y = [int(x) for x in input("Write two integers separated by space: ").split()]
        
        if x < 0 or y < 0:
            print("Introduce only positive numbers.", end='\n\n')
            return run()

    except ValueError as err:
        print("Error: {}. Try again! ".format(err), end='\n\n')
        return run()

    return x, y





if __name__ == "__main__":
    even = Even()
    start, end = run()
    print(even.range_pairs(start, end))
