# Left Join Dictionaries Challenge 1
def left_keys(dict_a: dict, dict_b: dict) -> tuple:
    """
    This function returns us ...
    :param dict_a: dict
    :param dict_b: dict
    :return: tuple
    """
    view1 = dict_a.keys()
    view2 = dict_b.keys()
    view3 = tuple(view1 - (view1 & view2))
    return view3


dicc_a = {'a': 1, 'b': 2, 'c': 3}
dicc_b = {'a': 1, 'b': 2, 'd': 9}
print(left_keys(dicc_a, dicc_b))


# Sum of even numbers Challenge 2
def sum_pairs(list_of_integers: list) -> int:
    """
    This function returns us ...
    :param list_of_integers: list
    :return: int
    """
    sum_even = 0
    for i in list_of_integers:
        if i % 2 == 0 and i > 0:
            sum_even += i
    return sum_even


argument = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, -2, -4]
argument1 = [2, 2, 2, 5, 4, 2, -2]
argument2 = [2, 1, 3, 5, 6, 10]
print(sum_pairs(argument))
print(sum_pairs(argument1))
print(sum_pairs(argument2))
