"""
Turing Community Github Challenges: 2.2
Even numbers within a sequence
Author: Julio Diaz
"""


def range_pairs(x: int, y: int) -> list:

    result = []

    for x in range(x, y):
        if x % 2 == 0:
            result.append(x)

    return result


if __name__ == '__main__':

    # x must be a positive integer greater than 0
    # y must be a positive number greater than x
    n1, n2 = input("Enter two numbers (separated by one space): ").split()
    x = int(n1)
    y = int(n2)
    
    if x > 0 and y > x:
        print(range_pairs(x, y))
    else:
        print("'x' is not greater than 0 or 'y' is not greater than x")


