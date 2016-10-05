#!/usr/bin/python3

def f(a, b):
    return a + b

def dict_interdiff(d1, d2):
    intersect = {}
    difference = {}
    for key1 in d1:
        if key1 in d2:
            intersect[key1] = f(d1[key1], d2[key1])
            del d2[key1]
        else:
            difference[key1] = d1[key1]
    for key2 in d2:
        difference[key2] = d2[key2]

    return (intersect, difference)


d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}


print(dict_interdiff(d1, d2))
