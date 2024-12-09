# Leap Year Problem

# বাং
# Problem Statement
# Write a program that checks if a year entered by the user is a leap year or not.

# Input
# The input consists of an integer.

# Output
# Output will print the type of the year whether it is leap year or not.

# Constraints
# 0 ≤ |S| ≤ 231 - 1
# Example-1:
# Enter a year

# Input:
# 1900
# Output:
# 1900 is not a leap year.
# Example-2:
# Enter a year

# Input:
# 2020
# Output:
# 2020 is a leap year.
# Function to check leap year


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
