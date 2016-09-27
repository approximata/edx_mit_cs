#!/usr/bin/python3

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    newTup = ()
    i = 0
    for element in aTup:
        if i%2 == 0:
            newTup += (element,)
        i += 1
    return newTup


tupika = ('I', 'am', 'a', 'test', 'tuple')

print(oddTuples(tupika))
