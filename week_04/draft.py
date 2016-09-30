#!/usr/bin/python3
# def calculateHandlen(hand):
#     """
#     Returns the length (number of letters) in the current hand.
#
#     hand: dictionary (string-> int)
#     returns: integer
#     """
#     # TO DO... <-- Remove this comment when you code this function
#     num_of_letter = 0
#     for element in hand:
#         num_of_letter += hand[element]
#     return num_of_letter
#
#
#
# hand1 = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
#
#
# print(calculateHandlen(hand1))

def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

hand1 = {'a': 1, 'e': 1, 'h': 1, 'm': 2, 'r': 1}


# displayHand(hand1)
# print('yhvjaschjb:')

print('njxdsvnk', end='')
displayHand(hand1)
