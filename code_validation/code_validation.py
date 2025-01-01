
# Code Validation

# বাং
# Problem Statement
# Write a program to create a function that determines whether a string is a valid code. A code must begin with a pound key # and is exactly 6 characters in length. Each character must be a digit from 0-9 or an alphabetic character from A-F. All alphabetic characters may be uppercase or lowercase.

# Input
# The program will take a string
# S
# S as input.

# Output
# The output will print either "true" or "false"

# Constraints
# 0 ≤ |S| ≤ 1000
# Example:
# Enter string

# Input:
# #CD5C5C
# Output:
# true

def is_valid_code(S):
    if len(S) == 7 and S[0] == '#':
        for char in S[1:]:
            if not (char.isdigit() or char.lower() in 'abcdef'):
                return False
        return True
    return False


S = input("Enter string: ")

if is_valid_code(S):
    print("true")
else:
    print("false")
