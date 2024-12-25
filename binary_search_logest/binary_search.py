# Do Binary Search In Array

# বাং
# Problem Statement
# Write a program to find the index of a target element from a sorted array in logarithmic time. If the target element is in the array it will print it's index value. Otherwise it will print "Element not found".

# Input
# The program will take an integer
# N
# N as the size of a sorted array. Then it will take the integer values of the array
# M
# [
# ]
# M[]. Finally, it will take the target value
# P
# P.

# Output
# The output will print either the index of the target element or "Element not found" if the element is not found.

# Constraints
# 0 ≤ |N| ≤ 100000
# 0 ≤ |M[]| ≤ 100000
# 0 ≤ |P| ≤ 100000
# Example-1:
# Enter numbers

# Input:
# 5
# 10 20 30 40 50
# 20
# Output:
# 1
# Example-2:
# Enter numbers

# Input:
# 5
# 10 20 30 40 50
# 60
# Output:
# Element not found
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Input handling
try:
    # Read size of the array
    N = int(input("Enter the size of the array: "))
    if N == 0:
        print("Element not found")
    else:
        # Read array elements
        M = list(map(int, input("Enter the sorted array elements: ").split()))

        # Read the target element
        P = int(input("Enter the target element: "))

        # Perform binary search
        result = binary_search(M, P)

        if result != -1:
            print(result)
        else:
            print("Element not found")

except ValueError:
    print("Invalid input. Please enter valid integers.")
