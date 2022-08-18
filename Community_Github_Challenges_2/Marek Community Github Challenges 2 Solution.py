# Generate random numbers Challenge 1
import random


def generatort(num=5) -> list:
    """
    This function returns us ...
    :param num: int
    :return: list
    """
    randomlist = []
    for i in range(0, num):
        digits = random.randint(1, 100)
        randomlist.append(digits)
    return randomlist


# Drive code
print(generatort())
print(generatort(2))
# Or.
# Uncomment the code below to put the value of N
# print("Put the N value")
# N = input()
# print(generatort(int(N)))


# Even numbers within a sequence Challenge 2
def range_pairs(x, y) -> list:
    """
    This function returns us ...
    :param x: int
    :param y: int
    :return: list
    """
    even_numbers = []
    for i in range(x, y):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers


x = input("Enter the first parameter x, where x is a positive number greater than 0 and less than 100: ")
y = input("Enter the second parameter y, where y is a positive number greater than 0, greater than x and less than "
          "100: ")

while x > y:
    print("Input invalid")
    y = input("Enter the second parameter y, where y is a positive number greater than 0, greater than x and less "
              "than 100: ")

print(range_pairs(int(x), int(y)))
