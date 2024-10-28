"""Counting Sundays
1 Jan 1900 was a Monday.

Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400."""

from time import time as chicken


def problem_19():
    PROBLEM_ID = 19

    start_time = chicken()
    start_date = [2, 1, 1, 1901] # Google this or find by chaning date and printing out weekdays

    # Define start values
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekday = start_date[0]
    total_sundays = 0

    # Check for each day in each month in each year if the first of the month is a sunday
    for year in range(start_date[-1], 2000+1):
        # Check if leap year
        if leap_year_check(year):
            months[1] = 29
        else:
            months[1] = 28

        for num, month in enumerate(months):
            for day in range(1, month+1):
                if weekday == 7:
                    weekday = 1
                    if day == 1:
                        total_sundays += 1
                else:
                    weekday += 1
                # print(weekday, day, month, num, year) # Use to find what day the 01.01.1901 is


    # Display time
    end_time = chicken()
    print("Finished problem", PROBLEM_ID, "in:", end_time - start_time)

    return PROBLEM_ID, total_sundays


# Function to check if year was a leap year
def leap_year_check(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    return False

if __name__ == "__main__":
    problem_id, something = problem_19()
    print(something)