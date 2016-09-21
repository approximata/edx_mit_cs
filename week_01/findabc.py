s = 'abcdefghijklmnopqrstuvwxyz'

longest_abc_words = []
current_word = ''
for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        current_word += s[i]
        if i == len(s)-2 and s[-1] >= s[i]:
            current_word += s[-1]
    else:
        current_word += s[i]
        longest_abc_words.append(current_word)
        current_word = ''

longestword = ''
if len(longest_abc_words) == 0:
    longestword = current_word
else:
    for n in range(len(longest_abc_words)):
        if len(longestword) < len(longest_abc_words[n]):
            longestword = longest_abc_words[n]
print(longestword)
