"""Reciprocal Cycles"""

from time import time as chicken


def problem_26():
    PROBLEM_ID = 26

    start_time = chicken()

    N = 1000
    largest_sequence = 0

    for denominator in range(1, 1000):
        denominators = []
        numerator = 1
        while numerator != 0:
            while numerator < denominator:
                numerator *= 10

            if numerator % denominator in denominators:
                i = denominators.index(numerator % denominator)
                denominators = denominators[i:]
                break

            denominators.append(numerator % denominator)
            numerator = numerator % denominator

        if len(denominators) > largest_sequence:
            largest_sequence = denominator

    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)


    return PROBLEM_ID, largest_sequence


if __name__ == "__main__":
    problem_id, something = problem_26()
    print((something))