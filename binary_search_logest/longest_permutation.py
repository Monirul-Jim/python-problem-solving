# Longest Substring Without Repeating Character

# বাং
# Problem Statement
# Write a program to find the length of the longest substring in a given string without repeating characters. For example, in the string "abcabcbb," the longest substring without repeating characters is "abc," which has a length of 3.

# Input
# The program will take a string as input.

# Output
# The output will be the length of the longest substring which will be an integer.

# Constraints
# 0 ≤ |S| ≤ 1000
# Example:
# Enter string

# Input:
# abcabcbb
# Output:
# 3
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


# Input handling
try:
    # Read the string input
    input_string = input("Enter string: ")

    # Calculate and print the length of the longest substring without repeating characters
    print(length_of_longest_substring(input_string))
except Exception as e:
    print("An error occurred:", e)
