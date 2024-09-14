def problem_5():
    PROBLEM_ID = 5

    num = 1

    the_range = [1, 20]

    while True:
        yes = True
        for i in range(the_range[0], the_range[1]):
            if num % i != 0:
                num += 1
                yes = False
                break
        if yes:
            break

    return PROBLEM_ID, num


if __name__ == "__main__":
    problem_id, something = problem_5()
    print("The difference of sums is:", something)