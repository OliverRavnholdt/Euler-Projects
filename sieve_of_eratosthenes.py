from math import sqrt
from time import time


''' Modes are:
    Primes which uses n as number of wanted primes.
    Number which uses n as a number returning all primes less or equal to N.
'''


def prime_sieve(n, mode='number', time_display=True):
    start_time = time()     # Get start time

    N = n+1     # Assign N

    # Determine what mode is being used
    if mode == 'number':
        primes = number_mode(N)
    elif mode == 'primes':
        primes = prime_mode(N)
    else:
        print("Wrong mode set for sieve!")
        primes = None

    end_time = time()   # End time

    # Display time to users if wanted
    if time_display:
        print("Found primes in:" + str(end_time-start_time))

    return primes


# Number mode function
def number_mode(N):
    # Create list of true values and set 0 and 1 to false
    primes = [True] * N
    primes[0], primes[1] = False, False

    # Iterate from 0 to sqrt of N and mark all multiples as false
    for i in range(int(sqrt(N))):
        if primes[i]:
            for j in range(i*i, len(primes), i):
                primes[j] = False

    # Create list of prime numbers only to return
    prime_return_list = [prime for prime, status in enumerate(primes) if status]
    return prime_return_list


# Prime mode function
def prime_mode(n):
    N = n*2

    # Loop to find all primes again if return list isn't long enough
    while True:
        # Create list of true values and set 0 and 1 to false
        primes = [True] * N
        primes[0], primes[1] = False, False

        # Iterate from 0 to sqrt of N and mark all multiples as false
        for i in range(int(sqrt(N))):
            if primes[i]:
                for j in range(i * i, len(primes), i):
                    primes[j] = False

        # Create list of prime numbers only to return
        prime_return_list = [prime for prime, status in enumerate(primes) if status]

        # Check if list is as long as wanted
        if len(prime_return_list) >= n:
            prime_return_list = prime_return_list[0:n-1]
            break
        else:
            N = N * 2

    return prime_return_list


if __name__ == '__main__':
    print(prime_sieve(1000))
    print(prime_sieve(1000, mode='primes'))
