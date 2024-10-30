"""Coin Sums"""
"""CHAT GPT NEED TO REDO!!!!!!"""

from time import time as chicken


def problem_31():
    PROBLEM_ID = 31

    start_time = chicken()

    def count_combinations(target, coins, index):
        # If the target is 0, we've found a valid combination
        if target == 0:
            return 1

        # If the target is less than 0, return 0 (invalid combination)
        if target < 0:
            return 0

        count = 0
        # Try to build combinations
        for i in range(index, len(coins)):
            count += count_combinations(target - coins[i], coins, i)  # allow the same coin

        return count

    # List of coin denominations in cents
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    # Count all combinations that make 100 cents
    total_combinations = count_combinations(200, coins, 0)
    print(f'Total combinations to make a dollar: {total_combinations}')

    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)

    return PROBLEM_ID, 1


if __name__ == "__main__":
    problem_id, something = problem_31()
    print((something))
