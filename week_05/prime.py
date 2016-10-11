#!/usr/bin/python3

# def genPrime():
#     primes = [2, 3]
#     x = 3
#     while True:
#         x += 2
#         for prime in primes:
#             if x % prime == 0:
#                 primes.append(x)
#                 next = x
#                 yield next
#
def genPrimes():
    primes = [2, 3]
    x = 3
    while x < 100:
        x += 2
        for prime in primes:
            if x % prime == 0:
                break
        else:
            primes.append(x)
            print(primes)
            print(primes[primes.index(x)-2])
            # yield x

genPrimes()
