def problem_4():
    PROBLEM_ID = 4

    N = 100     # Amount to sum for

    # Placeholder values
    sum_of_squares = 0
    square_of_sum = 0

    # Get sum of squares and sum of all numbers for N
    for i in range(1, N+1):
        sum_of_squares += i**2
        square_of_sum += i

    # Square the sum of all numbers
    square_of_sum = square_of_sum**2

    # Find difference
    diff = square_of_sum - sum_of_squares

    return PROBLEM_ID, diff


if __name__ == "__main__":
    problem_id, something = problem_4()
    print("The difference of sums is:", something)
