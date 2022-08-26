##### Challenge 1 #####


def left_keys(dict_a, dict_b):
    """Returns the difference of keys between two dictionaries.

    Compares two dictionaries to find all keys of the first dictionary
    that does not exist in the second dictionary.
    
    Parameters:
        dict_a : dict
        dict_b : dict

    Returns:
        A tuple of dictionary keys.
        example:

        (key, )
    """
    
    d = set(dict_a.keys())
    f = set(dict_b.keys())
    
    return tuple(d.difference(f))

