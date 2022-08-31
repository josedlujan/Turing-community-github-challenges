"""
Turing Community Github Challenges: 1.1
Highest digit
Author: Julio Diaz
"""


def highestDigit(num: int) -> int:

    lst = str(num)
    max_num = max(lst)
    return max_num


if __name__ == '__main__':

    lst_test = [12899, 8123, 193, 1]

    if len(lst_test) > 0:
        for num in lst_test:
            print(highestDigit(num))
    else:
        print('There are no items to test.')

