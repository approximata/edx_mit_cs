#!/usr/bin/python3
#
# def applyToEach(L, f):
#     for i in range(len(L)):
#         L[i] = f(L[i])
#     return L
#
# testList = [1, -4, 8, -9]
#
# def abs_value(element):
#     return abs(element)
#
# def duplicate(element):
#     return element*2
#
# def powertwo(element):
#     return element**2
#
#
# print(abs_value(-5))
# print(applyToEach(testList, abs_value))

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

print(applyEachTo([inc, square, halve, abs], 3.0))
