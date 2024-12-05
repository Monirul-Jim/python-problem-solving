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
import math


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

# Two Point Distance

# বাং
# Problem Statement
# Write a program to calculate distance between two points.

# Input
# The input consists of four double numbers. the first two numbers indicate the co-ordinate of first point and the second two numbers indicate the co-ordinates of second point.

# Output
# Output is the distance of two points.

# Constraints
# The program should print the number with exactly two decimal points.
# Example:
# Enter the co-ordinates of two points.

# Input:
# 0 0
# 2 2
# Output:
# Distance: 2.83


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


print("Enter the co-ordinates of two points:")
x1, y1 = map(float, input("Point 1 (x1 y1): ").split())
x2, y2 = map(float, input("Point 2 (x2 y2): ").split())

distance = calculate_distance(x1, y1, x2, y2)

print(f"Distance: {distance:.2f}")

# Positive Negative

# বাং
# Problem Statement
# Write a program that checks if a number entered by the user is positive, negative, or zero.

# Input
# The input consists of a integer.

# Output
# Output the type of number.

# Constraints
# -2 31 ≤ |S| ≤ 231 - 1
# Example-1:
# Enter a number

# Input:
# 5
# Output:
# 5 is a positive number.
# Example-2:
# Enter a number

# Input:
# -3
# Output:
# -3 is a negative number.
# Example-3:
# Enter a number

# Input:
# 0
# Output:
# The number is zero.
# Input
number = int(input("Enter a number: "))

if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print("The number is zero.")

# Game of Swap

# বাং
# Problem Statement
# Write a program that swaps the values of two variables.

# Input
# The input consists of two integers.

# Output
# Output consists of two integers.

# Constraints
# -2 31 ≤ |S| ≤ 231 - 1
# Example:
# Enter two numbers

# Input:
# 10 20
# Output:
# Before swapping: num1 = 10, num2 = 20
# After swapping: num1 = 20, num2 = 10
# Input
print("Enter two numbers:")
num1, num2 = map(int, input().split())

print(f"Before swapping: num1 = {num1}, num2 = {num2}")

num1, num2 = num2, num1

print(f"After swapping: num1 = {num1}, num2 = {num2}")
