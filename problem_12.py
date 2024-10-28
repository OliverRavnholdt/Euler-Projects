"""Highly Divisible Triangular Number"""

from time import time as chicken
from math import sqrt, floor


def problem_12():
    PROBLEM_ID = 12

    start_time = chicken()

    close = False
    i = 1

    while True:
        number = triangle_num(i)
        factors = 0

        s = floor(sqrt(number))

        for j in range(1, s+1):
            if number % j == 0:
                if number / j == s:
                    factors += 1
                else:
                    factors += 2
        if factors >= 500:
            break

        i += 1

    end_time = chicken()
    print("Finished problem 11 in:", end_time - start_time)

    return PROBLEM_ID, number

def triangle_num(n):
    num = 0
    for i in range(n+1):
        num += i
    return num

if __name__ == "__main__":
    problem_id, something = problem_12()
    print("The number you want is:", something)
