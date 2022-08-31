"""
Turing Community Github Challenges: 3.2
Sum of even numbers
Author: Julio Diaz
"""


def sum_pairs(lst_test: list) -> int:
    
    sum = 0
    for i in lst_test:
        if i % 2 == 0:
            sum += i
    
    return sum


if __name__ == '__main__':
    lst_test = [[1,2,3,4,5,6,7,8,9,10,12], [2,2,2,5,4,2], [2,1,3,5,6,10]]
    if len(lst_test) > 0:
        for i in lst_test:
            print(sum_pairs(i))
    else:
        print('There are no items to test.')