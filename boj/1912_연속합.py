import sys
input = sys.stdin.readline

n = int(input())
dp = list(map(int, input().split()))

for k in range(1, n):
    dp[k] = max(dp[k], dp[k-1] + dp[k])

print(max(dp))