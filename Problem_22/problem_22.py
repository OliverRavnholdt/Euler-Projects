"""Names Scores"""

from time import time as chicken


def problem_22():
    PROBLEM_ID = 22

    start_time = chicken()


    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)

    return PROBLEM_ID, 1


if __name__ == "__main__":
    problem_id, something = problem_22()