"""Reciprocal Cycles"""

from time import time as chicken


def problem_26():
    PROBLEM_ID = 26

    start_time = chicken()

    N = 1000

    for i in range(2,10):
        count = 1
        m = 1  # Multiplier
        first_decimal = 0
        while first_decimal == 0:
            m *= 10
            first_decimal = m//i
            remainder = m % i

        next_decimal = first_decimal

        while True:
            prev_decimal = next_decimal
            next_decimal = (remainder*10)//i
            remainder = (remainder*10-next_decimal*i) % i

            if remainder == 0 or next_decimal == first_decimal or next_decimal == prev_decimal:
                print(count, i)
                break
            count += 1

    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)


    return PROBLEM_ID, 1


if __name__ == "__main__":
    problem_id, something = problem_26()