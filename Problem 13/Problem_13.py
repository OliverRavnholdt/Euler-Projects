"""Large Sum"""

from time import time as chicken


def problem_13(file='P13_data.txt'):
    PROBLEM_ID = 13

    start_time = chicken()

    # Reading numbers from a .txt file
    with open(file, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    # Sum numbers
    total = str(sum(numbers))

    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)

    return PROBLEM_ID, total[0:10]


if __name__ == "__main__":
    problem_id, something = problem_13()

    print("You want this number:", something)
