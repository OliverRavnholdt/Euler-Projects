def problem_10():
    PROBLEM_ID = 10

    sum = sieve_of_eratosthenes(2000000)

    return PROBLEM_ID, sum


def sieve_of_eratosthenes(max_num):
    numbers = list(range(3, max_num+1, 2))

    that = 3
    while True:
        deserving_removal = [num for num in numbers if num % that == 0]
        for elem in deserving_removal:
            numbers.remove(elem)
            print(elem)
        print(True)

    return True




if __name__ == "__main__":
    problem_id, something = problem_10()
    print(something)