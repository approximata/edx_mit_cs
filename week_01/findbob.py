s = 'azcbobobegghaklbob'

number_of_bob = 0
for i in range(len(s)-2):
    if s[i] + s[i+1] + s[i+2] == 'bob':
        number_of_bob += 1
print(number_of_bob)
