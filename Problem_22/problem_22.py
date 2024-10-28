"""Names Scores"""

from time import time as chicken
import string


def problem_22():
    PROBLEM_ID = 22

    start_time = chicken()

    # Uppercase alphabet
    alphabet_uppercase = list(string.ascii_uppercase)

    # Get all names from file
    names = []
    with open('0022_names.txt', 'r') as file:
        names = file.readline().split(',')
        names = [x.replace("\"", '') for x in names]
        names.sort()

    # Find total score
    score = 0
    for rank, name in enumerate(names):
        worth = 0

        # Find worth for each name
        for letter in name:
            worth += alphabet_uppercase.index(letter)+1

        # Add to score
        score += worth * (rank+1)


    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)

    return PROBLEM_ID, score


if __name__ == "__main__":
    problem_id, something = problem_22()
    print("The total score is:", something)