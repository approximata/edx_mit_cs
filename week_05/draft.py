#!/usr/bin/python3
import string

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        # self.valid_words = load_words(WORDLIST_FILENAME)


    def build_shift_dict(self, shift):

        new_lower = string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
        new_upper = string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift]
        theDic = {}

        for i in range(len(string.ascii_lowercase)):
            theDic[string.ascii_lowercase[i]] = new_lower[i]

        for i in range(len(string.ascii_uppercase)):
            theDic[string.ascii_uppercase[i]] = new_upper[i]

        return theDic

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        thecorrectdic = self.build_shift_dict(shift)
        new_message = ''
        for letter in self.message_text:
            if letter in string.punctuation or letter in string.digits or letter == ' ':
                new_message += letter
            else:
                new_message += thecorrectdic[letter]

        return new_message

thesecret = Message('abc AB3C]');

print(thesecret.apply_shift(4))
