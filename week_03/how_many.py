#!/usr/bin/python3

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    len_of_value = 0
    for key in aDict:
        len_of_value += len(aDict[key])
    return len_of_value


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(animals)


print(how_many(animals))
