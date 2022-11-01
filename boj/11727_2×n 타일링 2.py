n = int(input())
dp = [0] * 1001

dp[1] = 1
dp[2] = 3

if n >= 3:
    for k in range(3, n+1):
        dp[k] = dp[k-2] * 2 + dp[k-1]

print(dp[n] % 10007)