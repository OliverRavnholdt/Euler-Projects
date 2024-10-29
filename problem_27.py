"""Quadratic Primes"""

from time import time as chicken
from sieve_of_eratosthenes import prime_sieve


def problem_27():
    PROBLEM_ID = 27

    start_time = chicken()

    # Find some given primes could be more than 200 if a and b are larger
    prime_list = prime_sieve(200, mode='prime', time_display=True)
    largest_n = 0
    largest_product = 0

    # Brute force all a and b from -1000 to 1000
    for a in range(-1000,1000+1):
        for b in range(-1000,1000+1):
            n = 0
            # Check if consecutive n are prime numbers otherwise break
            while True:
                num = n**2 + a*n + b    # Formula from problem
                if num not in prime_list:
                    if n > largest_n:
                        # Store largest n and the product
                        largest_n = n
                        largest_product = a*b
                    break
                n += 1

    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)

    return PROBLEM_ID, largest_product


if __name__ == "__main__":
    problem_id, something = problem_27()
    print("The largest product is:", something)