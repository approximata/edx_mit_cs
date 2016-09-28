#!/usr/bin/python3

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    abc = list(string.ascii_lowercase)

    for guess in lettersGuessed:
        if guess in abc:
            abc.remove(guess)

    return ''.join(abc)




# letters = ['e', 'i', 'k', 'p', 'r', 's']
#
# print(getAvailableLetters(letters))
