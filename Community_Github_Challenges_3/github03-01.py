"""
Turing Community Github Challenges: 3.1
Left join dictionaries
Author: Julio Diaz
"""


def left_keys(dict_a: dict, dict_b: dict) -> tuple:
    
    result = []
    
    for a in dict_a.keys():
        if a not in dict_b:
            result.append(a)
    
    return tuple(result)


if __name__ == '__main__':

    dict_a = {'a':1, 'b':2, 'c':3}
    dict_b = {'a':1, 'b':2, 'd':9}

    if len(dict_a) and len(dict_b) > 0:
        print(left_keys(dict_a, dict_b))
    else:
        print('Error: Dictionaries must contain items.')
