def problem_3():
    PROBLEM_ID = 3

    start_num = 600851475143    # Wanted number to get the largest prime factor of

    curr_prime = 0  # Prime number placeholder
    while True:
        # Find next prime number
        curr_prime += 1
        while not is_prime(curr_prime):
            curr_prime += 1

        # Using the division method to see if the current prime number is a factor of the wanted number
        if start_num % curr_prime == 0:
            start_num = start_num / curr_prime  # Define next number to use division method on

            # Check if all factors have been found
            if start_num == 1:
                break
            else:
                curr_prime = 0

    return PROBLEM_ID, curr_prime


# Function to check if number is prime number
def is_prime(num):
    # Hard coded solution for 0 and 1
    if num == 0 or num == 1:
        return False

    # Check if dividable by any other number than 0 or itself
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    problem_id, something = problem_3()
    print("The highest prime factor is:", something)
