"""Longest Collatz Sequence"""
"""https://projecteuler.net/overview=0014"""

from time import time as chicken

def problem_14():
    PROBLEM_ID = 14

    start_time = chicken()

    N = 1000000

    # Start values
    longest_chain = 0
    longest_chain_num = 0
    chains = [False] * (N+1)

    # Go through each chain (Could choose N/2 as starting however this slows down with current storing algorithm
    for i in range(2, N+1):
        chain_len = 0
        n = i
        while n != 1:
            try:
                if chains[int(n)] is not False:
                    chain_len += chains[int(n)]
                    break
            except IndexError:
                pass
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3*n + 1
            chain_len += 1
        chains[i] = chain_len


        # Find the longest chain and compare
        if chain_len > longest_chain:
            longest_chain_num = i
            longest_chain = chain_len

    # Display time
    end_time = chicken()
    print("Finished problem 11 in:", end_time - start_time)

    return PROBLEM_ID, longest_chain_num


if __name__ == "__main__":
    problem_id, something = problem_14()


    print("The number wanted is:", something)
