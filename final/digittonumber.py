# def general_poly (L):
#     """ L, a list of numbers (n0, n1, n2, ... nk)
#     Returns a function, which when applied to a value x, returns the value
#     n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
#     #YOUR CODE HERE
#     def function_to_poly(L, x):
#         new_value = 0;
#         for i in range(len(L)):
#             power = (len(L)-1) - i
#             # print(power, 'power')
#             # print(L[i], 'value')
#             new_value += L[i] * (x**power)
#
#         # print(new_value)
#         return new_value
#
# cucc = [1, 2, 3, 4]
#
# general_poly(cucc)

# Paste your code here
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    def function_to_poly(L, x):
        power = len(L) - 1
        sum = 0
        for number in L:
            sum += number * x ** power
            power -= 1
        return sum

    def function(x, l=L):
        return function_to_poly(l, x)

    return function


cucc = [1, 2, 3, 4]

x = 10

print(general_poly(cucc))
