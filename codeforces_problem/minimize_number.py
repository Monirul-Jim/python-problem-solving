def max_operations():
    N = int(input())
    A = list(map(int, input().split()))

    operations = 0

    while all(x % 2 == 0 for x in A):
        A = [x // 2 for x in A]
        operations += 1

    print(operations)


max_operations()
