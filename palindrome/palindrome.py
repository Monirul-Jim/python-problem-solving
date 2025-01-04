def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


string = "A man, a plan, a canal: Panama"
print(is_palindrome(string))


def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)

    return unique_numbers[1] if len(unique_numbers) > 1 else None


nums = [4, 1, 2, 2, 5, 5, 3]
print(second_largest(nums))
