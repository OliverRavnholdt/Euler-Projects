def problem_9():
    PROBLEM_ID = 9

    a = 3
    b = 4
    c = 5

    while True:
        k = 1
        if a**2 + b**2 == c**2:
            sum = a + b + c
            print(sum)
            if sum == 1000:
                break
        a = a / k
        b = b / k
        c = c / k

        k += 1

        a = a*k
        b = b*k
        c = c*k



    return PROBLEM_ID, a*b*c


if __name__ == "__main__":
    problem_id, something = problem_9()