"""Reciprocal Cycles"""

from time import time as chicken


def problem_26():
    PROBLEM_ID = 26

    start_time = chicken()

    N = 1000
    max_count = 0

    for i in range(1,1000):
        count = 1
        num_list = []
        m = 1  # Multiplier
        first_decimal = 0
        while first_decimal == 0:
            m *= 10
            first_decimal = m//i
            remainder = m % i

        next_decimal = first_decimal


        while True:
            num_list.append(next_decimal)
            prev_decimal = next_decimal
            next_decimal = (remainder*10)//i
            print(first_decimal, next_decimal, prev_decimal, remainder)

            if remainder == 0 or next_decimal == first_decimal or next_decimal == prev_decimal or count==10000:
                if next_decimal == prev_decimal and next_decimal != first_decimal:
                    count -= 1
                if count > max_count and count != 10000:
                    max_count = count
                break
            remainder = (remainder * 10 - next_decimal * i) % i
            count += 1

    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)


    return PROBLEM_ID, max_count


if __name__ == "__main__":
    problem_id, something = problem_26()
    print((something))