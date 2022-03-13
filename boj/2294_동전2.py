# sol1

import sys

n, k = map(int, sys.stdin.readline().split())
coin_value = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0] * (k + 1)

for s in range(1, k+1):
    temp = []
    for value in coin_value:
        if s >= value and dp[s-value] >= 0:
            temp.append(dp[s-value])
    dp[s] = min(temp) + 1 if temp else -1

print(dp[k])

# sol2

import sys

n, k = map(int, sys.stdin.readline().split())
coin_value = [int(sys.stdin.readline()) for _ in range(n)]

dp = [10001] * (k + 1)
dp[0] = 0

for value in coin_value:
    for s in range(value, k + 1):
        dp[s] = min(dp[s], dp[s - value]+1)

print(dp[k])