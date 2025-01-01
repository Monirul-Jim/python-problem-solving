
from itertools import combinations
user_input = input('Enter input : ')
for r in range(1, len(user_input)+1):
    combs = combinations(user_input, r)
    for comb in combs:
        print(''.join(comb))
