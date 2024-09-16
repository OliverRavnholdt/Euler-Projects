def problem_4():
    PROBLEM_ID = 4

    # Numbers to check for palindromes for
    x = 999
    y = 999

    num_list = []   # Placeholder for palindromes
    for i in reversed(range(x+1)):
        for j in reversed(range(y+1)):
            # Two values are assigned, the first is appended to list the other is modified under condition check
            save_num = i*j
            num = str(save_num)

            # Check if the number is a palindrome
            while True:
                check_result, num = number_checker(num) # 1: Result of check, 2: New modified number
                # If it's not a palindrome: Break the loop
                if not check_result:
                    break
                # No need to check middle number or when string is ""
                elif len(num) < 2:
                    num_list.append(save_num)
                    break

    return PROBLEM_ID, max(num_list)


# Helper function to check if the first and last digit is the same
def number_checker(number):
    if number[0] != number[-1]:
        return False, number
    elif len(number) >= 2:
        number = number[1:]
        number = number[:-1]

    return True, number


"""
This entire function could probably be solved by using something like:
num = str(j*i)
num_reverse = num[::-1]
num == num_reverse
I haven't tested and I don't know if this is less recourse intensive.
I would imagine that it uses less overhead.
"""
if __name__ == "__main__":
    problem_id, something = problem_4()
    print("The largest palindrome for problem:", problem_id, "is:", something)
