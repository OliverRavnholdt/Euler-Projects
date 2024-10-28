"""Power Digit Sum"""

from time import time as chicken

def problem_16(n):
    PROBLEM_ID = 16

    # Find the first number
    number = str(2**n)

    # Find the sum of each digit added together
    total = 0
    for i in number:
        total += int(i)

    return PROBLEM_ID, total


if __name__ == "__main__":
    problem_id, something = problem_16(1000)
    print(something)
