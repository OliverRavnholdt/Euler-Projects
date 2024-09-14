def problem_2():
    PROBLEM_ID = 2

    fib_max = 4 * (10**6)

    # First two terms of fib numbers
    fib_num_prev = 0
    fib_num = 1

    total = 0   # Sum
    while True:
        # Check that fib number isn't more than max value
        if fib_num > fib_max:
            break

        # Check if fib number is even
        if fib_num % 2 == 0:
            total += fib_num

        # Get next fib number and store prev
        fib_num += fib_num_prev
        fib_num_prev = fib_num - fib_num_prev

    return PROBLEM_ID, total


if __name__ == "__main__":
    problem_id, num = problem_2()
    print("The total is:", num)
