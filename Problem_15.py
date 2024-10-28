"""Lattice Paths
https://stemhash.com/counting-lattice-paths/"""

from time import time as chicken


def problem_15(n, k):
    PROBLEM_ID = 15

    start_time = chicken()

    # Define n as from n choose k
    n = n + k

    # Calculate the factorials
    fac_n = 1
    fac_k = 1
    fac_kn = 1

    for i in range(1, n + 1):
        fac_n *= i

    for i in range(1, k + 1):
        fac_k *= i

    if n - k == 0:
        fac_kn = 1
    else:
        for i in range(1, int(n - k) + 1):
            fac_kn *= i

    # Calculate total
    total = fac_n / (fac_kn * fac_k)

    # Display time
    end_time = chicken()
    print("Finished problem 11 in:", end_time - start_time)

    return PROBLEM_ID, int(total)


if __name__ == "__main__":
    problem_id, something = problem_15(20, 20)
    print("Here the number is boss:", something)
