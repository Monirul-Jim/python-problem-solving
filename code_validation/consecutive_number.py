# Consecutive Numbers

# বাং
# Problem Statement
# Write a program to create a function that determines whether elements in an array can be re-arranged to form a consecutive list of numbers where each number appears exactly once. The difference between two numbers will be 1 always.

# Input
# The program will take an integer
# N
# N as the size of an array. Then it will take the integer values of the array
# M
# [
# ]
# M[].

# Output
# The output will print either "true" or "false"

# Constraints
# 0 ≤ |N| ≤ 100000
# 0 ≤ |M[]| ≤ 100000
# Example-1:
# Enter numbers

# Input:
# 5
# 4 2 3 1 0
# Output:
# true
# Example-2:
# Enter numbers

# Input:
# 6
# 1 2 3 4 4 5
# Output:
# false

def can_form_consecutive(N, M):
    if N <= 1:
        return True

    M.sort()

    for i in range(1, N):
        if M[i] != M[i - 1] + 1:
            return False

    return True


N = int(input())
M = list(map(int, input().split()))
if can_form_consecutive(N, M):
    print("true")
else:
    print("false")
