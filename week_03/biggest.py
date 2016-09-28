#!/usr/bin/python3

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    len_of_value = 0
    key_of_biggest = ''
    for key in aDict:
        if len_of_value < len(aDict[key]):
            len_of_value = len(aDict[key])
            key_of_biggest = key
    tuple1 = (key_of_biggest, len_of_value)

    return tuple1[0]


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(animals)


print(biggest(animals))
