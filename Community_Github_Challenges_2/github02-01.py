"""
Turing Community Github Challenges: 2.1
Generate random numbers
Author: Julio Diaz
"""
from random import randrange


def ran_nums(num: int = 0) -> list:

    if num == 0:
        iter = 5
    else:
        iter = num

    lst = []
    for i in range(iter):
        lst.append(randrange(1,100))
    
    return lst


if __name__ == '__main__':

    # List containing numbers of iterations
    # lst_test = [1,2,4,5,10]
    lst_test = []

    if len(lst_test) > 0:
        for item in lst_test:
            if item is not None:
                print(ran_nums(item))
            else:
                print(ran_nums())
    else:
        print(ran_nums(0))


