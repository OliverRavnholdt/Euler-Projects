from math import sqrt
from time import time

''' Modes are:
    Primes which uses n as number of wanted primes.
    Number which uses n as a number returning all primes less or equal to N.
'''
def prime_sieve(n, mode='number', time_display=False):
    start_time = time()

    N = n+1

    primes = [True for i in range(N)]
    primes[0], primes[1] = False, False

    for i in range(int(sqrt(N))):
        if primes[i]:
            for j in range(i*i, len(primes), i):
                primes[j] = False

    end_time = time()

    print(True)

    count = 0
    for i in range(len(primes)):
        if primes[i]:
            print(i)
            count += 1
            if count == 1000: break

    if time_display:
        print("Found primes in:" + str(end_time-start_time))


prime_sieve(1000)