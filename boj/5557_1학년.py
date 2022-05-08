import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N-1)]
dp[0][arr[0]] = 1

for i in range(1, N - 1):
    for j in range(21):
        if dp[i - 1][j]:
            next_value = arr[i]
            if 0 <= j + next_value <= 20:
                dp[i][j + next_value] += dp[i - 1][j]
            if 0 <= j - next_value <= 20:
                dp[i][j - next_value] += dp[i - 1][j]

print(dp[N - 2][arr[-1]])