s = 'sazcbobobegghakl'

# def find_vowels(word):
#     vowels = 'aeiou'
#     number_of_vowels = 0
#     for i in word:
#         for n in vowels:
#             if i == n:
#                 number_of_vowels += 1
#     return number_of_vowels
#
# print(find_vowels(s))


vowels = 'aeiou'
number_of_vowels = 0
for i in s:
    for n in vowels:
        if i == n:
            number_of_vowels += 1
print(number_of_vowels)
