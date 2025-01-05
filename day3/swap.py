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
