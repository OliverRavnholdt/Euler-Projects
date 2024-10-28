"""Maximum Path Sum II
Fun fact: This was the first problem not completed in order as a test of problem 18.
This problem is basically copy-pasted from problem 18"""

from time import time as chicken
import os
from Problem_18 import problem_18


def problem_67():
    PROBLEM_ID = 67

    start_time = chicken()

    # Get all rows from file
    rows = []
    with open('0067_triangle.txt', 'r') as file:
        for line in file:
            rows.append(list(map(int, line.split(" "))))

    # Use the pathfinder function to find the best path
    new_triangle = problem_18.path_finder(rows)

    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)

    return PROBLEM_ID, new_triangle[-1][0]


if __name__ == "__main__":
    problem_id, something = problem_67()
    print("This is the largest number:", something)