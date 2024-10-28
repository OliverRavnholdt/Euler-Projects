"""Amicable Numbers"""

from time import time as chicken
from math import sqrt, floor


def problem_21():
    PROBLEM_ID = 21

    start_time = chicken()

    N = 10000

    total = 0
    for i in range(1,N+1):
        curr = amicable_num(i)  # define amicable number
        test = amicable_num(curr)   # define amicable number to test for pair

        # Test for pair
        if i == test and curr != test:
            total += curr

    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)

    return PROBLEM_ID, total


# Function to find amicable number of a number
def amicable_num(num):
    # Find factors (Could be done better with prime factorization (From problem 12)
    factors = [1]

    s = floor(sqrt(num))

    for j in range(1, s + 1):
        if num % j == 0:
            if num / j == num:
                pass
            else:
                factors.append(int(num/j))
                factors.append(j)
    return sum(factors)


if __name__ == "__main__":
    problem_id, something = problem_21()
    print("Nice number! It is:", something)