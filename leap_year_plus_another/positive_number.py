
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
