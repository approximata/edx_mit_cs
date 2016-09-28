#!/usr/bin/python3

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    guessedWord = []
    single_guessed_letters = []
    for element in lettersGuessed:
        if element not in single_guessed_letters:
            single_guessed_letters.append(element)
            # print(single_guessed_letters)
    for i in range(len(secretWord)):
        for guess in single_guessed_letters:
            if secretWord[i] == guess:
                guessedWord += secretWord[i]
        if len(guessedWord) == i:
            guessedWord.append('_ ')
    return ''.join(guessedWord)

# sword = 'broccoli'
# letterg =  ['z', 'x', 'q', 'r', 'o', 'l', 'i']
#
# print(getGuessedWord(sword, letterg))
