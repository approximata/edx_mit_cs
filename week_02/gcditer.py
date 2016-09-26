def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    # divider = 0
    # if a > b:
    #     divider = b
    #     while divider > 0:
    #         if a % divider == 0 and b % divider == 0:
    #             return divider
    #         divider -= 1
    # else:
    #     divider = a
    #     while divider > 0:
    #         if b % divider == 0 and a % divider == 0:
    #             return divider
    #         divider -= 1
    if b == 0:
        return a
    else:
        return gcdIter(b, a % b)




print(gcdIter(30, 100))
