
print('please guess a number beetween 0 and 100')
min = 0
max = 100

while True:
    guess = int((min + max) / 2)
    while True:
        print('is your secret number', guess, '?')
        user_input = input('Enter h for gigh, l fot low and c for corret guess:')
        if user_input in 'hlc':
            break
        else:
            print('Sorry, I did not understand your input.')
    if user_input == 'l':
        min = guess
    elif user_input == 'h':
        max = guess
    elif user_input == 'c':
        print('Game over. Your secret number was: {}'.format(guess))
        break
