# Highest Digit Challenge 1
# Create a function that receives a number as an argument and returns
# the highest digit in that number.
def fun(number) -> int:
    """
    This function returns us ...
    :param number: int
    :return: int
    """
    max = 0
    while number > 0:
        digit = number % 10
        if max < digit:
            max = digit
        number = number // 10
    return max


# Drive code
num = 12899
# num = 8123
# num = 193
# num = 1
print(fun(num))


# Case insensitive Comparison Challenge 2
# Write a function that validates whether two strings are identical.
# Remember you need to do it insensitive
def match(string1, string2) -> bool:
    """
    This function returns us ...
    :param string1: str
    :param string2: str
    :return: bool
    """
    if string1.casefold() == string2.casefold():
        return True
    else:
        return False


# Drive code
print(match(string1="Jose", string2="JoSe"))
print(match(string1="water", string2="wait"))
print(match(string1="JOHN", string2="JOHn"))
print(match(string1="ElEmEnTs", string2="eLeMeNtS"))
