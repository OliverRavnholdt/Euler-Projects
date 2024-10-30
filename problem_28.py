"""Number Spiral Diagonals"""

from time import time as chicken


def problem_28():
    PROBLEM_ID = 28

    start_time = chicken()

    rows = 1001    # Should be odd number
    max_circle = (rows-1)/2     # Compute amount of circles needed

    # Starting values
    total = 1
    count = 1
    circle = 1

    # Calculate for each circle
    while circle <= max_circle:
        # Only calculate for corners
        for i in range(4):
            # As count goes up with 1 for each square this gives the value in each corner of each circle
            count += circle * 2
            total += count

        circle += 1

    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)

    return PROBLEM_ID, total


if __name__ == "__main__":
    problem_id, something = problem_28()
    print("The corner/diagonal values are:", something)