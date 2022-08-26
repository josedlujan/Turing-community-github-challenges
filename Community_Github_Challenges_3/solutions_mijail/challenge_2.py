##### Challenge 2 #####


def sum_pairs(*args):
    """Returns the sum of all even numbers in a list of numbers.

    Parameters:
        *args : tuple
            A variable amount of positve numbers.

    Returns:
        int
            The sum of all even numbers.
    """

    # The following lines of code add more functionality
    # for other cases when there are lists or tuples in the
    # input elements. Does't work with nested lists and tuples.
    elements = list(args)
    for element in args:
        if isinstance(element, (list, tuple)):
            elements.remove(element)
            elements += element
        
    def is_even(element):
        # Return True if the element is even otherwise False
        if isinstance(element, (str, float)) or element < 0:
            return False
        return element & 1 == 0

    return sum(filter(is_even, elements))

