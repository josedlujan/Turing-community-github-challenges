def range_pairs(x, y):
    lst = []
    if x < y:
        for n in range(x,y):
            if n % 2 == 0:
                lst.append(n)
        return lst
    
    else:
        return None


if  __name__ == '__main__':
    print(range_pairs(3,10))
    # I have to write code to enter the two numbers
