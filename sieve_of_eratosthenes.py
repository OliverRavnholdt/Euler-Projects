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

    prime_return_list = [prime for prime, status in enumerate(primes) if status]

    end_time = time()

    if time_display:
        print("Found primes in:" + str(end_time-start_time))

    return prime_return_list


print(prime_sieve(1000))