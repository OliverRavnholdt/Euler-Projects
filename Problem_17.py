"""Number Letter Counts"""

from time import time as chicken

def problem_17():
    PROBLEM_ID = 17

    start_time = chicken()

    # Create one long word with all numbers in word format
    word = ""
    for i in range(1, 1001):
        word += num_to_word(i)

    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)

    return PROBLEM_ID, word


# Function that converts anu number less than 10000 to a word
def num_to_word(num):
    # From https://www.javatpoint.com/python-program-to-convert-a-given-number-into-words
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    word = ""
    num = str(num)

    if len(num) > 4:
        print("Too large number for now!")
        return None

    if len(num) > 3 and num[-4] != "0":
        word += ones[int(num[-4])] + "thousand"

    if len(num) > 2 and num[-3] != "0":
        word += ones[int(num[-3])] + "hundred"

    if len(num) > 2:
        if num[-2] == "0" and num[-1] == "0":
            pass
        else:
            word += "and"

    if len(num) > 1:
        if int(num[-2]) >= 2:
            word += tens[int(num[-2])]
        elif int(num[-2]) == 0:
            pass
        else:
            word += teens[int(num[-1])]
            return word

    if len(num) > 0:
        word += ones[int(num[-1])]

    return word

if __name__ == "__main__":
    problem_id, something = problem_17()
    print("This is a very long word:", something)
    print("The number you want is:", len(something))
