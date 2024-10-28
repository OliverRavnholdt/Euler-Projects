"""Factorial Digit Sum"""

from time import time as chicken


def problem_20():
    PROBLEM_ID = 20

    start_time = chicken()

    N = 100

    # Find factorial
    fac = 1
    for i in range(1, N+1):
        fac *= i

    fac = str(fac)

    # Sum each integer
    total = 0
    for num in fac:
        total += int(num)

    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)

    return PROBLEM_ID, total


if __name__ == "__main__":
    problem_id, something = problem_20()
    print("You want this number:", something)
