import sys
input = sys.stdin.readline

N = int(input())
juice = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N+1)

dp[1] = juice[1]

if N >= 2:
    dp[2] = dp[1] + juice[2]

for k in range(3, N+1):
    dp[k] = max(dp[k-1], dp[k-2] + juice[k], dp[k-3] + juice[k-1] + juice[k])

print(dp[N])