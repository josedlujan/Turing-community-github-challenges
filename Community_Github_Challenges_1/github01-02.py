"""
Turing Community Github Challenges: 1.2
Case insentive comparison
Author: Julio Diaz
"""


def match(str1: str, str2: str) -> bool:
    
    if str(str1).lower() == str(str2).lower():
        return True
    else:
        return False


if __name__ == '__main__':
    
    lst_test = [("Jose","JoSe"), ("water","wait"), ("JOHN", "JOHn"), ("ElEmEnTs", "eLeMeNtS")]

    if len(lst_test) > 0:
        for item in lst_test:
            print(match(item[0], item[1]))
    else:
        print('There are no items to test.')


