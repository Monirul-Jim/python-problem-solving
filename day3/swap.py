def swap_variables(a, b):
    """
    Swaps the values of two variables without using a temporary variable.

    Args:
      a: The first variable.
      b: The second variable.

    Returns:
      A tuple containing the swapped values of a and b.
    """
    a = a + b
    b = a - b
    a = a - b
    return a, b


# Example usage
x = 10
y = 5

print(f"Before swapping: x = {x}, y = {y}")

x, y = swap_variables(x, y)

print(f"After swapping: x = {x}, y = {y}")
