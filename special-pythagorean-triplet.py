def problem_9():
    PROBLEM_ID = 9

    # Starting m and n
    m = 2
    n = 1

    while True:
        # Definitions of n and m per this link
        # https://en.wikipedia.org/wiki/Pythagorean_triple
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2

        # Check if total is 1000
        if a**2 + b**2 == c**2:
            total = a + b + c
            if total == 1000:
                break

        # Increment m
        m += 1

        # Iterate for n + 100 size m and then repeat for new n.
        # This might not find the value wanted value so a tweak of the value 100 might be necessary
        if m == n+100:
            n += 1
            m = n + 1

    product = a*b*c
    return PROBLEM_ID, product


if __name__ == "__main__":
    problem_id, something = problem_9()
    print("The product abc is:", something)