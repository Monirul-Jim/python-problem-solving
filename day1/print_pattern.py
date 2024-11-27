for row in range(4):
    for col in range(row+1):
        print('#', end=" ")
    print()


def print_diamond(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "#" * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "#" * (2 * i - 1))


n = int(input("Enter the size of the diamond: "))

print_diamond(n)
