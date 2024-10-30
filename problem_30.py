"""Digit Fifth Powers"""

from time import time as chicken


def problem_30():
    PROBLEM_ID = 30

    start_time = chicken()

    # Start definitions
    power = 5
    end_val = power*(9**power)  # Max value
    power_sum = 0

    # Iterate through all values
    for num in range(2, end_val):
        total = num     # Save to compare
        num = list(str(num))    # Convert to list to get individual numbers

        # Find the power of each number and add together
        tester = 0
        for i in num:
            tester += int(i)**power

        # Check if the same and sum up
        if tester == total:
            power_sum += tester

    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)

    return PROBLEM_ID, power_sum


if __name__ == "__main__":
    problem_id, something = problem_30()
    print("The total sum is:", something)
