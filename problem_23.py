"""Non-Abundant Sums"""

from time import time as chicken
from math import sqrt, floor


def problem_23():
    PROBLEM_ID = 23

    start_time = chicken()

    sum_list = [False] * (28123+1)
    abundant_list = []

    # Find all abundant numbers
    for i in range(1, len(sum_list)):
        if abundant_check(i):
            abundant_list.append(i)

    # Mark all values that can be written as a sum as True
    for i in abundant_list:
        for j in abundant_list:
            if i + j < len(sum_list):
                sum_list[i+j] = True
            else:
                break

    # Sum all numbers that can't be written as a sum of TWO abundant numbers
    total = 0
    for num, status in enumerate(sum_list):
        if not status:
            total += num


    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)

    return PROBLEM_ID, total


def abundant_check(num):
    # Find factors (Could be done better with prime factorization (From problem 23)
    factors = {1}

    s = floor(sqrt(num))

    for j in range(1, s + 1):
        if num % j == 0:
            if num / j == num:
                pass
            else:
                factors.add(int(num/j))
                factors.add(j)

    return sum(factors) > num


if __name__ == "__main__":
    problem_id, something = problem_23()
    print("Your lucky number is:", something)
