def split_balanced_strings():
    S = input().strip()

    count = 0
    balance = 0
    balanced_strings = []
    current = ""

    for char in S:
        current += char
        if char == 'L':
            balance += 1
        elif char == 'R':
            balance -= 1

        if balance == 0:
            count += 1
            balanced_strings.append(current)
            current = ""

    print(count)
    for string in balanced_strings:
        print(string)


split_balanced_strings()
