"""
Pandigital Products

This could be done in many ways, but I found this approach the most fun and pretty fast.
Enjoy! :D
"""

from time import time as chicken


def problem_32():
    PROBLEM_ID = 32

    start_time = chicken()

    # List to match with
    match_str = "".join(map(str, list(range(1, 10))))

    # Placeholders
    sum_list = set()
    total = 0

    # Using 1 or 2 digit multipliers
    for i in range(1, 100):
        # Using 3 or 4 digit multipliers
        for j in range(100, 10000):
            ij = i * j  # product

            # Continue to save time if product already found
            if ij in sum_list:
                continue

            # Create a string to check if matches original string
            check_str = str(ij) + str(i) + str(j)

            # End early if length is too long or if 0 is in the string
            if len(check_str) != len(match_str) or "0" in check_str:
                continue

            # Used to validate if it should be added to total
            yes = True

            # Check that each character only appears once
            for char in match_str:
                if check_str.count(char) != 1:
                    yes = False
                    break

            # If there is only one of each character then add product to total
            if yes:
                sum_list.add(ij)
                total += ij

    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)

    return PROBLEM_ID, total


if __name__ == "__main__":
    problem_id, something = problem_32()
    print("The sum is:", something)
