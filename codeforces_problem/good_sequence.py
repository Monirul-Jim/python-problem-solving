def good_sequence():

    N = int(input())
    a = list(map(int, input().split()))

    freq = {}
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    removals = 0
    for x, count in freq.items():
        if x < count:
            removals += count - x
        elif x > count:
            removals += count

    print(removals)


good_sequence()
