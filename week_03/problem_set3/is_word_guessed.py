def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    guessedWord = ''
    secret_letters = ''
    guess_letters = []
    for letter in secretWord:
        if letter not in secret_letters:
            secret_letters += letter
    for element in lettersGuessed:
        if element not in guess_letters:
            guess_letters.append(element)
            # print(guess_letters)
    for sletter in secret_letters:
        for guess in guess_letters:
            if sletter == guess:
                guessedWord += sletter
                # print(guessedWord)
    return guessedWord == secret_letters

# sword = 'broccoli'
# letterg =  ['z', 'x', 'q', 'b', 'r', 'o', 'c', 'c', 'o', 'l', 'i']
#
# print(isWordGuessed(sword, letterg))
