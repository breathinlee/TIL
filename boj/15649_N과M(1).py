# sol 1 (파이썬만 가능)

from itertools import permutations
import sys

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

cases = permutations(arr, M)

for case in cases:
    for c in case:
        print(c, end=' ')
    print()



# sol 2

def dfs():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for k in range(1, N+1):
        if k not in result:
            result.append(k)
            dfs()
            result.pop()


N, M = map(int, input().split())
result = []

dfs()