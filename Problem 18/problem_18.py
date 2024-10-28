"""Maximum Path Sum I
https://www.youtube.com/watch?v=v0fR9xPEbEk"""

from time import time as chicken

def problem_18():
    PROBLEM_ID = 18

    start_time = chicken()

    # Get all rows from file
    rows = []
    with open('input18.txt', 'r') as file:
        for line in file:
            rows.append(list(map(int, line.split(" "))))

    # Use the pathfinder function to find the best path
    new_triangle = path_finder(rows)

    return PROBLEM_ID, new_triangle[-1][0]


# Pathfinder function starting from the bottom to find best path
def path_finder(rows):
    new_rows = [list() for i in range(len(rows))]

    # Find the best path for each row
    for i, row in enumerate(reversed(rows)):
        # Skip last row
        if i == 0:
            new_rows[i] = row
            continue

        # Find the max of the two options of where to go
        for j in range(len(row)):
            new_rows[i].append(max(row[j]+new_rows[i-1][j], row[j]+new_rows[i-1][j+1]))

    return new_rows


if __name__ == "__main__":
    problem_id, something = problem_18()
    print("This is the largest number:", something)
