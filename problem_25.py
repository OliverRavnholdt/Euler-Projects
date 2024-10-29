"""1000-digit Fibonacci Number"""

from time import time as chicken


def problem_25():
    PROBLEM_ID = 25

    start_time = chicken()

    fib_list = [1, 1]
    wanted_len = 1000

    # Find fib numbers and break when number is longer than 1000 characters
    while True:
        fib_list.append(fib_list[-1]+fib_list[-2])
        if len(str(fib_list[-1])) == 1000:
            break

    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)

    return PROBLEM_ID, len(fib_list)


if __name__ == "__main__":
    problem_id, something = problem_25()
    print(something)
