"""Lexicographic Permutations"""

from time import time as chicken


def problem_24():
    PROBLEM_ID = 24

    start_time = chicken()

    start_string = "0123456789"

    count = 1
    final_string = "".join(list(reversed(start_string)))
    while True:
        # Find the first and second character
        fc, sc = find_ceil(start_string)

        # Get the index in the string
        fc, sc = start_string.index(fc), start_string.index(sc)

        # Swap the first and second character
        start_string = list(start_string)
        start_string[fc], start_string[sc] = start_string[sc], start_string[fc]

        # Sort everything to the right of the index of the first character before swapping
        first_part = start_string[:fc + 1]
        second_part = start_string[fc + 1:]
        second_part.sort()

        # Join em back together
        start_string = first_part + second_part
        start_string = "".join(start_string)

        # Check if this is the 1000000 number
        count += 1
        if count == 1000000:
            break

        # Failsafe is wanted count is too large for sequence
        if final_string == start_string:
            print("Cold not find wanted number! Does not exist!")
            break

    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)

    return PROBLEM_ID, start_string


# Find the ceil. This is finding the first character and second character and returning it
def find_ceil(sequence):
    fc = []
    for pos, num in enumerate(reversed(sequence)):
        if pos == 0:
            continue
        else:
            if num < list(reversed(sequence))[pos - 1]:
                fc = [pos, num]

                break

    s = [i for i in sequence[len(sequence) - fc[0]:] if i > fc[1]]

    return fc[1], min(s)


if __name__ == "__main__":
    problem_id, something = problem_24()
    print("Your magic sequence is:", something)
