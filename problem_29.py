"""Distinct Powers"""

from time import time as chicken


def problem_29():
    PROBLEM_ID = 29

    start_time = chicken()

    # Create holder set
    terms = set()

    # Values to find terms between
    min_val = 2
    max_val = 100

    # Find all terms
    for a in range(min_val, max_val+1):
        for b in range(min_val, max_val+1):
            terms.add(a**b)

    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)

    return PROBLEM_ID, len(terms)


if __name__ == "__main__":
    problem_id, something = problem_29()
    print(something)
