#!/usr/bin/python3

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    elif exp >= 1:
        return base*iterPower(base, exp-1)
    # result = 1
    # while exp > 0:
    #     result *= base
    #     exp -= 1
    #
    # return result

print(iterPower(2,3))
