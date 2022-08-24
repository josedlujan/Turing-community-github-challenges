from random import randrange

def random_nums(n=0):
    
    lst = []
    if n == None or n == 0:
        n =5
        
    for n in range(0,n):
        num = randrange(1,100)
        lst.append(num)
    return lst


if __name__ == '__main__':
    print(random_nums(3))
