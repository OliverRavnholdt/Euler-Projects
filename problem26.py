"""Reciprocal Cycles"""

from time import time as chicken


def problem_26():
    PROBLEM_ID = 26

    start_time = chicken()

    # Placeholder and iterations
    N = 1000
    largest_sequence = 0
    largest_denominator = 0

    # Loop through all fractions using long division
    for denominator in range(6, 7):
        # List to store remainders to find recurring cycle
        remainders = []

        # Make sure the numerator is larger than the denominator
        numerator = 1
        while numerator != 0:
            while numerator < denominator:
                numerator *= 10

            # Break the loop if indication of cycle
            if numerator % denominator in remainders:
                break

            # Add the remainder to the remainder list
            remainders.append(numerator % denominator)

            # Calculate the next numerator for long division
            numerator = numerator % denominator

        # When loop breaks find the length of the cycle
        i = remainders.index(numerator % denominator)
        remainders = remainders[i:]

        # Check if this cycle is the largest cycle so far
        if len(remainders) > largest_sequence:
            largest_sequence = len(remainders)  # To check next cycles
            largest_denominator = denominator   # Needed as return value

    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)

    return PROBLEM_ID, largest_denominator


if __name__ == "__main__":
    problem_id, something = problem_26()
    print("This took a while but it works now :) Here it is:", something)
