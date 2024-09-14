def problem_1():
    PROBLEM_ID = 1
    N = 1000  # Amount to sum all multiples under
    multiples = [3, 5]  # Numbers to check for multiples

    total = 0
    for n in range(N):
        for i in multiples:
            if n % i == 0:
                total += n
                break

    return PROBLEM_ID, total


if __name__ == "__main__":
    problem_id, total = problem_1()
    print("The total is:", total)
