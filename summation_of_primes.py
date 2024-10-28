from sieve_of_eratosthenes import prime_sieve

def problem_10():
    PROBLEM_ID = 10

    N = 2000000

    prime_list = prime_sieve(n=N-1, mode='number')

    return PROBLEM_ID, sum(prime_list)


if __name__ == "__main__":
    problem_id, something = problem_10()
    print("The sum is: " + str(something))