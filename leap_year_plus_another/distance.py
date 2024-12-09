

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
import math


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


print("Enter the co-ordinates of two points:")
x1, y1 = map(float, input("Point 1 (x1 y1): ").split())
x2, y2 = map(float, input("Point 2 (x2 y2): ").split())

distance = calculate_distance(x1, y1, x2, y2)

print(f"Distance: {distance:.2f}")
