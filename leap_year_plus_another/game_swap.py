
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
