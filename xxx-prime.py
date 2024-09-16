from largest_prime_factor import is_prime


# This could probably be optimized to not check for every number
def problem_7():
    PROBLEM_ID = 7

    wanted_count = 10001    # Wanted prime number

    # Placeholders for prime count and number counter
    count = 0
    num = 0
    while True:
        num += 1

        # Uses function from project ID 3 to check if the number is prime
        if is_prime(num):
            count += 1
            if count == wanted_count:
                print(count)
                break

    return PROBLEM_ID, num


if __name__ == "__main__":
    problem_id, something = problem_7()
    print("The number you want is:", something)
