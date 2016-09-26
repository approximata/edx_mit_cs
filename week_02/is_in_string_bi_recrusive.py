#!/usr/bin/python3

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    aStr = ''.join(sorted(aStr))
    print(aStr)
    if len(aStr) == 0:
        return False
    if len(aStr) == 1:
        return True if aStr == char else False
    if char == aStr[int(len(aStr)/2)]:
        return True
    else:
        if char > aStr[int(len(aStr)/2)]:
            return isIn(char, aStr[int(len(aStr)/2)+1:])
        else:
            return isIn(char, aStr[:int(len(aStr)/2)])

print(isIn('q', 'iqrw'))
