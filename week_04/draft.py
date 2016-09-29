#!/usr/bin/python3
def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    num_of_letter = 0
    for element in hand:
        num_of_letter += hand[element]
    return num_of_letter



hand1 = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}


print(calculateHandlen(hand1))
