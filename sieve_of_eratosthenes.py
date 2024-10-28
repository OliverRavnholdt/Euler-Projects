from math import sqrt
from time import time


''' Modes are:
    Primes which uses n as number of wanted primes.
    Number which uses n as a number returning all primes less or equal to N.
'''


def prime_sieve(n, mode='number', time_display=True):
    start_time = time()

    N = n+1

    if mode == 'number':
        primes = number_mode(N)
    elif mode == 'primes':
        primes = prime_mode(N)
    else:
        print("Wrong mode set for sieve!")
        primes = None

    end_time = time()

    if time_display:
        print("Found primes in:" + str(end_time-start_time))

    return primes


def number_mode(N):
    primes = [True for i in range(N)]
    primes[0], primes[1] = False, False

    for i in range(int(sqrt(N))):
        if primes[i]:
            for j in range(i*i, len(primes), i):
                primes[j] = False

    prime_return_list = [prime for prime, status in enumerate(primes) if status]
    return prime_return_list


def prime_mode(n):
    N = n*2
    while True:

        primes = [True for i in range(N)]
        primes[0], primes[1] = False, False

        for i in range(int(sqrt(N))):
            if primes[i]:
                for j in range(i * i, len(primes), i):
                    primes[j] = False

        prime_return_list = [prime for prime, status in enumerate(primes) if status]
        if len(prime_return_list) >= n:
            prime_return_list = prime_return_list[0:n-1]
            break
        else:
            N = N * 2

    return prime_return_list


if __name__ == '__main__':
    print(prime_sieve(1000))
    print(prime_sieve(1000, mode='primes'))