# String Permutation

# বাং
# Problem Statement
# Write a program to implement a function to generate all possible permutations of characters in a given string. For example, if the input is "abc," the output should include "abc," "acb," "bac," "bca," "cab," and "cba." The output answers will be in sorted order.

# Input
# The program will take a string as input.

# Output
# The output will be the possible strings after permutation.

# Constraints
# 0 ≤ |S| ≤ 100
# Example:
# Enter string

# Input:
# abc
# Output:
# abc acb bac bca cab cba
from itertools import permutations


def generate_permutations(s):
    return sorted(["".join(p) for p in permutations(s)])


s = input("Enter string: ")
print(" ".join(generate_permutations(s)))
